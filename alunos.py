lista_alunos = []

def cadastrar_aluno(lista):
    nome = input('Insira o nome do aluno: ')

    while True:
        try:
            idade = int(input('Insira a idade do aluno: '))
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

    print(f'\nAluno {nome} cadastrado com sucesso! Seja bem vindo!\n')

def listar_alunos(lista):
    if not lista:
        print('\nNenhum aluno cadastrado.\n')
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

def menu():
    while True:
        print('\n>>>> Menu Inicial <<<<')
        print('1. Cadastrar aluno')
        print('2. Listar alunos')
        print('3. Buscar aluno')
        print('4. Remover aluno')
        print('5. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_aluno(lista_alunos)
        elif opcao == '2':
            listar_alunos(lista_alunos)
        elif opcao == '3':
            nome = input('Digite o nome do aluno a buscar: ')
            aluno = buscar_aluno(lista_alunos, nome)
            if aluno:
                print('\nAluno encontrado:')
                print(aluno)
            else:
                print(f'\nAluno {nome} não encontrado.')
        elif opcao == '4':
            nome = input('Digite o nome do aluno a remover: ')
            remover_aluno(lista_alunos, nome)
        elif opcao == '5':
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida. Tente novamente!')


menu()

        