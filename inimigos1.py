import pygame
from config import XP_RAIO_ATRACAO, XP_VELOCIDADE_ATRACAO
#CLASSE PAI
class InimigoBase(pygame.sprite.Sprite):
    
    def __init__(self, x, y, velocidade, cor, vida_maxima , xp):
        super().__init__()
        self.velocidade = velocidade
        self.vida = vida_maxima
        self.image = pygame.Surface((40, 40))
        self.image.fill(cor)
        self.rect = self.image.get_rect(center=(x, y))
        self.xp = xp
    def update(self, jogador):
        # Todos os inimigos por padrão vão perseguir o jogador
        if self.rect.x < jogador.rect.x:
            self.rect.x += self.velocidade
        elif self.rect.x > jogador.rect.x:
            self.rect.x -= self.velocidade

        if self.rect.y < jogador.rect.y:
            self.rect.y += self.velocidade
        elif self.rect.y > jogador.rect.y:
            self.rect.y -= self.velocidade

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.kill()


#CLASSES FILHAs
class ZumbiComum(InimigoBase):
    def __init__(self, x, y):
        # Zumbi comum: Velocidade 2, Cor Vermelha, 3 de Vida
        super().__init__(x, y, velocidade=2, cor=(255, 0, 0), vida_maxima=3, xp=1)


class ZumbiCorredor(InimigoBase):
    def __init__(self, x, y):
        # Corredor: Mais rápido (Velocidade 4), Cor Laranja, 1 de Vida (morre fácil)
        super().__init__(x, y, velocidade=4, cor=(255, 165, 0), vida_maxima=1,xp=2)

class XP(pygame.sprite.Sprite):

    def __init__(self, x, y, quantidade):
        super().__init__()

        self.quantidade = quantidade
        self.velocidade = XP_VELOCIDADE_ATRACAO


        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect(center=(x, y))

    def update(self,jogador):
        xp_pos = pygame.math.Vector2(self.rect.center)
        jogador_pos = pygame.math.Vector2(jogador.rect.center)

        distancia = xp_pos.distance_to(jogador_pos)

        # só se move se estiver dentro do raio de atração
        if distancia <= XP_RAIO_ATRACAO and distancia > 0:
            direcao = (jogador_pos - xp_pos).normalize()
            self.rect.x += direcao.x * self.velocidade
            self.rect.y += direcao.y * self.velocidade