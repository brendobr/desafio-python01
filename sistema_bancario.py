menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
limite_saque_diario = 1500
saque_diario = 1500

# Aqui uma função para exibir e armazenar todas as movimentações feitas no extrato
def exibir_extrato():
    print("Extrato".center(10, "-"))
    for movimentacao in extrato:
         print(movimentacao)
    print("---------------")
    print(f"Saldo atual: R${saldo:.2f}")
    print("---------------\n")
while True:

    opcao = input(menu)
# Logica de decisão para Depósito
    if opcao == "d":
        valor_deposito = float(input("Valor do Depósito: "))
        if valor_deposito == 0:
                break
        saldo += valor_deposito
        extrato.append(f"Depósito no valor de R${valor_deposito:.2f}.\n")
        print(f"Depósito R$:{saldo:.2f}")
# Logica de decisão simples para Saque     
    elif opcao == "s":
        resposta = """
        Deseja sacar ?
        [1] Sim
        [2] Não
        """
        opcao2 = input(resposta)
        if opcao2 == "1" and numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o Valor do saque:"))
            if saldo < valor_saque:
                 print(f"Sem saldo suficiente para saque, seu saldo é de R${saldo:.2f}")
                       
            elif valor_saque <= limite:
                numero_saques += 1 
                saldo -= valor_saque
                extrato.append(f"Saque no valor de R${valor_saque:.2f}\n")
                print(f"Você sacou R${valor_saque:.2f}, seu saldo atual é R$:{saldo:.2f}")
                
                if valor_saque > saque_diario:
                    saque_diario -= valor_saque
                    print(f"Seu limite de aque diario é de R${limite_saque_diario:.2f},podendo sacar mais f{saque_diario:.2f}, para aumentar contate seu gerente.")
            

        elif opcao2 == "1" and numero_saques >= LIMITE_SAQUES:
            print(f"Saque limite de R${limite_saque_diario:.2f} atingido, contate seu gerente para mais informações")   

        elif opcao2 == "2":
            break
        else:
            print("Operação Inválida, por favor selecione a operação desejada")

# Aqui chamamos a função "exibir_extrato" para verificarmos todas as transações feitas na conta 
    elif opcao == "e":
      exibir_extrato()
    
    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione a operação desejada")