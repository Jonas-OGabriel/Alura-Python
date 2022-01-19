def jogar():
    print("*********************************")
    print("****Bem vindo ao Jogo da Forca****")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"] 

    enforcou = False
    acertou = False

    erros = 0
    
    
    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        
        chute = input("Qual letra?: ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            indice = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[indice] = letra
                indice += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        
        print("{}\njogando...".format(letras_acertadas))
    
    if(acertou):
        print("Você ganhou!")
    else:
        print("Você Perdeu!")


    print("Fim do Jogo")

if(__name__=="__main__"):
    jogar()