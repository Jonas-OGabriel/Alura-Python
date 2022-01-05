import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    #Adicionado pontuação do usuário
    pontos = 1000
    numero_secreto = random.randrange(1,101)
    #print(numero_secreto)

    #Adicionando escolha para usuário ter opções de dificuldade
    print("Qual o nível de dificuldade?")
    print("(1)Fácil (2)Médio (3)Difícil")
    nivel = int(input("Nivel: "))

    if(nivel == 1):
        total_tentativas = 5
    elif(nivel == 2):
        total_tentativas = 3
    else:
        total_tentativas = 1;

    for tentiva_atual in range(1,total_tentativas + 1):

        print("Tentativa {} de {}".format(tentiva_atual, total_tentativas))
        tentativa = int(input("Digite um número - entre 1 e 100 - e tente acertar o número secreto: "))
        if(tentativa < 1 or tentativa > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        condicao_acerto = tentativa == numero_secreto
        condicao_erro_maior = tentativa > numero_secreto
        condicao_erro_menor = tentativa < numero_secreto

        if(condicao_acerto):
            print("Parabens! Você acertou!")
            print("Sua pontuação final: {}".format(pontos))
            break
        else:
            if(condicao_erro_maior):
                print("Que pena, você errou... Sua tentiva foi maior do que número secreto")
            elif(condicao_erro_menor):
                print("Que pena, você errou... Sua tentiva foi menor do que número secreto")
            pontos = pontos - abs(numero_secreto - tentativa)

        if(pontos <= 0):
            break


    print("Fim do jogo!")
    print("Sua pontuação final: {}".format(pontos))
    print("O numero secreto era: {}".format(numero_secreto))