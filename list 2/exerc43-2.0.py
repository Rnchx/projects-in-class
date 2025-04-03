print("Programa para escrever por extenso números inteiros de -99 a 99")

deseja_escrever_mais_numero_por_extenso = True

while deseja_escrever_mais_numero_por_extenso:
    digitou_corretamente = False

    while not digitou_corretamente:
        try:
            numero = int(input("Digite um nº por extenso de -99 a 99  "))
        except ValueError:
            print("Foi pedido um nº inteiro, tente novamente!!")
        else:
            if numero < -99 or numero > 99:
                print("O nº está fora da faixa válida, tente novamente!!")
            else:
                digitou_corretamente = True
    
    if numero < 0:
        print("Menos", end="")
        numero = -numero

    unidade = numero % 10
    dezena = numero // 10

    if dezena == 0 and unidade == 0:
        print("Zero", end="")
    elif dezena == 1:
        if unidade == 0:
            print("dez", end="")
        elif unidade == 1:
            print("onze", end="")
        elif unidade == 2:
            print("doze", end="")
        elif unidade == 3:
            print("treze", end="")
        elif unidade == 4:
            print("quatorze", end="")
        elif unidade == 5:
            print("quinze", end="")
        elif unidade == 6:
            print("dezesseis", end="")
        elif unidade == 7:
            print("dezessete", end="")
        elif unidade == 8:
            print("dezoito", end="")
        elif unidade == 9:
            print("dezenove", end="")
    elif dezena == 2:
        print("vinte", end="")
    elif dezena == 3:
        print("trinta", end="")
    elif dezena == 4:
        print("quarenta", end="")
    elif dezena == 5:
        print("cinquenta", end="")
    elif dezena == 6:
        print("sessenta", end="")
    elif dezena == 7:
        print("setenta", end="")
    elif dezena == 8:
        print("oitenta", end="")
    elif dezena == 9:
        print("noventa", end="")

    if dezena > 1 and unidade > 0:
        print(" e ", end="")

    if dezena != 1:
        if unidade == 1:
            print("um", end="")
        elif unidade == 2:
            print("dois", end="")
        elif unidade == 3:
            print("três", end="")
        elif unidade == 4:
            print("quatro", end="")
        elif unidade == 5:
            print("cinco", end="")
        elif unidade == 6:
            print("seis", end="")
        elif unidade == 7:
            print("sete", end="")
        elif unidade == 8:
            print("oito", end="")
        elif unidade == 9:
            print("nove", end="")
    
    print()