"""Artes compartilhadas, carregadas a partir da pasta do projeto."""
from functools import lru_cache
from pathlib import Path

import pygame

RAIZ = Path(__file__).resolve().parent
PERSONAGENS = {
    "cacto": {"nome": "Cacto", "sprite": "pixilart-sprite.png", "tiro": "tiro do cacto.png"},
    "ervilheiro": {"nome": "Ervilheiro", "sprite": "ervilheiro.png", "tiro": "tiro ervilheiro.png"},
    "lirio": {"nome": "Lírio", "sprite": "lirio.png", "tiro": "tiro do lirio.png"},
}


@lru_cache(maxsize=None)
def carregar_imagem(caminho):
    return pygame.image.load(str(RAIZ / caminho)).convert_alpha()


@lru_cache(maxsize=None)
def carregar_frames(personagem, tamanho):
    sheet = carregar_imagem("ARTES/" + PERSONAGENS[personagem]["sprite"])
    lado = sheet.get_height()
    return tuple(
        pygame.transform.scale(sheet.subsurface((x, 0, lado, lado)), (tamanho, tamanho))
        for x in range(0, sheet.get_width(), lado)
    )


@lru_cache(maxsize=None)
def carregar_tiro(personagem):
    sheet = carregar_imagem("ARTES/" + PERSONAGENS[personagem]["tiro"])
    # As artes contêm duas orientações; a metade direita aponta para a direita.
    largura = sheet.get_width() // 2
    sprite = sheet.subsurface((largura, 0, largura, sheet.get_height()))
    return pygame.transform.scale(sprite, (largura * 2, sheet.get_height() * 2))


def criar_mapa(tamanho):
    piso = carregar_imagem("ARTES/deserto.png")
    mapa = pygame.Surface(tamanho)
    for y in range(0, tamanho[1], piso.get_height()):
        for x in range(0, tamanho[0], piso.get_width()):
            mapa.blit(piso, (x, y))
    return mapa
