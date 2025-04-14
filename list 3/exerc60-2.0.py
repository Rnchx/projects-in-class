print('PROGRAMA PARA "DESENHAR" TRIÂNGULOS')

digitou_corretamente=False
while not digitou_corretamente:
    try:
        qtd_de_linhas=int(input("Quer um triângulo de quantas linhas (de 2 a 50)? "))
    except ValueError:
        print("A quantidade deve ser um número inteiro; tente novamente!")
    else:
        if qtd_de_linhas<2 or qtd_de_linhas>50:
            print("A quantidade deve ser de 2 a 50; tente novamente!")
        else:
            digitou_corretamente=True

qtd_de_espacos_iniciais=qtd_de_linhas-1 # na 1ª linha
qtd_de_espacos_intermediarios=1 # na 1ª linha que tem espaços intermediários
qtd_de_Os=1 # na 1ª linha tem 1 Os

nro_da_linha_sendo_escrita=0
while nro_da_linha_sendo_escrita<qtd_de_linhas:
    nro_da_linha_sendo_escrita+=1 # nro_da_linha_sendo_escrita=nro_da_linha_sendo_escrita+1
    
    nro_do_espaco_sendo_escrito=0
    while nro_do_espaco_sendo_escrito<qtd_de_espacos_iniciais:
        nro_do_espaco_sendo_escrito+=1 # nro_do_espaco_sendo_escrito=nro_do_espaco_sendo_escrito+1
        print(" ",end="")
        
    # preparação para a próxima linha
    qtd_de_espacos_iniciais-=1 # qtd_de_espacos_iniciais=qtd_de_espacos_iniciais-1
    
    nro_do_O_sendo_escrito=0
    while nro_do_O_sendo_escrito<qtd_de_Os:
        nro_do_O_sendo_escrito+=1 # nro_do_O_sendo_escrito=nro_do_O_sendo_escrito+1
        print("O",end="")

    print() # pula linha
    
    qtd_de_Os+=2
        
print("PROGRAMA ENCERRADO")    