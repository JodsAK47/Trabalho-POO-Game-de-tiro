import math
import pygame
from entities.base import Entidade
from assets import carregar_frames

from config import (
    LARGURA,
    ALTURA,
    JOGADOR_VELOCIDADE,
    JOGADOR_VIDA_INICIAL,
    JOGADOR_TAMANHO
)


class Jogador(Entidade):
    """Planta selecionada, animada por uma faixa horizontal de sprites."""

    def __init__(self, x, y, personagem="cacto"):
        super().__init__(x, y, JOGADOR_TAMANHO, JOGADOR_VELOCIDADE)

        self.vida = JOGADOR_VIDA_INICIAL

        # animação
        self.frames = []
        self.frame_index = 0
        self.frame_delay = 6  # frames do jogo por frame de animação
        self._frame_timer = 0

        # bob (efeito de pulo ao mover)
        self.base_y = self.rect.centery
        self.bob_timer = 0
        self.bob_amplitude = 6
        self.bob_speed = 0.018  # controla a frequência do "pulo"

        self.personagem = personagem
        self.frames = carregar_frames(personagem, JOGADOR_TAMANHO)

        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.base_y = self.rect.centery

    def mover(self, dx, dy):
        # mover horizontalmente altera o rect; mover verticalmente altera a
        # posição base (`base_y`) para que o efeito de bobbing não anule
        # o movimento vertical do jogador.
        self.rect.x += dx
        self.base_y += dy

    def _animate(self, moving: bool):
        if len(self.frames) <= 1:
            return

        if moving:
            self._frame_timer += 1
            if self._frame_timer >= self.frame_delay:
                self._frame_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image = self.frames[self.frame_index]
        else:
            # frame de idle
            self.frame_index = 0
            self.image = self.frames[0]

    def update(self):
        keys = pygame.key.get_pressed()

        dx = dy = 0
        if keys[pygame.K_w]:
            dy -= self.velocidade
        if keys[pygame.K_s]:
            dy += self.velocidade
        if keys[pygame.K_a]:
            dx -= self.velocidade
        if keys[pygame.K_d]:
            dx += self.velocidade

        moving = dx != 0 or dy != 0

        if moving:
            self.mover(dx, dy)
            # bob timer avança enquanto se move
            self.bob_timer += self.bob_speed * (abs(dx) + abs(dy))
        else:
            # desacelera o bob timer para suavizar retorno
            self.bob_timer *= 0.9

        # animação de frames
        self._animate(moving)

        # efeito de pulo (bobbing) baseado em seno
        bob_offset = int(math.sin(self.bob_timer) * self.bob_amplitude)
        self.rect.centery = self.base_y + bob_offset

        # Impede o jogador de sair da tela
        self.rect.x = max(0, min(self.rect.x, LARGURA - JOGADOR_TAMANHO))
        self.base_y = max(JOGADOR_TAMANHO // 2, min(self.base_y, ALTURA - JOGADOR_TAMANHO // 2))

    def tomar_dano(self, dano=1):
        self.vida -= dano
        return self.vida <= 0


class Personagem_2(Entidade):
    def __init__(self, x, y):
        super().__init__(x, y, JOGADOR_TAMANHO, JOGADOR_VELOCIDADE)
        self.image.fill((255, 0, 0))
        self.vida = JOGADOR_VIDA_INICIAL