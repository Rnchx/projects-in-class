print("PROGRAMA PARA CLASSIFICAR TRIÂNGULOS COM BASE NOS ÂNGULOS")

os_3_angulos_combinam=False
while not os_3_angulos_combinam:
    primeiros_2_angulos_digitados_combinam=False
    while not primeiros_2_angulos_digitados_combinam:
        digitou_corretamente=False
        while not digitou_corretamente:
            try: # tentando obter número; posso me dar mal
                angulo1=float(input("Quanto mede em graus o 1º ângulo? "))
            except ValueError: # se der ruim...
                print("O 1º ângulo de um triângulo deve ser numérico; tente novamente!")
            else: # senão, ou seja, se não der ruim...
                if angulo1<=0 or angulo1>=180: # 1º angulo é número, mas está fora da faixa válida
                    print("O 1º ângulo deve ser maior que 0 e menor que 180 graus; tente novamente!")
                else: # 1º angulo é número e está na faixa válida
                    digitou_corretamente=True
            
        digitou_corretamente=False
        while not digitou_corretamente:
            try: # tentando obter número; posso me dar mal
                angulo2=float(input("Quanto mede em graus o 2º ângulo? "))
            except ValueError: # se der ruim...
                print("O 2º ângulo de um triângulo deve ser numérico; tente novamente!")
            else: # senão, ou seja, se não der ruim...
                if angulo2<=0 or angulo2>=180: # 2º angulo é número, mas está fora da faixa válida
                    print("O 2º ângulo deve ser maior que 0 e menor que 180 graus; tente novamente!")
                else: # 2º angulo é número e está na faixa válida
                    digitou_corretamente=True
                    
        if angulo1+angulo2>=180:
            print("Os 2 primeiros ângulos não podem ser ângulos de um triângulo; tente novamente!")
        else:
            primeiros_2_angulos_digitados_combinam=True
            
    digitou_corretamente=False
    while not digitou_corretamente:
        try: # tentando obter número; posso me dar mal
            angulo3=float(input("Quanto mede em graus o 3º ângulo? "))
        except ValueError: # se der ruim...
            print("O 3º ângulo de um triângulo deve ser numérico!")
        else: # senão, ou seja, se não der ruim...
            if angulo3<=0 or angulo3>=180: # 3º angulo é número, mas está fora da faixa válida
                print("O 3º ângulo deve ser maior que 0 e menor que 180 graus!")
            else: # 3º angulo é número e está na faixa válida
                digitou_corretamente=True
        
    if angulo1+angulo2+angulo3!=180: # os 3 ângulos não combinam e não formam um triângulo
        print("Esses ângulos não podem ser ângulos de um triângulo!")
    else: # os 3 ângulos combinam e formam um triângulo
        os_3_angulos_combinam=True

if angulo1<90 and angulo2<90 and angulo3<90: # temos 3 ângulos agudos, "pontudinhos"
    print("Trata-se de um triângulo acutângulo!")
else:
    if angulo1==90 or angulo2==90 or angulo3==90:
        print("Trata-se de um triângulo retângulo!")
    else: # ser obtusângulo é o que sobrou
        print("Trata-se de um triângulo obtusângulo!")

print("PROGRAMA ENCERRADO!")