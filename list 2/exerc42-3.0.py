print("PROGRAMA PARA ESCREVER POR EXTENSO VALORES INTEIROS ENTRE -9 E 9")

try:
    numero=int(input("Quer escrever por extenso qual número? "))
except ValueError:
    print("Era para digitar um valor inteiro!")
else:
    if numero<-9 or numero>9:
        print("Era para digitar um valor entre -9 e 9!")
    else:
        copia=numero
        if numero<0:
            numero=-numero

        if numero==0:
            print("Zero",end="")
        elif numero==1:
            print("Um",end="")
        elif numero==2:
            print("Dois",end="")
        elif numero==3:
            print("Três",end="")
        elif numero==4:
            print("Quatro",end="")
        elif numero==5:
            print("Cinco",end="")
        elif numero==6:
            print("Seis",end="")
        elif numero==7:
            print("Sete",end="")
        elif numero==8:
            print("Oito",end="")
        else:
            print("Nove",end="")
            
        if copia<0:
            print(" Negativo",end="")

print("\nPROGRAMA ENCERRADO!")