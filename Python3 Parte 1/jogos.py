import adivinhacao

print("*********************************")
print("**Bem vindo ao Jogos em Python!**")
print("*********************************")

print("(1) Advinhação")
jogo = int(input("Jogo escolhido: "))

if(jogo == 1):
    adivinhacao.jogar()
else:
    print("Escolha um jogo válido")