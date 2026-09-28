from dataclasses import dataclass


@dataclass(frozen=True)
class Habilidade:
    nome: str
    descricao: str
    atributo: str
    multiplicador: float = 1
    acrescimo: int = 0

    def aplicar(self, jogador):
        valor = getattr(jogador, self.atributo)
        setattr(jogador, self.atributo, valor * self.multiplicador + self.acrescimo)
        if self.atributo == "vida_maxima":
            jogador.vida = min(jogador.vida + 1, jogador.vida_maxima)


HABILIDADES = (
    Habilidade("Adubo potente", "+20% de dano nos próximos tiros.", "dano_tiro", 1.2),
    Habilidade("Fotossíntese acelerada", "+15% de velocidade de ataque.", "intervalo_tiro", 1 / 1.15),
    Habilidade("Casca resistente", "+1 de vida máxima e recupera 1 de vida.", "vida_maxima", acrescimo=1),
    Habilidade("Raízes coletoras", "+30% de alcance para atrair XP.", "raio_atracao_xp", 1.3),
    Habilidade("Espinhos perfurantes", "Cada tiro pode atingir mais 1 inimigo.", "perfuracoes", acrescimo=1),
)
