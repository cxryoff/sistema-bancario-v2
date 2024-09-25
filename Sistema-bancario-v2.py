def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Saldo insuficiente.")
    elif excedeu_limite:
        print("O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Número máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========= EXTRATO =========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("============================")

def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [c] Cadastrar usuário
    [cc] Cadastrar conta corrente
    [lc] Listar contas

    => """
    return input(menu)

def criar_usuario():
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário (YYYY-MM-DD): ")
    cpf = input("Informe o CPF do usuário: ")
    endereco = input("Informe o endereço do usuário: ")
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário criado com sucesso!")

def criar_conta_corrente():
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    if usuario is None:
        print("Erro: Usuário não encontrado.")
        return
    conta = {
        'agencia': '0001',
        'numero_conta': len(contas) + 1,
        'usuario': usuario
    }
    contas.append(conta)
    print("Conta corrente criada com sucesso!")

def listar_contas():
    print("Contas:")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    global usuarios, contas  # Declarar como global
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        elif opcao == "c":
            criar_usuario()

        elif opcao == "cc":
            criar_conta_corrente()

        elif opcao == "lc":
            listar_contas()

        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")

main()
