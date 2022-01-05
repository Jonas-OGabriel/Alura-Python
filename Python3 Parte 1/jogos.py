import adivinhacao

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

print("(1) Advinhação")
jogo = int(input("Jogo escolhido: "))

if(jogo == 1):
    adivinhacao.jogar_advinhacao()
else:
    print("Escolha um jogo válido")