def jogar():
    print("*********************************")
    print("****Bem vindo ao Jogo da Forca****")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    letras_acertadas = ["_", "_", "_", "_", "_", "_"] 
    
    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        
        chute = input("Qual letra?: ")
        chute = chute.strip()

        indice = 0
        for letra in palavra_secreta:
            if(chute.lower() == letra.lower()):
                letras_acertadas[indice] = letra
            indice = indice + 1
            
        
        print("{}\njogando...".format(letras_acertadas))


    print("Fim do Jogo")

if(__name__=="__main__"):
    jogar()