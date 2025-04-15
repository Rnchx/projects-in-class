print("PROGRAMA PARA DIZER QUANTOS DIVISORES IMPARES TEM UM NÚMERO NATURAL")

nro = int(input("Digite um número natural para dizer quantos divisores impares ele tem:  "))

possivel_divisor = 1
metade = nro // 2
divisores = 0
mostrar_divisores = []


while possivel_divisor <= metade:
    if nro % possivel_divisor == 1:
        divisores += 1
        mostrar_divisores.append(possivel_divisor)
    
    possivel_divisor += 1


print(nro, "tem", divisores, "divisores impares")
print("os divisores são: ", mostrar_divisores)
