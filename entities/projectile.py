import pygame
from entities.base import Entidade
from config import TIRO_VELOCIDADE, COR_TIRO, TIRO_TAMANHO, LARGURA, ALTURA



class Tiro(Entidade):

    def __init__(self, x, y, direcao):
        super().__init__(x, y, TIRO_VELOCIDADE, TIRO_TAMANHO)
        self.image.fill(COR_TIRO)
        self.dano = 1
        self.direcao = direcao
        
    def update(self):
        self.rect.x += self.direcao.x * self.velocidade
        self.rect.y += self.direcao.y * self.velocidade
       #atualiza o tiro e o remove ao sair da tela

        if (self.rect.right < 0 or self.rect.left > LARGURA or
                self.rect.bottom < 0 or self.rect.top > ALTURA):
            self.kill()