import random

def jogar():
    print("*********************************")
    print("****Bem vindo ao Jogo da Forca****")
    print("*********************************")

    
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()


    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False

    erros = 0
    
    
    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        
        chute = input("\nQual letra?: ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            indice = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[indice] = letra
                indice += 1
        else:
            erros += 1
            print("\nOps, você errou!\nA palavra não tem a letra {}\n\nVocê ainda tem {} tentativas.\n\n".format(chute,6-erros))
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        
        print("{}\njogando...".format(letras_acertadas))
    
    if(acertou):
        print("Você ganhou! A palavra secreta era {}".format(palavra_secreta))
    else:
        print("Que pena... Você Perdeu!")


    print("Fim do Jogo")

if(__name__=="__main__"):
    jogar()