import datetime

lista_alunos = []

def cadastrar_aluno(lista):
    nome = input('Insira o nome do aluno(a): ')

    while True:
        try:
            idade = int(input('Insira a idade do aluno(a): '))
            break
        except ValueError:
            print('Idade inválida. Digite uma idade válida (número inteiro).')

    plano = input('Escolha o seu plano (mensal, trimestral ou anual): ')
    contato = input('Insira informações para contato (whatsapp, e-mail): ')

    aluno = {
        'nome': nome,
        'idade': idade,
        'plano': plano,
        'contato': contato
    }

    lista.append(aluno)
    print(f'\nAluno(a) {nome} cadastrado com sucesso! Seja bem-vindo!\n')

def listar_alunos(lista):
    if not lista:
        print('\nNenhum aluno(a) cadastrado.\n')
        return

    print('\n>>>> Lista de alunos <<<<')
    for aluno in lista:
        print(f'Nome: {aluno["nome"]}')
        print(f'Idade: {aluno["idade"]}')
        print(f'Plano: {aluno["plano"]}')
        print(f'Contato: {aluno["contato"]}')
        print('-' * 30)

def buscar_aluno(lista, nome):
    for aluno in lista:
        if aluno['nome'].lower() == nome.lower():
            return aluno
    return None

def remover_aluno(lista, nome):
    for aluno in lista:
        if aluno['nome'].lower() == nome.lower():
            lista.remove(aluno)
            print(f'\nAluno {nome} removido com sucesso!\n')
            return
    print(f'\nAluno {nome} não encontrado.\n')

lista_frequencia = []

def registrar_entrada(lista_frequencia, nome):
    data_atual = datetime.datetime.now().strftime('%d/%m/%Y')
    hora_entrada = datetime.datetime.now().strftime('%H:%M')

    frequencia = {
        'nome': nome,
        'data': data_atual,
        'entrada': hora_entrada,
        'saida': None
    }
    lista_frequencia.append(frequencia)
    print(f'Entrada registrada para {nome} às {hora_entrada}.')

def registrar_saida(lista_frequencia, nome):
    data_atual = datetime.datetime.now().strftime('%d/%m/%Y')
    hora_saida = datetime.datetime.now().strftime('%H:%M')

    for registro in lista_frequencia:
        if registro['nome'].lower() == nome.lower() and registro['data'] == data_atual and registro['saida'] is None:
            registro['saida'] = hora_saida
            print(f'Saída registrada para {nome} às {hora_saida}.')
            return
    print(f'O(a) aluno(a) {nome} ainda não entrou. Registre a entrada primeiro.')

def listar_frequencia(lista_frequencia):
    if not lista_frequencia:
        print('Nenhum registro de frequência.')
        return

    for registro in lista_frequencia:
        print(f"{registro['nome']} - {registro['data']} - Entrada: {registro['entrada']} - Saída: {registro['saida']}")

def salvartxt(lista_frequencia, nome_arquivo='frequencia.txt'):
    with open(nome_arquivo, 'w') as arquivo:
        for registro in lista_frequencia:
            linha = f"{registro['nome']},{registro['data']},{registro['entrada']},{registro['saida']}\n"
            arquivo.write(linha)

def carregar_txt(lista_frequencia, nome_arquivo='frequencia.txt'):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                nome, data, entrada, saida = linha.strip().split(',')
                registro = {
                    'nome': nome,
                    'data': data,
                    'entrada': entrada,
                    'saida': saida if saida != 'None' else None
                }
                lista_frequencia.append(registro)
    except FileNotFoundError:
        pass

def aluno_existe(nome):
    """Verifica se o aluno está cadastrado na lista de alunos."""
    return any(a['nome'].lower() == nome.lower() for a in lista_alunos)

def menu_frequencia():
    carregar_txt(lista_frequencia)
    while True:
        print('\n--- Menu de Controle de Acesso ---')
        print('1 - Registrar entrada')
        print('2 - Registrar saída')
        print('3 - Listar frequência')
        print('0 - Voltar ao menu principal')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            nome = input('Digite o nome do aluno: ')
            if not aluno_existe(nome):
                print(f"Aluno {nome} não está cadastrado! Cadastre primeiro.")
                continue
            registrar_entrada(lista_frequencia, nome)
            salvartxt(lista_frequencia)

        elif escolha == '2':
            nome = input('Digite o nome do aluno: ')
            if not aluno_existe(nome):
                print(f"Aluno {nome} não está cadastrado! Cadastre primeiro.")
                continue
            registrar_saida(lista_frequencia, nome)
            salvartxt(lista_frequencia)

        elif escolha == '3':
            listar_frequencia(lista_frequencia)

        elif escolha == '0':
            print('Voltando ao menu principal...')
            salvartxt(lista_frequencia)
            break

        else:
            print('Opção inválida. Tente novamente!')


def menu_principal():
    while True:
        print('\n===== MENU PRINCIPAL =====')
        print('1 - Gestão de alunos')
        print('2 - Controle de frequência')
        print('0 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            menu_alunos()
        elif opcao == '2':
            menu_frequencia()
        elif opcao == '0':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida!')


def menu_alunos():
    while True:
        print('\n>>>> Menu de Alunos <<<<')
        print('1. Cadastrar aluno')
        print('2. Listar alunos')
        print('3. Buscar aluno')
        print('4. Remover aluno')
        print('0. Voltar ao menu principal')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_aluno(lista_alunos)
        elif opcao == '2':
            listar_alunos(lista_alunos)
        elif opcao == '3':
            nome = input('Digite o nome do aluno(a): ')
            aluno = buscar_aluno(lista_alunos, nome)
            if aluno:
                print('\nAluno(a) encontrado:')
                print(aluno)
            else:
                print(f'\nAluno {nome} não encontrado.')
        elif opcao == '4':
            nome = input('Digite o nome do aluno(a) a remover: ')
            remover_aluno(lista_alunos, nome)
        elif opcao == '0':
            print('Voltando ao menu principal...')
            break
        else:
            print('Opção inválida. Tente novamente!')

menu_principal()
