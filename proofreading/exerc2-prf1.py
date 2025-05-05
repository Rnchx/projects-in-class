'''

Correção da 1º prova de algorítimo de programação

exercício 2

data da correção - 05/05/2025

'''
print ('PROGRAMA PARA DESCOBRIR DIVISORES COMPLEMENTARES')

nro1 = int(input("Digite um número natural: "))
nro2 = int(input("Digite outro número natural: "))

saoDivisoresComunsNro1 = True

if nro2 % nro1 != 0:
    saoDivisoresComunsNro1 = False
else:
    possivel_divisor = 2
    
    while possivel_divisor <= nro1 // 2:
        if nro1 % possivel_divisor == 0 and nro2 % possivel_divisor != 0:
            saoDivisoresComunsNro1 = False
            break
        possivel_divisor += 2

saoDivisoresComunsNro2 = True

if nro2 % nro1 != 0:
    saoDivisoresComunsNro2 = False
else:
    possivel_divisor = 2
    
    while possivel_divisor <= nro2 // 2:
        if nro2 % possivel_divisor == 0 and nro1 % possivel_divisor != 0:
            saoDivisoresComunsNro2 = False
            break
        possivel_divisor += 2

if saoDivisoresComunsNro1 and not saoDivisoresComunsNro2 or saoDivisoresComunsNro2 and not saoDivisoresComunsNro1:
    print(nro1, "e", nro2, "têm divisores complementares!")
else:
    print(nro1, "e", nro2, "não têm divisores complementares!")