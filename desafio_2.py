import textwrap

def menu():
    menu = '''
    ========== MENU ==========
    
    [d]\tDEPOSITAR
    [s]\tSACAR
    [e]\tEXTRATO
    [nc]\tNOVA CONTA
    [lc]\tLISTAR CONTAS
    [nu]\tNOVO USUÁRIO
    [q]\tSAIR 
    
    ==========================
    '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"=== DEPÓSITO: R$ {valor} ===\n"
        print("Depósito realizado com sucesso")
    else:
        print("@@@ Operação inválida. Insira valor positivo. @@@")
    return saldo, extrato
    
def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    if valor > saldo:
        print("\n@@@ Operação inválida. Você não possui saldo suficiente. @@@")
    elif numero_saques >= limite_saques:
        print("\n@@@ Você excedeu o limite de saques de hoje. Tente novamente amanhã. @@@")
    elif valor > limite:
        print("\n@@@ O valor inserido para saque ultrapasse o valor permitido por saque. Insira um valor menor e tente novamente. @@@")
    elif valor > 0:
        numero_saques += 1
        saldo -= valor
        extrato += f'=== SAQUE: R$ {valor} ==='
        print("Saque realizado com sucesso!")
    else:
        print("\n@@@ Operação falhou. Tente novamente mais tarde. @@@")
    return saldo, extrato
    
def visualizar_extrato(saldo,/,*, extrato):
    print('EXTRATO'.center(20, "="))
    print(extrato if extrato else extrato)
    print(f'SALDO = {saldo}')

def criar_usuario(usuarios):
    cpf = int(input("Digite seu cpf. Apenas números: "))
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Operação inválida. Você já possui cadastro no banco. Volte e acesse sua conta.")
        return
    else:
        nome = input("Insira seu nome: ")
        data_nascimento = input("Insira sua data de nascimento (dd-mm-aaaa): ")
        endereco  = input("Insira seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuário criado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado. Fluxo de criação de conta encerrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f'''
        Agência: \t{conta['agencia']}
        C/C: \t\t{conta['numero_conta']}
        Titular: \t {conta['usuario']['nome']}
        '''
        print("=", *100)
        print(textwrap.dedent(linha))
     
def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    LIMITE = 500
    
    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        
        opcao = menu()
        
        if opcao == 'd':
            valor = int(input("Insira o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == 's':
            valor = int(input("Insira o valor que deseja sacar: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor,extrato=extrato,limite=LIMITE, numero_saques=numero_saques, limite_saques=LIMITE_SAQUE)
            
        elif opcao == 'e':
            visualizar_extrato(saldo, extrato=extrato)
            
        elif opcao == 'nu':
            criar_usuario(usuarios)
            
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            
        elif opcao == 'lc':
            listar_contas(contas)      
                    
        elif opcao == 'q':
            break
        
        else:
            print("Insira uma opção válida")
        
main()