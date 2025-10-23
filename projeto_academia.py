import json

def menu():
 try:

    while True:
        print('\n===== SISTEMA ACADEMIA =====')
        print('1 - Gestão de Alunos')
        print('2 - Gestão Financeira')
        print('3 - Controle de Acesso')
        print('4 - Agendamento e Treinos')
        print('0 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            gestao_alunos()
        elif opcao == '2':
            gestao_financeira()
        elif opcao == '3':
            controle_acesso()
        elif opcao == '4':
            agendamento_treinos()
        elif opcao == '0':
            print('Encerrando o sistema')
            break
        else:
            print('Opção inválida! Tente novamente.')

 except KeyboardInterrupt:
    print('\n Interrupção detectada. Programa encerrado')

def gestao_alunos():
    print('bloco de gestao')

def gestao_financeira():
    print('bloco financeiro')

def controle_acesso():
    print('bloco de acesso')

def agendamento_treinos():
    
    def calcular_imc(peso, altura):
        return peso / (altura ** 2)

    def classificar_imc(imc):
        if imc < 18.5:
            return 'Abaixo do peso'
        elif 18.5 <= imc < 25:
            return 'Peso normal'
        elif 25 <= imc < 30:
            return 'Sobrepeso'
        elif 30 <= imc < 35:
            return 'Obesidade grau 1'
        elif 35 <= imc < 40:
            return 'Obesidade grau 2'
        else:
            return 'Obesidade grau 3'

    def sugerir_modalidades(classificacao):
        sugestoes = {
            'Abaixo do peso': ['Treino de força leve', 'Pilates', 'Yoga'],
            'Peso normal': ['Musculação', 'Funcional', 'HIIT moderado'],
            'Sobrepeso': ['Caminhada rápida', 'Spinning', 'Circuito funcional leve'],
            'Obesidade grau 1': ['Hidroginástica', 'Caminhada', 'Treino supervisionado leve'],
            'Obesidade grau 2': ['Hidroginástica', 'Caminhada', 'Treino supervisionado leve'],
            'Obesidade grau 3': ['Hidroginástica', 'Caminhada', 'Treino supervisionado leve']
        }
        return sugestoes.get(classificacao, [])

    while True:
        print('\n=== Agendamento e Treinos ===')
        
        nome = input('Digite seu nome: ')
        altura = float(input('Digite sua altura (em metros): '))
        peso = float(input('Digite seu peso (em kg): '))

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        modalidades = sugerir_modalidades(classificacao)

        print(f'\n {nome}, seu IMC é: {imc:.2f} ({classificacao})')
        print('\n Modalidades de treino recomendadas para você:')
        for i, treino in enumerate(modalidades, 1):
            print(f'   {i}. {treino}')

        ficha = {'Nome': nome, 'IMC': round(imc, 2), 'Classificação': classificacao, 'Modalidades': modalidades}

        with open('arquivo.txt', 'a') as arquivo:
            arquivo.write(json.dumps(ficha) + '\n')

        continuar = input('\n Deseja cadastrar outro usuário? (s/n): ')
        if continuar != 's':
            print('Encerrando o programa')
            break


if __name__ == "__main__":
    menu()
