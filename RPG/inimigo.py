from player import *
import random

inimigo = []

def nome_inimigo():
    lista_nome = ["Goblin Sombrio", "Dragão de Cinzas", "Espectro da Névoa", "Fera das Sombras", "Basilisco de Pedra", "Quimera Flamejante", "Golem de Ferro", "Vampiro Alado", "Lobo Fantasma", "Hidra do Abismo", "Aranha Colossal", "Troll da Montanha", "Esqueleto Guerreiro", "Serpente do Pântano", "Demônio de Fogo", "Wendigo Gélido", "Harpia Cantante", "Kraken Profundo", "Salamandra Ardente", "Manticora Venenosa"]
    nome = random.choice(lista_nome)
    return nome

def cria_inimigo():
    npc = {"nome": nome_inimigo(),
               "level": "1",
               "hp": 100,
               "hp-max": 100,
               "dano": 5,
               "defesa": 3,
               "cric" : 0.05,
               "exp" : 1,
               "esquiva": 10,
               "prec": 90,
               "velocidade": 60
               }
    inimigo.append(npc)

def gera_inimigo(quantidade):
    for x in range(quantidade):
        cria_inimigo()

def info_inimigos():
    for x in inimigo:
        print(x)


def ataque_inimigo():
    print("O inimigo está atacando:")
    esquivaPlayer = esquiva_jogador(jogador[0]['esquiva'])
    if esquivaPlayer is True:
        print("errou o ataque")
    else:
        jogador[0]['hp'] -= inimigo[0]['dano']
        print("Acertou o ataque")

def esquiva_inimigo(esquiva):
    valor = random.randint(0,100)
    if valor > esquiva:
        print("Inimigo não esquivou com: ",esquiva)
        print("Valor tirado: ",valor)
        return False
    else:
        print("Inimigo esquivou do ataque com: ",esquiva)
        print("Valor tirado: ",valor)
        return True

def morre_inimigo(hp):
    if hp <= 0:
        print("Inimigo morreu")


gera_inimigo(1)
info_inimigos()