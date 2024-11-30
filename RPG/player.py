from inimigo import *
import random

jogador = []

def cria_jogador(name):
    player = {"nome": name,
               "level": "1",
               "hp": 100,
               "hp-max": 100,
               "dano": 7,
               "defesa": 5,
               "cric" : 0.1,
               "exp" : 1,
               "exp-max": 50,
               "esquiva": 30,
               "prec": 95,
               "velocidade": 60
               }
    jogador.append(player)

def info_jogador():
    for jogo in jogador:
        print(f"Nome: {jogo['nome']} -- Level: {['level']}\nExp: {jogo['exp']}-{jogo['exp-max']}\nHP: {jogo['hp']}-{jogo['hp-max']}\nDano: {jogo['dano']}\nDefesa: {jogo['defesa']}\n")

def ataque_jogador(vida_inimigo, ataque):
    print("Você está atacando:")
    esquivainimigo = esquiva_inimigo(inimigo[0]['esquiva'])
    if esquivainimigo is True:
        print("errou o ataque")
    else:
        inimigo[0]['hp'] -= jogador[0]['dano']
        print("Acertou o ataque")
        vida_inimigo -= ataque

def esquiva_jogador(esquiva):
    valor = random.randint(0,100)
    if valor > esquiva:
        print("Você não esquivou com: ",esquiva)
        print("Valor tirado: ",valor)
        return False
    else:
        print("Você esquivou do ataque com: ",esquiva)
        print("Valor tirado: ",valor)
        return True

def levelUp_jogador():
    pass

def morre_jogador():
    pass

def checa_jogador():
    pass

def defesa_jogadro():
    pass

cria_jogador("Disco")
info_jogador()