print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

for tentiva_atual in range(1,4):

    print("Tentativa {} de 3".format(tentiva_atual))
    tentativa = int(input("Digite um número - entre 1 e 100 - e tente acertar o número secreto: "))
    #Trativa de input do usuário
    if(tentativa < 1 or tentativa > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    condicao_acerto = tentativa == numero_secreto
    condicao_erro_maior = tentativa > numero_secreto
    condicao_erro_menor = tentativa < numero_secreto

    if(condicao_acerto):
        print("Parabens! Você acertou!")
        #Criando quebra de laço do repetição
        break
    else:
        if(condicao_erro_maior):
            print("Que pena, você errou... Sua tentiva foi maior do que número secreto")
        elif(condicao_erro_menor):
            print("Que pena, você errou... Sua tentiva foi menor do que número secreto")


print("Fim do jogo!")