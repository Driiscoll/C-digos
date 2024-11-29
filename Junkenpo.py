import random

cpu = ["papel", "pedra", "tesoura"]

player = input("pedra, papel ou tesoura: ")

cpu = random.choice(cpu)

if cpu == "pedra" and player == "papel":
    print("Jogador Venceu!!")
elif cpu == "pedra" and player == "tesoura":
    print("CPU Venceu")
elif cpu == "papel" and player == "pedra":
    print("CPU Venceu")
elif cpu == "papel" and player == "tersoura":
    print("Jogador Venceu!!")
elif cpu == "tesoura" and player == "papel":
    print("CPU Venceu")
elif cpu == "tesoura" and player == "pedra":
    print("Jogador Venceu!!")
else:
    print("jogo empatado")