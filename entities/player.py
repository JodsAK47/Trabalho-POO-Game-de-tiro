import pygame
from entities.base import Entidade
from config import LARGURA, ALTURA, JOGADOR_VELOCIDADE, JOGADOR_VIDA_INICIAL, COR_JOGADOR, JOGADOR_TAMANHO


class Jogador(Entidade):
    
    def __init__(self, x, y):
       
        super().__init__(x, y, JOGADOR_VELOCIDADE, JOGADOR_TAMANHO)
        self.image.fill(COR_JOGADOR)
        self.vida = JOGADOR_VIDA_INICIAL

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.mover(0, -self.velocidade)
        if keys[pygame.K_s]:
            self.mover(0, self.velocidade)
        if keys[pygame.K_a]:
            self.mover(-self.velocidade, 0)
        if keys[pygame.K_d]:
            self.mover(self.velocidade, 0)

        self.rect.x = max(0, min(self.rect.x, LARGURA - JOGADOR_TAMANHO))
        self.rect.y = max(0, min(self.rect.y, ALTURA - JOGADOR_TAMANHO))

    def tomar_dano(self, dano=1):
        self.vida -= dano
        return self.vida <= 0  #caso o jogador morra, retorna True
