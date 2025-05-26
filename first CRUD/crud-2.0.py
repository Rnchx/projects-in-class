import re
from datetime import datetime

def apresenteSe():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| João Pedro Cassan da Rocha                                  |')
    print('|                                                             |')
    print('| Versão 2.0 de 26/05/2025                                    |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto(solicitacao, mensagem, valido):
    while True:
        txt = input(solicitacao).strip()
        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            return txt

def opcaoEscolhida(mnu):
    print()
    opcoesValidas = []
    for i, item in enumerate(mnu):
        print(f"{i+1}) {item}")
        opcoesValidas.append(str(i+1))
    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

def ondeEsta(nom, agd):
    inicio = 0
    final = len(agd) - 1
    while inicio <= final:
        meio = (inicio + final) // 2
        if agd[meio][0] == nom:
            return [True, meio]
        elif agd[meio][0] > nom:
            final = meio - 1
        else:
            inicio = meio + 1
    return [False, inicio]

# Validações

def validar_nome(nome):
    padrao = re.compile(r"^[A-ZÀ-Ý][a-zà-ÿ]*(?: (?:[A-ZÀ-Ý]|[a-zà-ÿ])[a-zà-ÿ]*)*$")
    return padrao.fullmatch(nome) is not None

def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validar_telefone(tel):
    return re.fullmatch(r"\d{4}-\d{4}", tel) is not None

def validar_celular(cel):
    return re.fullmatch(r"\(\d{2}\) \d{5}-\d{4}", cel) is not None

def validar_email(email):
    return re.fullmatch(r".+@(?:gmail|hotmail|yahoo)\.com", email) is not None

def validar_endereco(end):
    return not end.isdigit() and len(end) >= 3

def cadastrar(agd):
    while True:
        nome = input("Digite o nome para cadastro (ou 'cancela' para desistir): ").strip()
        if nome.lower() == 'cancela':
            print("Cadastro não realizado.")
            return
        if not validar_nome(nome):
            print("Nome inválido. Use letras maiúsculas no início, evite números ou símbolos.")
            continue
        achou, pos = ondeEsta(nome, agd)
        if achou:
            print("Nome já cadastrado. Digite outro nome.")
        else:
            aniversario = input("Digite a data de aniversário (dd/mm/aaaa): ").strip()
            if aniversario.lower() == 'cancela' or not validar_data(aniversario):
                print("Data inválida. Cadastro cancelado.")
                return

            endereco = input("Digite o endereço: ").strip()
            if endereco.lower() == 'cancela' or not validar_endereco(endereco):
                print("Endereço inválido. Cadastro cancelado.")
                return

            telefone = input("Digite o telefone fixo (0000-0000): ").strip()
            if telefone.lower() == 'cancela' or not validar_telefone(telefone):
                print("Telefone fixo inválido. Cadastro cancelado.")
                return

            celular = input("Digite o celular ((99) 00000-0000): ").strip()
            if celular.lower() == 'cancela' or not validar_celular(celular):
                print("Celular inválido. Cadastro cancelado.")
                return

            email = input("Digite o e-mail: ").strip()
            if email.lower() == 'cancela' or not validar_email(email):
                print("E-mail inválido. Cadastro cancelado.")
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
                    novo = input("Digite o novo aniversário (dd/mm/aaaa) ou 'cancela': ").strip()
                    if novo.lower() == 'cancela':
                        print("Atualização de aniversário cancelada.")
                    elif validar_data(novo):
                        contato[1] = novo
                        print("Aniversário atualizado com sucesso.")
                    else:
                        print("Data inválida. Tente novamente.")
                
                elif opc == 2:
                    novo = input("Digite o novo endereço ou 'cancela': ").strip()
                    if novo.lower() == 'cancela':
                        print("Atualização de endereço cancelada.")
                    elif validar_endereco(novo):
                        contato[2] = novo
                        print("Endereço atualizado com sucesso.")
                    else:
                        print("Endereço inválido (não pode ser só números). Tente novamente.")
                
                elif opc == 3:
                    novo = input("Digite o novo telefone fixo (0000-0000) ou 'cancela': ").strip()
                    if novo.lower() == 'cancela':
                        print("Atualização de telefone fixo cancelada.")
                    elif validar_telefone(novo):
                        contato[3] = novo
                        print("Telefone fixo atualizado com sucesso.")
                    else:
                        print("Telefone fixo inválido. Tente novamente.")
                
                elif opc == 4:
                    novo = input("Digite o novo celular ((99) 00000-0000) ou 'cancela': ").strip()
                    if novo.lower() == 'cancela':
                        print("Atualização de celular cancelada.")
                    elif validar_celular(novo):
                        contato[4] = novo
                        print("Celular atualizado com sucesso.")
                    else:
                        print("Celular inválido. Tente novamente.")
                
                elif opc == 5:
                    novo = input("Digite o novo e-mail ou 'cancela': ").strip()
                    if novo.lower() == 'cancela':
                        print("Atualização de e-mail cancelada.")
                    elif validar_email(novo):
                        contato[5] = novo
                        print("E-mail atualizado com sucesso.")
                    else:
                        print("E-mail inválido. Tente novamente.")
                
                elif opc == 6:
                    print("Finalizando atualizações.")
                    return
                
                else:
                    print("Opção inválida. Tente novamente.")
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

menu=['Cadastrar Contato',
      'Procurar Contato',
      'Atualizar Contato',
      'Listar Contatos',
      'Excluir Contato',
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
    else:
        deseja_terminar_o_programa=True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')
