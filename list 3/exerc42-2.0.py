print("PROGRAMA PARA ESCREVER POR EXTENSO VALORES INTEIROS ENTRE -9 E 9")

resposta="S"
while resposta=="S":
    digitou_direito=False
    while not digitou_direito:
        try:
            numero=int(input("Quer escrever por extenso qual número? "))
        except ValueError:
            print("Era para digitar um valor inteiro; tente novamente!")
        else:
            if numero<-9 or numero>9:
                print("Era para digitar um valor entre -9 e 9; tente novamente!")
            else:
                digitou_direito=True
    
    if numero<0:
        print("Menos ",end="")
        numero=-numero
    
    if numero==0:
        print("Zero")
    elif numero==1:
        print("Um")
    elif numero==2:
        print("Dois")
    elif numero==3:
        print("Três")
    elif numero==4:
        print("Quatro")
    elif numero==5:
        print("Cinco")
    elif numero==6:
        print("Seis")
    elif numero==7:
        print("Sete")
    elif numero==8:
        print("Oito")
    else:
        print("Nove")
        
    digitou_direito=False
    while not digitou_direito:
        resposta=input("Deseja escrever mais números por extenso (S/N)? ")
        resposta=resposta.upper()
        if resposta!="S" and resposta!="N":
            print("Você deve responder S ou N; tente novamente")
        else:
            digitou_direito=True

print("PROGRAMA ENCERRADO!")