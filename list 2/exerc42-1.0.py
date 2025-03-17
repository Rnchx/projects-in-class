print("PROGRAMA PARA ESCREVER POR EXTENSO VALORES INTEIROS ENTRE -9 E 9")

try:
    numero=int(input("Quer escrever por extenso qual número? "))
except ValueError:
    print("Era para digitar um valor inteiro!")
else:
    if numero<-9 or numero>9:
        print("Era para digitar um valor entre -9 e 9!")
    else:
        if numero<0:
            print("Menos ",end="")
            numero=-numero

        if numero==0:
            print("Zero")
        else:
            if numero==1:
                print("Um")
            else:
                if numero==2:
                    print("Dois")
                else:
                    if numero==3:
                        print("Três")
                    else:
                        if numero==4:
                            print("Quatro")
                        else:
                            if numero==5:
                                print("Cinco")
                            else:
                                if numero==6:
                                    print("Seis")
                                else:
                                    if numero==7:
                                        print("Sete")
                                    else:
                                        if numero==8:
                                            print("Oito")
                                        else:
                                            print("Nove")
print("PROGRAMA ENCERRADO!")