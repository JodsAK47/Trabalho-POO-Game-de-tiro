import pygame
import random
from entities.player import Jogador
from inimigos1 import XP
from entities.projectile import Tiro
from inimigos1 import ZumbiComum, ZumbiCorredor
from config import (
    LARGURA, ALTURA, FPS, COR_FUNDO, COR_TEXTO,
    SPAWN_INTERVALO, TAXA_ZUMBI_COMUM, TIRO_DANO,
    INIMIGOS_RODADA_INICIAL,
    AUMENTO_INIMIGOS_POR_RODADA,
    TEMPO_ENTRE_RODADAS
)


class Game:
    #classe do loop principal
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Garden Survivors")
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.SysFont(None, 30)

        # Sprites groups
        self.todos_sprites = pygame.sprite.Group()
        self.inimigos = pygame.sprite.Group()
        self.tiros = pygame.sprite.Group()      
        self.xps = pygame.sprite.Group()
        
        # Criar jogador
        self.jogador = Jogador(LARGURA // 2, ALTURA - 60)
        self.todos_sprites.add(self.jogador)
        #variaveis
        self.pontos = 0
        self.xp = 0
        self.nivel = 1
        self.tempo_inicio = pygame.time.get_ticks()
        self.tempo_final = None
        
        self.xp_maximo = 10
        self.spawn_timer = 0
        self.rodando = True
        self.tempo_ultimo_tiro = 0
        self.intervalo_tiro = 180
        #rodadas
        self.rodada = 1
        self.inimigos_para_spawnar = INIMIGOS_RODADA_INICIAL
        self.inimigos_spawnados = 0
        self.tempo_entre_rodadas = 0
        self.aguardando_proxima_rodada = False


    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False

        teclas = pygame.key.get_pressed()
        agora = pygame.time.get_ticks()

        if teclas[pygame.K_SPACE] and agora - self.tempo_ultimo_tiro >= self.intervalo_tiro:
            self.disparar_tiro()
            self.tempo_ultimo_tiro = agora

    def disparar_tiro(self):
        tiro = Tiro(self.jogador.rect.centerx, self.jogador.rect.y)
        self.todos_sprites.add(tiro)
        self.tiros.add(tiro)

    def spawnar_inimigo(self):
        lado = random.randint(0, 3)
        
        if lado == 0:  # Topo
            x = random.randint(-40, LARGURA + 40)
            y = -40
        elif lado == 1:  # Baixo
            x = random.randint(-40, LARGURA + 40)
            y = ALTURA + 40
        elif lado == 2:  # Esquerda
            x = -40
            y = random.randint(-40, ALTURA + 40)
        else:  # Direita
            x = LARGURA + 40
            y = random.randint(-40, ALTURA + 40)

        #aleatoriedade dos zumbis
        if random.random() < TAXA_ZUMBI_COMUM:
            novo_inimigo = ZumbiComum(x, y)
        else:
            novo_inimigo = ZumbiCorredor(x, y)

        self.todos_sprites.add(novo_inimigo)
        self.inimigos.add(novo_inimigo)

    def verificar_colisoes(self):
       
        #Colisão tiro e zumbi
        colisoes_tiros = pygame.sprite.groupcollide(
            self.inimigos, self.tiros, False, True
        )
        for zumbi, tiros_nele in colisoes_tiros.items():
            for tiro in tiros_nele:
                zumbi.tomar_dano(TIRO_DANO)
                if zumbi.vida <= 0:
                    self.pontos += 1
                    xp = XP(
                        zumbi.rect.centerx,
                        zumbi.rect.centery,
                        zumbi.xp
                    )
                    self.todos_sprites.add(xp)
                    self.xps.add(xp)
        xps_coletados = pygame.sprite.spritecollide(
            self.jogador,
            self.xps,
            True
            )

        for xp in xps_coletados:
            self.xp += xp.quantidade

            if self.xp >= self.xp_maximo:
                self.xp -= self.xp_maximo
                self.nivel += 1

                print(f"LEVEL UP! Agora você está no nível {self.nivel}")
        #colisão zumbi e jogador
        if pygame.sprite.spritecollide(self.jogador, self.inimigos, True):
            if self.jogador.tomar_dano():
                print("GAME OVER!")
                self.tempo_final = pygame.time.get_ticks()
                self.rodando = False

    def atualizar(self):
        # Timer de spawn
        if not self.aguardando_proxima_rodada:

            if self.inimigos_spawnados < self.inimigos_para_spawnar:

                self.spawn_timer += 1

                if self.spawn_timer >= SPAWN_INTERVALO:
                    self.spawnar_inimigo()
                    self.inimigos_spawnados += 1
                    self.spawn_timer = 0

    # quando morrer todo mundo e rodada acabar
            elif len(self.inimigos) == 0:
                self.aguardando_proxima_rodada = True
                self.tempo_entre_rodadas = TEMPO_ENTRE_RODADAS

        else:
    #contagem para próxima rodada
            self.tempo_entre_rodadas -= 1
            if self.tempo_entre_rodadas <= 0:
                self.iniciar_proxima_rodada()

        self.jogador.update()
        self.tiros.update()

        for inimigo in self.inimigos:
            inimigo.update(self.jogador)
        self.verificar_colisoes()

    def iniciar_proxima_rodada(self):
        self.rodada += 1
    # Aumenta quantidade de inimigos
        self.inimigos_para_spawnar = (
            INIMIGOS_RODADA_INICIAL +
            (self.rodada - 1) * AUMENTO_INIMIGOS_POR_RODADA
    )
        self.inimigos_spawnados = 0
        self.spawn_timer = 0
        self.aguardando_proxima_rodada = False
        print(f"rodada {self.rodada}")

    def desenhar(self):
        self.tela.fill(COR_FUNDO)
        self.todos_sprites.draw(self.tela)

    # Relógio
        if self.tempo_final is None:
            tempo_atual = pygame.time.get_ticks()
            tempo = (tempo_atual - self.tempo_inicio) // 1000
        else:
            tempo = (self.tempo_final - self.tempo_inicio) // 1000

    # HUD
        texto = self.fonte.render(
            f"Rodada: {self.rodada} | Vida: {self.jogador.vida} | "
            f"Pontos: {self.pontos} | Nível: {self.nivel} | "
            f"Tempo: {tempo}s",
            True,
            COR_TEXTO
        )

        self.tela.blit(texto, (10, 10))

    # Barra de XP
        largura_barra = 400
        altura_barra = 12

        x_barra = (LARGURA - largura_barra) // 2
        y_barra = ALTURA - 25

        # Fundo da barra
        pygame.draw.rect(
            self.tela,
            (50, 50, 50),
            (x_barra, y_barra, largura_barra, altura_barra)
        )

        # Progresso
        progresso = self.xp / self.xp_maximo

        pygame.draw.rect(
            self.tela,
            (0, 255, 100),
            (
                x_barra,
                y_barra,
                largura_barra * progresso,
                altura_barra
            )
        )

        pygame.display.flip()

    def executar(self):
        #loop principal
        while self.rodando:
            self.clock.tick(FPS)
            self.processar_eventos()
            self.atualizar()
            self.desenhar()

        pygame.quit()
