print("PROGRAMA PARA MOSTRAR SE OS NÚMEROS ESCOLHIDOS TEM DIVISORES COMPLEMENTARES")

nro1 = int(input("Digite o primeiro número natural:  "))
nro2 = int(input("Digite o segundo número natural:  "))

maior = nro1
menor = nro2

if nro1 < nro2:

    menor = nro1
    maior = nro2

complementares = 1
divisor = 1
divisoresMenor = []
divisoresMaior = []

while divisor <= menor:
    if menor % divisor == 0:
        if maior % divisor != 0:
            complementares = 0
    
    if menor % divisor == 0 and maior % divisor == 0:
        divisoresMenor.append(divisor)
        divisoresMaior.append(divisor)
    
    divisor += 1

if complementares == 1:
    print("Os números", menor, "e", maior, "tem divisores complementares!")
    print("Divisores de", menor, ":", divisoresMenor)
    print("Divisores de", maior, ":", divisoresMaior)
else:
    print("Os números", menor, "e", maior, "NÃO tem divisores complementares!")

