pagamentos = []  # armazenar todos os pagamentos


# registrar pagamentos
def registrar_pagamento(pagamentos):
    nome = input('Nome do aluno: ')
    valor = float(input('Valor da mensalidade (R$): '))
    data = input('Data do pagamento (dd/mm/aaaa): ')


    pagamento = {
        'nome': nome,
        'valor': valor,
        'data': data
    }


    pagamentos.append(pagamento)
    print('Pagamento registrado com sucesso!')
pagamentos =[]

# listar todos os pagamentos
def listar_pagamentos():
    if not pagamentos:
        print('Ainda não há pagamentos registrados.')
        return

    print('Lista de pagamentos')
    for p in pagamentos:
        print(f"Aluno: {p['nome']} | Valor: R$ {p['valor']:.2f} | Data: {p['data']}")
    print('----------------------\n')


# ver total arrecadado
def ver_saldo():
    if not pagamentos:
        print('Não há pagamentos registrados.')
        return

    total = sum(p["valor"] for p in pagamentos)
    print(f" Total arrecadado: R$ {total:.2f}")


# relatório financeiro simples
def relatorio_financeiro():
    if not pagamentos:
        print("Nenhum pagamento registrado.")
        return

    print("RELATÓRIO FINANCEIRO ")
    total = 0
    for p in pagamentos:
        print(f"Aluno: {p['nome']:<20} Valor: R$ {p['valor']:<8.2f} Data: {p['data']}")
        total += p['valor']
    print("--------------------------------")
    print(f"TOTAL GERAL: R$ {total:.2f}")


# menu
def menu_financeiro():
    while True:
        print("MENU FINANCEIRO")
        print("1 - Registrar pagamento")
        print("2 - Listar pagamentos")
        print("3 - Ver total arrecadado")
        print("4 - Gerar relatório financeiro")
        print("0 - Voltar ao inicio")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_pagamento(pagamentos)
        elif opcao == "2":
            listar_pagamentos()
        elif opcao == "3":
            ver_saldo()
        elif opcao == "4":
            relatorio_financeiro()
        elif opcao == "0":
            print("Voltando ao inicio.")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_financeiro()
