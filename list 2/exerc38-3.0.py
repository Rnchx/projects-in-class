print("Programa para classificar triângulos com base nos ângulos")

somaDosAngulos = False
while not somaDosAngulos:
    
    primeiroAngulo = False
    while not primeiroAngulo:
        try:
            angulo1=float(input("Quanto mede em graus o 1º ângulo? "))
        except ValueError:
            print("O 1º ângulo deve ser numérico!")
        else:
            if angulo1 <= 0 or angulo1 >= 180:
                print("O 1º ângulo deve ser maior que 0 e menor que 180 graus!")
            else:
                primeiroAngulo = True

    segundoAngulo = False
    while not segundoAngulo:
        try:
            angulo2=float(input("Quanto mede em graus o 2º ângulo? "))
        except ValueError:
            print("O 2º ângulo deve ser numérico!")
        else:
            if angulo2 <= 0 or angulo2 >= 180:
                print("O 2º ângulo deve ser maior que 0 e menor que 180 graus!")
            else:
                if angulo1 + angulo2 >= 180:
                    print("Esses ângulos não podem ser ângulos de um triângulo!")                         
                else:
                    segundoAngulo = True

    terceiroAngulo = False
    while not terceiroAngulo:
        try:
            angulo3=float(input("Quanto mede em graus o 3º ângulo? "))
        except ValueError:
            print("O 3º ângulo deve ser numérico!")
        else:
            if angulo3 <= 0 or angulo3 >= 180:
                print("O 3º ângulo deve ser maior que 0 e menor que 180 graus!")
            else:                     
                terceiroAngulo = True

if angulo1 + angulo2 + angulo3 != 180:
    print("Esses ângulos não podem ser ângulos de um triângulo!")
else: somaDosAngulos = True                

if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print("Trata-se de um triângulo acutângulo!")
else:
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("Trata-se de um triângulo retângulo!")
    else:
        print("Trata-se de um triângulo obtusângulo!")
