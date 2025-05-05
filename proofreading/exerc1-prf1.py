'''

Correção da 1º prova de algorítimo de programação

exercício 1

data da correção - 05/05/2025

'''
print ('PROGRAMA PARA CONTAR DIVISORES IMPARES DE UM NÚMERO')

nro = int(input("Digite um número natural: "))

possivel_divisor = 1
metade = nro // 2
divisores_impares = 0

while possivel_divisor <= metade:
    if nro % possivel_divisor == 1:
        divisores_impares += 1
    
    possivel_divisor += 1
    
print(nro, "tem", divisores_impares, "divisores impares")