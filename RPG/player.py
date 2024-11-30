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

cria_jogador("Disco")
info_jogador()

def ataque_jogador(vida_inimigo, ataque):
    vida_inimigo -= ataque
    pass

def checa_jogador():
    pass

def defesa_jogadro():
    pass

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