menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    print()
    banco = "_Seu Banco_"
    print(banco.center(40, "="))

    opcao = input(menu)

    if opcao == "d":
        valor = float(input(">> Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"* Depósito: R$ {valor:.2f}\n"

        else:
            print(">> Não foi possível executar sua solicitação! \nO valor informado é inválido.\n")

    elif opcao == "s":
        valor = float(input(">> Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(">> Não foi possível executar sua solicitação! \nVocê não tem saldo suficiente.\n")

        elif excedeu_limite:
            print(">> Não foi possível executar sua solicitação! \nO valor do saque excede o limite.\n")

        elif excedeu_saques:
            print(">> Não foi possível executar sua solicitação! \nNúmero máximo de saques excedido.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"* Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print(">> Não foi possível executar sua solicitação! \nO valor informado é inválido.\n")

    elif opcao == "e":
        servico = "_Seu Banco - Extrato_"
        print(servico.center(40, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================")

    elif opcao == "q":
        break

    else:
        print("* Operação inválida, por favor selecione novamente a operação desejada.\n")
