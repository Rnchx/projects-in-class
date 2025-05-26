def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Profs André Carvalho & J.G.Pícolo                           |')
    print('|                                                             |')
    print('| Versão 1.0 de 12/maio/2025                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio <= final:
        meio = (inicio + final) // 2

        if agd[meio][0] == nom:
            return [True, meio]
        
        elif agd[meio] > nom:
            final = meio - 1

        else:
            inicio = meio + 1

    return [False, inicio]

def cadastrar(agd):
    while True:
        nome = input("Digite o nome para cadastro (ou 'cancela' para desistir): ").strip()
        if nome.lower() == 'cancela':
            print("Cadastro não realizado.")
            return
        if nome == '':
            print("Nome não pode ser vazio. Tente novamente.")
            continue

        achou, pos = ondeEsta(nome, agd)
        if achou:
            print("Nome já cadastrado. Digite outro nome.")
        else:
            aniversario = input("Digite a data de aniversário (dd/mm/aaaa): ").strip()
            if aniversario.lower() == 'cancela':
                print("Cadastro não realizado.")
                return

            endereco = input("Digite o endereço: ").strip()
            if endereco.lower() == 'cancela':
                print("Cadastro não realizado.")
                return

            telefone = input("Digite o telefone fixo: ").strip()
            if telefone.lower() == 'cancela':
                print("Cadastro não realizado.")
                return

            celular = input("Digite o celular: ").strip()
            if celular.lower() == 'cancela':
                print("Cadastro não realizado.")
                return

            email = input("Digite o e-mail: ").strip()
            if email.lower() == 'cancela':
                print("Cadastro não realizado.")
                return

            contato = [nome, aniversario, endereco, telefone, celular, email]
            agd.insert(pos, contato)
            print(f"Cadastro do contato '{nome}' realizado com sucesso!")
            return


def procurar(agd):
    while True:
        nome = input("Digite o nome para procurar (ou 'cancela' para desistir): ").strip()
        if nome.lower() == 'cancela':
            print("Busca cancelada.")
            return
        achou, pos = ondeEsta(nome, agd)
        if achou:
            contato = agd[pos]
            print("Contato encontrado:")
            print(f"Nome: {contato[0]}")
            print(f"Aniversário: {contato[1]}")
            print(f"Endereço: {contato[2]}")
            print(f"Telefone fixo: {contato[3]}")
            print(f"Celular: {contato[4]}")
            print(f"E-mail: {contato[5]}")
            return
        else:
            print("Contato não encontrado. Tente novamente.")


def atualizar(agd):
    while True:
        nome = input("Digite o nome para atualizar (ou 'cancela' para desistir): ").strip()
        if nome.lower() == 'cancela':
            print("Atualização cancelada.")
            return
        achou, pos = ondeEsta(nome, agd)
        if achou:
            contato = agd[pos]
            submenu = [
                "Atualizar aniversário",
                "Atualizar endereço",
                "Atualizar telefone fixo",
                "Atualizar celular",
                "Atualizar e-mail",
                "Finalizar atualizações"
            ]
            while True:
                print("\nO que deseja atualizar?")
                opc = int(opcaoEscolhida(submenu))
                if opc == 1:
                    novo = input("Digite o novo aniversário (ou 'cancela'): ").strip()
                    if novo.lower() == 'cancela':
                        print("Atualização cancelada.")
                    else:
                        contato[1] = novo
                        print("Aniversário atualizado.")
                elif opc == 2:
                    novo = input("Digite o novo endereço (ou 'cancela'): ").strip()
                    if novo.lower() == 'cancela':
                        print("Atualização cancelada.")
                    else:
                        contato[2] = novo
                        print("Endereço atualizado.")
                elif opc == 3:
                    novo = input("Digite o novo telefone fixo (ou 'cancela'): ").strip()
                    if novo.lower() == 'cancela':
                        print("Atualização cancelada.")
                    else:
                        contato[3] = novo
                        print("Telefone fixo atualizado.")
                elif opc == 4:
                    novo = input("Digite o novo celular (ou 'cancela'): ").strip()
                    if novo.lower() == 'cancela':
                        print("Atualização cancelada.")
                    else:
                        contato[4] = novo
                        print("Celular atualizado.")
                elif opc == 5:
                    novo = input("Digite o novo e-mail (ou 'cancela'): ").strip()
                    if novo.lower() == 'cancela':
                        print("Atualização cancelada.")
                    else:
                        contato[5] = novo
                        print("E-mail atualizado.")
                else:
                    print("Atualizações finalizadas.")
                    return
        else:
            print("Contato não encontrado. Tente novamente.")


def listar(agd):
    if len(agd) == 0:
        print("Nenhum contato cadastrado.")
        return
    print("\nLista de contatos cadastrados:")
    for contato in agd:
        print('-' * 40)
        print(f"Nome: {contato[0]}")
        print(f"Aniversário: {contato[1]}")
        print(f"Endereço: {contato[2]}")
        print(f"Telefone fixo: {contato[3]}")
        print(f"Celular: {contato[4]}")
        print(f"E-mail: {contato[5]}")
    print('-' * 40)


def excluir(agd):
    while True:
        nome = input("Digite o nome para excluir (ou 'cancela' para desistir): ").strip()
        if nome.lower() == 'cancela':
            print("Exclusão cancelada.")
            return
        achou, pos = ondeEsta(nome, agd)
        if achou:
            contato = agd[pos]
            print("Contato encontrado:")
            print(f"Nome: {contato[0]}")
            print(f"Aniversário: {contato[1]}")
            print(f"Endereço: {contato[2]}")
            print(f"Telefone fixo: {contato[3]}")
            print(f"Celular: {contato[4]}")
            print(f"E-mail: {contato[5]}")
            confirma = input("Confirma exclusão? (s/n): ").strip().lower()
            if confirma == 's':
                agd.pop(pos)
                print(f"Contato '{nome}' excluído com sucesso!")
            else:
                print("Exclusão não realizada.")
            return
        else:
            print("Contato não encontrado. Tente novamente.")


apresenteSe()

agenda=[]

menu=['Cadastrar Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

deseja_terminar_o_programa=False
while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        cadastrar(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    else: # opcao==6
        deseja_terminar_o_programa=True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')