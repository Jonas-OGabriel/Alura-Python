def jogar():
    print("*********************************")
    print("****Bem vindo ao Jogo da Forca****")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        chute = input("Qual letra?: ")
        chute = chute.strip()

        for letra in palavra_secreta:
            if(chute.lower() == letra):
                print(chute, end="")
            else:
                print("_", end="")

        print("\njogando...")


    print("Fim do Jogo")

if(__name__=="__main__"):
    jogar()