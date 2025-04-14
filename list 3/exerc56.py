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

            while nro != 0: # o número que vc digitou é 12345

                ultimo_nro = nro % 10  # 5, 4, 3 ... 1
                nro = nro // 10 # 1234, 123, 12 ... 0
                inv = inv*10 + ultimo_nro # na primeira vez que passar pelo while o INV = 5, INV = 54, INV = 543, INV = 5432 ... INV = 54321

            print(inv)
