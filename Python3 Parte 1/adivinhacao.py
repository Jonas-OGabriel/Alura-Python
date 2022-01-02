print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

#O código abaixo salvará o input do usuário como string
#chute = input("Digite o seu numero: ")

#O código int() converte o valor de input para tipo int
chute = int(input("Digite o seu numero: "))

print("Você digitou", chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou")

print("Fim do jogo!")

#O código acima sempre dará "Você errou" pois os tipos das variaveis são diferentes
#print(type(numero_secreto), type(chute))
