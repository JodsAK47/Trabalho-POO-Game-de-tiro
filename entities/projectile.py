"""
Classe Tiro - projéteis disparados pelo jogador
"""
import pygame
from entities.base import Entidade
from config import TIRO_VELOCIDADE, COR_TIRO, TIRO_TAMANHO


class Tiro(Entidade):

    def __init__(self, x, y):
        super().__init__(x, y, TIRO_VELOCIDADE, TIRO_TAMANHO)
        self.image.fill(COR_TIRO)
        self.dano = 1

    def update(self):
       #atualiza o tiro e o remove ao sair da tela
        self.rect.y -= self.velocidade
        if self.rect.y < 0:
            self.kill()  #remove o sprite de todos os grupos
