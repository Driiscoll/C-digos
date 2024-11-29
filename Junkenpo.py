from random import choice
placarPlayer = 0
placarCpu = 0

while True:
    try:
        opcoes = ["papel", "pedra", "tesoura"]
        player = input("pedra, papel ou tesoura: ")
        if player not in opcoes:
            print("Escolha inválida, tente novamente:\n")
            continue
        cpu = choice(opcoes)
        print("a CPU escolheu: ", cpu)
        if cpu == "pedra" and player == "papel":
            print("Jogador Venceu!!")
            placarPlayer += 1
        elif cpu == "pedra" and player == "tesoura":
            print("CPU Venceu")
            placarCpu += 1
        elif cpu == "papel" and player == "pedra":
            print("CPU Venceu")
            placarCpu += 1
        elif cpu == "papel" and player == "tersoura":
            print("Jogador Venceu!!")
            placarPlayer += 1
        elif cpu == "tesoura" and player == "papel":
            print("CPU Venceu")
            placarCpu += 1
        elif cpu == "tesoura" and player == "pedra":
            print("Jogador Venceu!!")
            placarPlayer += 1
        else:
            print("jogo empatado")

        print("\nSegue placar do jogo:\nJogador: ",placarPlayer,"\nCPU: ",placarCpu)
        
        novamente = input("\nGostaria de jogar novamente?\n1 = sim\n2 = não\n")
        if novamente != "1":
            break
    except Exception as e:
        print(e)