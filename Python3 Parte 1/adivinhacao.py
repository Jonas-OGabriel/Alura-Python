print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
tentiva_atual = 1

while(tentiva_atual <= 3):
    #Formatando a string da função print()
    print("Tentaiva {} de 3".format(tentiva_atual))
    tentativa = int(input("Digite um número e tente acertar o número secreto: "))

    condicao_acerto = tentativa == numero_secreto
    condicao_erro_maior = tentativa > numero_secreto
    condicao_erro_menor = tentativa < numero_secreto

    if(condicao_acerto):
        print("Parabens! Você acertou!")
    else:
        if(condicao_erro_maior):
            print("Que pena, você errou... Sua tentiva foi maior do que número secreto")
        elif(condicao_erro_menor):
            print("Que pena, você errou... Sua tentiva foi menor do que número secreto")
    
    tentiva_atual = tentiva_atual + 1

print("Fim do jogo!")