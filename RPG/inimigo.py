import random
inimigo = []

def nome_inimigo():
    lista_nome = ["Goblin Sombrio", "Dragão de Cinzas", "Espectro da Névoa", "Fera das Sombras", "Basilisco de Pedra", "Quimera Flamejante", "Golem de Ferro", "Vampiro Alado", "Lobo Fantasma", "Hidra do Abismo", "Aranha Colossal", "Troll da Montanha", "Esqueleto Guerreiro", "Serpente do Pântano", "Demônio de Fogo", "Wendigo Gélido", "Harpia Cantante", "Kraken Profundo", "Salamandra Ardente", "Manticora Venenosa"]
    nome = range(lista_nome)
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
               "esquiva": 0.1,
               "prec": 0.9,
               "velocidade": 60
               }
    inimigo.append(npc)

def gera_inimigo(quantidade):
    for x in quantidade:
        cria_inimigo()

def ataque_inimigo():
    pass


def morre_inimigo():
    pass