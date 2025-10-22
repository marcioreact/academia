import datetime

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
    print(f"O(a) aluno(a) {nome} ainda não entrou. Registre a entrada primeiro.")

def listar(lista_frequencia):
    if not lista_frequencia:
        print('Nenhum registro de frequência.')
    for registro in lista_frequencia:
        print(f'{registro['nome']} - {registro['data']} - Entrada: {registro['entrada']} - Saída: {registro['saida']}')

def salvartxt(lista_frequencia, nome_arquivo='frequencia.txt'):
    with open(nome_arquivo, 'w') as arquivo:
        for registro in lista_frequencia:
            linha = f'{registro['nome']},{registro['data']},{registro['entrada']},{registro['saida']}\n'
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

def limpar_dia(lista_frequencia, nome_arquivo='frequencia.txt'):
    data_atual = datetime.datetime.now().strftime('%d/%m/%Y')
    lista_frequencia[:] = [r for r in lista_frequencia if r['data'] != data_atual]
    salvartxt(lista_frequencia, nome_arquivo)
    print(f"Registros do dia {data_atual} foram removidos.")

def remover_aluno(lista_frequencia, nome, nome_arquivo='frequencia.txt'):
    original_len = len(lista_frequencia)
    lista_frequencia[:] = [r for r in lista_frequencia if r['nome'].lower() != nome.lower()]
    if len(lista_frequencia) < original_len:
        salvartxt(lista_frequencia, nome_arquivo)
        print(f"Todos os registros de {nome} foram removidos.")
    else:
        print(f"Nenhum registro encontrado para {nome}.")

def limpar_historico(lista_frequencia, nome_arquivo='frequencia.txt'):
    confirm = input("Tem certeza que deseja apagar TODO o histórico? (s/n): ").lower()
    if confirm == 's':
        lista_frequencia.clear()
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('')
        print("Histórico apagado com sucesso.")
    else:
        print("Operação cancelada.")

def menu_remover(lista_frequencia):
    while True:
        print('\n--- Menu de Remoção de Histórico ---')
        print('1 - Remover todo o histórico')
        print('2 - Remover registros do dia atual')
        print('3 - Remover registros de um aluno específico')
        print('0 - Voltar ao menu principal')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            limpar_historico(lista_frequencia)
        elif escolha == '2':
            limpar_dia(lista_frequencia)
        elif escolha == '3':
            nome = input('Digite o nome do aluno: ')
            remover_aluno(lista_frequencia, nome)
        elif escolha == '0':
            print('Voltando ao menu principal...')
            break
        else:
            print('Opção inválida. Tente novamente.')

carregar_txt(lista_frequencia)

while True:
    print('\n--- Menu de Controle de Acesso ---')
    print('1 - Registrar entrada')
    print('2 - Registrar saída')
    print('3 - Listar frequência')
    print('4 - Remover registros')
    print('0 - Sair')
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        while True:
            opcao = input('Digite o nome do aluno (ou 0 para voltar): ')
            if opcao == '0':
                print('Voltando ao menu principal...')
                break
            registrar_entrada(lista_frequencia, opcao)
            salvartxt(lista_frequencia)
    elif escolha == '2':
        while True:
            nome = input('Digite o nome do aluno (ou 0 para voltar): ')
            if nome == '0':
                print('Voltando ao menu principal...')
                break
            registrar_saida(lista_frequencia, nome)
            salvartxt(lista_frequencia)
    elif escolha == '3':
        listar(lista_frequencia)
    elif escolha == '4':
        menu_remover(lista_frequencia)
    elif escolha == '0':
        print('Saindo...')
        salvartxt(lista_frequencia)
        break
    else:
        print('Opção inválida, tente outra opção.')