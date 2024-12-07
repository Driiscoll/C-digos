from inimigo import *
import random

jogador = []

def cria_jogador(name):
    player = {"nome": name,
               "level": 1,
               "hp": 100,
               "hp-max": 100,
               "dano": 7,
               "defesa": 5,
               "crit" : 10,
               "exp" : 1,
               "exp-max": 50,
               "esquiva": 30,
               "prec": 95,
               "velocidade": 60
               }
    jogador.append(player)

def info_jogador():
    for jogo in jogador:
        print(f"""
        Informações da Party:
Nome: {jogo['nome']} -- Level: {jogo['level']}
Exp: {jogo['exp']}-{jogo['exp-max']}
HP: {jogo['hp']}-{jogo['hp-max']}
Dano: {jogo['dano']}
Defesa: {jogo['defesa']}
Critico: {jogo['crit']}/100
Precisão: {jogo['prec']}/100
Velocidade: {jogo['velocidade']}
""")

def inimigo_selecionado(valor):
    inimigo_escolhido = inimigo[valor]
    return inimigo_escolhido

def ataque_jogador(vida_inimigo, ataque):
    print("Você está atacando:")
    esquivainimigo = esquiva_inimigo(inimigo[0]['esquiva']) # trocar valor fixos
    if esquivainimigo is True:
        print("errou o ataque")
    else:
        if chance_critico == True:
            inimigo[0]['hp'] -= jogador[0]['dano'] #trocar valores fixos futuramente
            print("Acertou o ataque CRITICO")
            vida_inimigo -= ataque*jogador[0]['crit']
        else:
            inimigo[0]['hp'] -= jogador[0]['dano'] - inimigo[0]['defesa'] #trocar valores fixos futuramente
            print("Acertou o ataque")
            vida_inimigo -= ataque

def chance_critico(crit):
    valor = random.randint(0,100)
    if valor > crit:
        return False
    else:
        return True

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
    while jogador[0]['exp'] >= jogador[0]['exp-max']:
        exp_restante = jogador[0]['exp'] - jogador[0]['exp-max']
        jogador[0]['exp'] = exp_restante
        jogador[0]['level'] = jogador[0]['level']+1
        jogador[0]['hp-max'] = jogador[0]['hp-max']+random.randint(10,50)
        jogador[0]['dano'] = jogador[0]['dano']+random.randint(5,10)
        jogador[0]['defesa'] = jogador[0]['defesa']+random.randint(5,10)
        jogador[0]['crit'] = jogador[0]['crit']+random.randint(1,5)
        jogador[0]['exp-max'] = jogador[0]['exp-max']+jogador[0]['exp-max']*2
        jogador[0]['esquiva'] = jogador[0]['esquiva']+random.randint(5,10)
        jogador[0]['velocidade'] = jogador[0]['velocidade']+random.randint(5,10)
        info_jogador()

def morre_jogador():
    if 0 >= jogador[0]['hp']:
        del jogador[0]
        print("Jogador morreu")
        return True
    else:
        return False

def checar_jogador():
    pass
