print("PROGRAMA PARA ESCREVER POR EXTENSO VALORES INTEIROS ENTRE 0 E 9")

try:
    numero=int(input("Quer escrever por extenso qual número? "))
except ValueError:
    print("Era para digitar um valor inteiro!")
else:
    if numero<0 or numero>9:
        print("Era para digitar um valor entre 0 e 9!")
    elif numero==0:
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

print("PROGRAMA ENCERRADO!")