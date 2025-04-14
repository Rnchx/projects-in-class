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

