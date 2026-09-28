import pygame
from entities.base import Entidade
from assets import carregar_tiro
from config import TIRO_VELOCIDADE, TIRO_TAMANHO, TIRO_DANO, LARGURA, ALTURA


class Tiro(Entidade):
    def __init__(self, x, y, direcao, personagem="cacto"):
        super().__init__(x, y, TIRO_TAMANHO, TIRO_VELOCIDADE)
        self.direcao = pygame.Vector2(direcao)
        angulo = self.direcao.angle_to(pygame.Vector2(1, 0)) if self.direcao.length_squared() else 0
        self.image = pygame.transform.rotate(carregar_tiro(personagem), angulo)
        self.rect = self.image.get_rect(center=(x, y))
        self.posicao = pygame.Vector2(x, y)
        self.dano = TIRO_DANO

    def update(self):
        self.posicao += self.direcao * self.velocidade
        self.rect.center = (round(self.posicao.x), round(self.posicao.y))
        if (self.rect.right < 0 or self.rect.left > LARGURA or
                self.rect.bottom < 0 or self.rect.top > ALTURA):
            self.kill()
