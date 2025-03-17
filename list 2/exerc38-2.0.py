print("PROGRAMA PARA CLASSIFICAR TRIÂNGULOS COM BASE NOS ÂNGULOS")

try: # tentando conseguir a digitação de um número
    angulo1=float(input("Quanto mede em cm o 1º ângulo? "))
except ValueError: # quando der ruim
    print("O 1º ângulo deve ser numérico!")
else: # senão, quando não deu ruim
    if angulo1<=0 or angulo1>=180: # tenho um número, mas está fora da faixa válida
        print("O 1º ângulo deve ser maior que 0 e menor que 180 graus!")
    else: # tenho o 1º angulo apropriadamente digitado
        try: # tentando conseguir a digitação de um número
            angulo2=float(input("Quanto mede em cm o 2º ângulo? "))
        except ValueError: # quando der ruim
            print("O 2º ângulo deve ser numérico!")
        else: # senão, quando não deu ruim
            if angulo2<=0 or angulo2>=180: # tenho um número, mas está fora da faixa válida
                print("O 2º ângulo deve ser maior que 0 e menor que 180 graus!")
            else: # tenho o 2º angulo apropriadamente digitado
                if angulo1+angulo2>=180:
                    print(", esses ângulos não podem ser ângulos de um triângulo!")                        
                else:
                    try: # tentando conseguir a digitação de um número
                        angulo3=float(input("Quanto mede em cm o 3º ângulo? "))
                    except ValueError: # quando der ruim
                        print("O 3º ângulo deve ser numérico!")
                    else: # senão, quando não deu ruim
                        if angulo3<=0 or angulo3>=180: # tenho um número, mas está fora da faixa válida
                            print("O 3º ângulo deve ser maior que 0 e menor que 180 graus!")
                        else: # tenho o 3º angulo apropriadamente digitado
                            if angulo1+angulo2+angulo3!=180: # individualmente, todos os angulos estão OK, mas, em conjunto, não combinam para formar um triângulo
                                print(" esses ângulos não podem ser ângulos de um triângulo!")                        
                            else: # tenho os 3 ângulos de um triângulo
                                if angulo1<90 and angulo2<90 and angulo3<90: # tenho 3 ângulos agudos, "pontudinhos"
                                    print(" trata-se de um triângulo acutângulo!")
                                else: # acutângulo, o triângulo não é
                                    if angulo1==90 or angulo2==90 or angulo3==90: # tenho um ângulo reto
                                        print(" trata-se de um triângulo retângulo!")
                                    else: # nem acutângulo, nem retângulo o triângulo é; o que sobrou?
                                        print(" trata-se de um triângulo obtusângulo!")

print("PROGRAMA ENCERRADO!")