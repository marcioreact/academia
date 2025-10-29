# academia
Sistema de gerenciamento de academias

Sistema Academia

Funcionalidades principais
Gestão de alunos: Cadastro de informações, acompanhamento do histórico de pagamentos e planos, e controle de frequência. 

Gestão financeira: Controle de mensalidades, emissão de boletos e cobranças recorrentes, acompanhamento de fluxo de caixa e relatórios financeiros. 
Controle de acesso: Gestão da entrada e saída de alunos, muitas vezes com integração com catracas e leitores biométricos. 

Agendamento: Organização de horários, controle de reservas de aulas e envio de lembretes automáticos. 

Prescrição e acompanhamento de treinos: Cadastro de treinos personalizados, envio para o aluno (via WhatsApp, e-mail ou aplicativo) e registro do progresso, como carga, tempo e percepção de esforço. 

Comunicação e marketing: Envio de notificações automáticas, e-mails e mensagens para os clientes, ajudando na fidelização e em campanhas de divulgação. 

Relatórios e análises: Geração de relatórios para acompanhar o desempenho financeiro, operacional e de alunos, auxiliando na tomada de decisões estratégicas. 






🏋️‍♂️ Projeto: Sistema Academia (versão para iniciantes)
👩‍💻 Linguagem: Python (básico)

Uso de listas, dicionários e funções simples.

Nada de classes, banco de dados ou bibliotecas externas (para deixar acessível).

Interface: apenas terminal (console).

🔹 Parte 1 — Gestão de Alunos (Pessoa 1)

Responsável: Cadastro e controle dos alunos.

Funções sugeridas:

cadastrar_aluno(lista_alunos)

Recebe nome, idade, plano e contato.

Armazena em um dicionário e adiciona à lista de alunos.

listar_alunos(lista_alunos)

Mostra todos os alunos cadastrados.

buscar_aluno(lista_alunos, nome)

Retorna informações do aluno (caso exista).

remover_aluno(lista_alunos, nome)

Remove o aluno do sistema.

📋 Estrutura sugerida de cada aluno:

{
    "nome": "Maria Silva",
    "idade": 25,
    "plano": "Mensal",
    "contato": "1199999-9999"
}

🔹 Parte 2 — Gestão Financeira (Pessoa 2)

Responsável: Controle de mensalidades, pagamentos e relatórios simples.

Funções sugeridas:

registrar_pagamento(lista_pagamentos, nome, valor)

Registra um pagamento feito por um aluno.

listar_pagamentos(lista_pagamentos)

Mostra todos os pagamentos e alunos.

ver_saldo(lista_pagamentos)

Mostra o total arrecadado (soma dos valores).

relatorio_financeiro(lista_pagamentos)

Exibe um relatório simples de receitas.

📋 Estrutura sugerida de pagamento:

{
    "nome": "Maria Silva",
    "valor": 120.00,
    "data": "21/10/2025"
}

🔹 Parte 3 — Controle de Acesso e Frequência (Pessoa 3)

Responsável: Registrar entradas e saídas de alunos na academia.

Funções sugeridas:

registrar_entrada(lista_frequencia, nome)

Registra a hora de entrada de um aluno.

registrar_saida(lista_frequencia, nome)

Registra a hora de saída.

listar_frequencia(lista_frequencia)

Mostra histórico de presença.

📋 Estrutura sugerida de frequência:

{
    "nome": "Maria Silva",
    "data": "21/10/2025",
    "entrada": "08:30",
    "saida": "09:45"
}

🔹 Parte 4 — Agendamento e Treinos (Pessoa 4)

Responsável: Organizar horários e prescrever treinos simples.

Funções sugeridas:

agendar_aula(lista_agendamentos, nome, atividade, data, hora)

Registra uma aula para o aluno.

listar_agendamentos(lista_agendamentos)

Mostra todos os agendamentos.

registrar_treino(lista_treinos, nome, treino)

Guarda o treino prescrito.

mostrar_treino(lista_treinos, nome)

Exibe o treino do aluno.

📋 Estrutura sugerida:

# Agendamento
{
    "nome": "Maria Silva",
    "atividade": "Musculação",
    "data": "22/10/2025",
    "hora": "10:00"
}

# Treino
{
    "nome": "Maria Silva",
    "treino": ["Supino reto - 3x10", "Agachamento - 3x12", "Abdominal - 3x20"]
}

🔸 Integração Final (opcional para o grupo)

Depois que cada parte estiver funcionando, vocês podem criar um menu principal:

def menu():
    print("===== SISTEMA ACADEMIA =====")
    print("1 - Gestão de Alunos")
    print("2 - Gestão Financeira")
    print("3 - Controle de Acesso")
    print("4 - Agendamento e Treinos")
    print("0 - Sair")


Cada opção chamará as funções do respectivo módulo.
