import pygame
import random
from entities.player import Jogador
from entities.projectile import Tiro
from inimigos1 import ZumbiComum, ZumbiCorredor
from config import (
    LARGURA, ALTURA, FPS, COR_FUNDO, COR_TEXTO,
    SPAWN_INTERVALO, TAXA_ZUMBI_COMUM, TIRO_DANO
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
        
        # Criar jogador
        self.jogador = Jogador(LARGURA // 2, ALTURA - 60)
        self.todos_sprites.add(self.jogador)
        
        # Variáveis de jogo
        self.pontos = 0
        self.spawn_timer = 0
        self.rodando = True

    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.disparar_tiro()

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

        #Colisão zumbi e jogador
        if pygame.sprite.spritecollide(self.jogador, self.inimigos, True):
            if self.jogador.tomar_dano():
                print("GAME OVER!")
                self.rodando = False

    def atualizar(self):
        # Timer de spawn
        self.spawn_timer += 1
        if self.spawn_timer > SPAWN_INTERVALO:
            self.spawnar_inimigo()
            self.spawn_timer = 0

        self.jogador.update()
        self.tiros.update()
        for inimigo in self.inimigos:
            inimigo.update(self.jogador)

        
        self.verificar_colisoes()

    def desenhar(self):
        self.tela.fill(COR_FUNDO)
        self.todos_sprites.draw(self.tela)

        #hudzinha la de cima 
        texto = self.fonte.render(
            f"Vida: {self.jogador.vida}  |  Pontos: {self.pontos}",
            True, COR_TEXTO
        )
        self.tela.blit(texto, (10, 10))

        pygame.display.flip()

    def executar(self):
        #loop principal
        while self.rodando:
            self.clock.tick(FPS)
            self.processar_eventos()
            self.atualizar()
            self.desenhar()

        pygame.quit()
