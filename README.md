# 🌱 lilium's Decay

Um jogo de sobrevivência inspirado em **Brotato**, onde plantas guerreiras enfrentam hordas intermináveis de zumbis para proteger o jardim.

---

## 📖 Sobre o Jogo

**Garden Survivors** é um jogo de ação e sobrevivência em arena desenvolvido com **Python** e **Pygame**.

O jogador controla uma planta armada que deve sobreviver a ondas cada vez mais difíceis de zumbis. Durante a partida, é possível coletar recursos, evoluir atributos e desbloquear novas habilidades para enfrentar inimigos mais poderosos.

A proposta combina a progressão rápida e frenética de Brotato com um universo de plantas e mortos-vivos.

---

## 🎮 Gameplay

* Movimentação livre pelo mapa.
* Ataques automáticos.
* Ondas progressivas de inimigos.
* Sistema de evolução entre rodadas.
* Diferentes plantas jogáveis.
* Diversos tipos de zumbis.
* Chefes especiais.
* inimigos que surgem em maior quantidade e mais rapido a cada rodada que passa(Usando contadores e quantidades de inimigos)

---

## 🌿 Plantas Disponíveis

### 🟢 Ervilheiro

* Alta velocidade de ataque.
* Dano moderado.

### 🌵 Cacto

* Alto dano por disparo.
* Menor velocidade de movimento.

### 🌻 Girassol Guerreiro

* Regeneração de vida.
* Atributos equilibrados.

### 🦷 Planta Carnívora

* Especialista em combate corpo a corpo.
* Grande resistência.

---

## 🧟 Inimigos

| Inimigo        | Características           |
| -------------- | ------------------------- |
| Zumbi Comum    | Equilibrado               |
| Zumbi Corredor | Muito rápido              |
| Zumbi Tanque   | Grande quantidade de vida |
| Zumbi Tóxico   | Aplica dano contínuo      |
| Chefe Zumbi    | Extremamente resistente   |

---

## ⭐ Sistema de Melhorias

Ao subir de nível, o jogo pausa e oferece três habilidades diferentes sorteadas
entre as cinco abaixo. Clique em um cartão ou pressione **1, 2 ou 3** para escolher.

| Habilidade | Efeito por escolha |
| --- | --- |
| Adubo potente | +20% de dano nos próximos tiros |
| Fotossíntese acelerada | +15% de velocidade de ataque |
| Casca resistente | +1 de vida máxima e recupera 1 de vida |
| Raízes coletoras | +30% de alcance de atração do XP |
| Espinhos perfurantes | Cada tiro pode atingir mais 1 inimigo |

As melhorias se acumulam durante a partida; os percentuais são aplicados sobre
o valor atual. Cada projétil causa dano apenas uma vez em cada inimigo.
Se uma coleta render vários níveis, cada nível concede uma escolha, em sequência.
Uma nova partida reinicia todos os atributos.

---

## 🎯 Objetivo

Sobreviver ao maior número possível de ondas e derrotar os chefes que surgem durante a partida.

---

## 🎮 Controles

| Tecla | Função              |
| ----- | ------------------- |
| W     | Mover para cima     |
| A     | Mover para esquerda |
| S     | Mover para baixo    |
| D     | Mover para direita  |
| ESC   | Voltar ao menu e encerrar a partida atual |

---

### Menu e sprites implementados

No menu inicial, clique em **Jogar** ou pressione Enter/Espaço para abrir a seleção.
Depois, selecione **Cacto**, **Ervilheiro** ou **Lírio** com o mouse, A/D ou as setas.
Clique em **Iniciar partida** ou pressione Enter/Espaço para começar.
Na seleção, **Voltar** ou ESC retorna ao menu inicial.
Cada planta usa sua animação e seu projétil; os atributos de combate continuam iguais.
O cenário da partida usa a textura `ARTES/deserto.png` repetida pelo mapa.

ESC durante a partida retorna ao menu; ao jogar novamente, a partida começa do zero.
Ao perder toda a vida, o jogo também retorna ao menu inicial. ESC no menu ou **Sair** fecha o jogo.

## 🛠️ Tecnologias Utilizadas

* Python 3
* Pygame

---

## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/garden-survivors.git
```

Acesse a pasta do projeto:

```bash
cd garden-survivors
```

Instale as dependências:

```bash
pip install pygame
```

Execute o jogo:

```bash
python main.py
```

---

## 📂 Estrutura do Projeto

```text
garden-survivors/
│
├── assets/
│   ├── sprites/
│   ├── sounds/
│   └── backgrounds/
│
├── src/
│   ├── player.py
│   ├── enemy.py
│   ├── projectile.py
│   ├── wave_manager.py
│   └── game.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📸 Screenshots

Adicione imagens do jogo aqui:

```markdown
![Gameplay](assets/screenshots/gameplay.png)
```

---

## 🔮 Funcionalidades Futuras

* Sistema de loja permanente
* Novas plantas jogáveis
* Mais tipos de zumbis
* Habilidades únicas
* Sistema de conquistas
* Salvamento de progresso
* Multiplayer local

---

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Faça um Fork do projeto
2. Crie uma branch para sua feature

```bash
git checkout -b minha-feature
```

3. Commit suas alterações

```bash
git commit -m "Adiciona nova funcionalidade"
```

4. Envie para o GitHub

```bash
git push origin minha-feature
```

5. Abra um Pull Request

---

## 📜 Licença

Este projeto está sob a licença MIT.

---

Desenvolvido com ❤️ utilizando Python e Pygame.
