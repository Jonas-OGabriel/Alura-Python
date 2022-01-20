import random

def jogar():
    
    mensagem_abertura()
    
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    game_loop(palavra_secreta, letras_acertadas)
    
    print("Fim do Jogo")

def mensagem_abertura():
    print("**********************************")
    print("****Bem vindo ao Jogo da Forca****")
    print("**********************************")

def carrega_palavra_secreta(nome_arquivo="palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("\nQual letra?: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    indice = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[indice] = letra
        indice += 1

def checa_vencedor(acertou, palavra_secreta):
    if(acertou):
        print("Você ganhou! A palavra secreta era {}".format(palavra_secreta))
    else:
        print("Que pena... Você Perdeu!")

def game_loop(palavra_secreta, letras_acertadas):
    
    enforcou = False
    acertou = False
    erros = 0
    
    while(not enforcou and not acertou):
        
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            print("\nOps, você errou!\nA palavra não tem a letra {}\n\nVocê ainda pode errar {} vez(es).\n\n".format(chute,7-erros))
            desenha_forca(erros)
        
        enforcou = erros == 7
        
        acertou = "_" not in letras_acertadas
        
        print("{}\njogando...".format(letras_acertadas))

    checa_vencedor(acertou, palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__=="__main__"):
    jogar()