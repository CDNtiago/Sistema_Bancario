import re # A biblioteca re é uma biblioteca padrão do Python que fornece suporte para expressões regulares. 

# Definição do menu principal
menu_principal = """
Seja bem vindo!
 Selecione o que deseja:
[1] Cadastro
[2] Login
[q] Sair

=> """

# Definição do menu de operações bancárias
menu_operacoes = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Dicionário para armazenar os clientes, onde as chaves são os CPFs e os valores são dicionários contendo informações do cliente
clientes = {}

# Definição do limite de saques
LIMITE_SAQUES = 3

#fução para validar email
def validar_email(email):
    # Expressão regular para validar um endereço de e-mail
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Verificar se o e-mail corresponde ao padrão
    if re.match(padrao_email, email):
        return True
    else:
        return False


# Função para cadastrar um novo cliente
def cadastrar_cliente():
    while True:
        nome = input("Informe seu nome: ")
        if nome.replace(" ", "").isalpha() and len(nome) <= 50:
            break
        else:
            print("O nome deve ser composto apenas por letras, sem números, e ter no máximo 50 caracteres.")

    while True:
        cpf = input("Informe seu CPF (apenas números): ")
        if cpf.isdigit() and len(cpf) == 11:
            break
        else:
            print("O CPF deve ser composto apenas por números e ter exatamente 11 dígitos.")

    while True:
        endereco = input("Informe seu endereço (apenas letras e números, sem pontuações): ")
        if endereco.replace(" ", "").isalnum() and len(endereco) <= 100:
            break
        else:
            print("O endereço deve ser composto apenas por letras e números, sem pontuações, e ter no máximo 100 caracteres.")


    while True:
        email = input("Informe seu email: ")
        if validar_email(email):
            break
        else:
            print("O email informado não é válido.")
       

    while True:
        senha = input("Crie uma senha com exatamente 4 dígitos numéricos: ")
        if senha.isdigit() and len(senha) == 4:
            break
        else:
            print("A senha deve ser composta apenas por números inteiros e ter exatamente 4 caracteres.")

    clientes[cpf] = {'nome': nome, 'endereco': endereco, 'email': email, 'senha': senha, 'saldo': 0, 'limite': 500, 'extrato': "", 'numero_saques': 0}



# Função para realizar o login de um cliente
def login():
    cpf = input("Informe seu CPF: ")
    senha = input("Informe sua senha: ")  # Solicitar a senha durante o login
    if cpf in clientes and clientes[cpf]['senha'] == senha:  # Verificar se a senha corresponde à senha armazenada
        cliente = clientes[cpf]
        print(f"Bem-vindo, {cliente['nome']}!")
        return cliente
    else:
        print("CPF ou senha incorretos.")
        return None

# Loop principal do programa
while True:
    # Exibe o menu principal e aguarda a escolha do usuário
    opcao_principal = input(menu_principal)

    # Opção para cadastrar um novo cliente
    if opcao_principal == "1":
        cadastrar_cliente()

    # Opção para realizar login
    elif opcao_principal == "2":
        cliente = login()
        if cliente:
            while True:
                # Exibe o menu de operações bancárias e aguarda a escolha do usuário
                opcao_operacoes = input(menu_operacoes)

                # Opção para realizar depósito
                if opcao_operacoes == "d":
                    valor = float(input("Informe o valor do depósito: "))

                    if valor > 0:
                        # Atualiza o saldo do cliente e registra a transação no extrato
                        cliente['saldo'] += valor
                        cliente['extrato'] += f"Depósito: R$ {valor:.2f}\n"
                    else:
                        print("Operação falhou! O valor informado é inválido.")

                # Opção para realizar saque
                elif opcao_operacoes == "s":
                    valor = float(input("Informe o valor do saque: "))

                    excedeu_saldo = valor > cliente['saldo']
                    excedeu_limite = valor > cliente['limite']
                    excedeu_saques = cliente['numero_saques'] >= LIMITE_SAQUES

                    if excedeu_saldo:
                        print("Operação falhou! Você não tem saldo suficiente.")
                    elif excedeu_limite:
                        print("Operação falhou! O valor do saque excede o limite.")
                    elif excedeu_saques:
                        print("Operação falhou! Número máximo de saques excedido.")
                    elif valor > 0:
                        # Atualiza o saldo do cliente, registra a transação no extrato e atualiza o número de saques
                        cliente['saldo'] -= valor
                        cliente['extrato'] += f"Saque: R$ {valor:.2f}\n"
                        cliente['numero_saques'] += 1
                    else:
                        print("Operação falhou! O valor informado é inválido.")

                # Opção para exibir o extrato
                elif opcao_operacoes == "e":
                    print("\n================ EXTRATO ================")
                    print(f"Extrato do usuário: {cliente['nome']}")
                    print("\nNão foram realizadas movimentações." if not cliente['extrato'] else cliente['extrato'])
                    print(f"\nSaldo: R$ {cliente['saldo']:.2f}")
                    print("==========================================")

                # Opção para sair do menu de operações bancárias
                elif opcao_operacoes == "q":
                    break

                else:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")

    # Opção para sair do programa
    elif opcao_principal == "q":
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
