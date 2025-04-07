print("programa para calcular e escrever números naturais ao contrário")

digitou_o_numero_corretamente = False

while not digitou_o_numero_corretamente:
    try:
        nro=int(input("Digite um número natural para que o programa imprima ele ao contrário:  "))
    except ValueError:
        print("Por favor digite apenas números")
    else:
        if nro < 0:
            print("Por favor digite apenas números naturais, ou seja apenas números positivos")
        else:

            inv = 0

            while nro != 0:

                ultimo_nro = nro % 10
                nro = nro // 10
                inv = inv*10 + ultimo_nro
            
            print(inv)
