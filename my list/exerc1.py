print ('Programa para dizer se um número é par ou impar!')

digitouCorretamente = False
while not digitouCorretamente:
    try:
        nro = int(input("Digite um número natural:  "))
    except ValueError:
        print("Por favor Digite apenas números no campo acima!")
    else:
        if nro < 0:
            print("Por favor digite apenas números naturais!!")
        else:
            digitouCorretamente = True

if nro % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")