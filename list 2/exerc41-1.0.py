print("PROGRAMA PARA ESCREVER POR EXTENSO VALORES INTEIROS ENTRE 0 E 9")

try:
    numero=int(input("Quer escrever por extenso qual número? "))
except ValueError:
    print("Era para digitar um valor inteiro!")
else:
    if numero<0 or numero>9:
        print("Era para digitar um valor entre 0 e 9!")
    else:
        if numero==0:
            print("Zero")
        if numero==1:
            print("Um")
        if numero==2:
            print("Dois")
        if numero==3:
            print("Três")
        if numero==4:
            print("Quatro")
        if numero==5:
            print("Cinco")
        if numero==6:
            print("Seis")
        if numero==7:
            print("Sete")
        if numero==8:
            print("Oito")
        if numero==9:
            print("Nove")

print("PROGRAMA ENCERRADO!")