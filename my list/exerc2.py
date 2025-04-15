print("Programa para descobrir se o número é primo!")

digitou_certo = False

while not digitou_certo:
    try:
        nro = int(input("Digite um número:  "))
    except ValueError:
        print("Digite apenas números!!")
    else:
        if nro < 0:
            print("Digite apenas números inteiros!")
        else:
            digitou_certo = True

possivel_divisor = 2
metade = nro // 2
eh_primo = True

while possivel_divisor <= metade:
    if nro % possivel_divisor == 0:
        eh_primo = False
        break

    possivel_divisor += 1

if eh_primo == True and nro != 1:
    print(nro, "é primo")
else:
    print(nro, "não é primo")