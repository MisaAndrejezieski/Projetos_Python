import time
from decimal import Decimal

class Usuario:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = Decimal('0')
        self.limite = Decimal('500')
        self.extrato = ""
        self.quantidade_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo += valor_deposito
            self.extrato += f"{time.strftime('%d/%m/%y %X')}  |    Depósito   |  R$ {valor_deposito:.2f}\n"
            print(f"Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor_saque):
        if 0 < valor_saque <= self.saldo and valor_saque <= self.limite and self.quantidade_saques < self.LIMITE_SAQUES:
            self.saldo -= valor_saque
            self.extrato += f"{time.strftime('%d/%m/%y %X')}  |    Saque      | (R$ {valor_saque:.2f})\n"
            self.quantidade_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! Verifique seu limite de saque ou quantidade de saques.")

    def exibir_extrato(self):
        data_hora = time.localtime()
        data = time.strftime('%d/%m/%y',data_hora)
        hora = time.strftime('%H:%M:%S',data_hora)
        extrato_formatado = f"Não há registro de movimentações.\n" if not self.extrato else self.extrato
        saldo_formatado = f"\nSaldo em {data} {hora}:           R$ {self.saldo:.2f}"
        print("\n===================== EXTRATO =====================")
        print("\n===================================================")
        print("Data/Hora          |   Operação    |    Valor")
        print("===================================================")
        print(extrato_formatado)
        print(saldo_formatado)
        print("======================= FIM =======================")

usuarios = []
contas = []

def menu_principal():
    print("""
          ===================== BANK0K =====================
                            MENU PRINCIPAL

    [1] Cadastrar novo usuário
    [2] Cadastrar nova conta
    [3] Acessar conta
    [4] Listar usuários
    [5] Listar contas

    [0] Sair
    """)
    return input("Digite a opção desejada e tecle [Enter]: ")

def menu_conta():
    print("""
          ===================== BANK0K =====================
                            MENU DE CONTA
    [1] Depositar
    [2] Sacar
    [3] Extrato

    [0] Voltar
    """)
    return input("Digite a opção desejada e tecle [Enter]: ")

def criar_usuario():
    cpf = input("\nInforme o CPF (somente números): ")
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("\nCPF vinculado a um usuário existente.")
            return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")
    usuarios.append(Usuario(cpf, nome, data_nascimento, endereco))
    print("Usuário criado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF(somente números): ")
    for usuario in usuarios:
        if usuario.cpf == cpf:
            agencia = "0001"
            numero_conta = len(contas) + 1
            conta = Conta(agencia, numero_conta, usuario)
            contas.append(conta)
            usuario.contas.append(conta)
            print(f"\nConta: {numero_conta} \nAgencia: {agencia} \nConta criada com sucesso!!!")
            return
    print("Usuário não encontrado. Use um CPF cadastrado.")

def acessar_conta():
    cpf = input("Informe o CPF(somente números): ")
    for usuario in usuarios:
        if usuario.cpf == cpf:
            if len(usuario.contas) > 0:
                print("\nContas disponíveis:")
                for i, conta in enumerate(usuario.contas):
                    print(f"[{i+1}] Conta: {conta.numero_conta} Agencia: {conta.agencia}")
                opcao_conta = int(input("Selecione o numero da conta que deseja acessar: ")) - 1
                if opcao_conta >= 0 and opcao_conta < len(usuario.contas):
                    conta = usuario.contas[opcao_conta]
                    while True:
                        opcao = menu_conta()
                        if opcao == "1":
                            valor_deposito = Decimal(input("Informe o valor do depósito: R$ "))
                            conta.depositar(valor_deposito)
                        elif opcao == "2":
                            valor_saque = Decimal(input("Informe o valor do saque: R$ "))
                            conta.sacar(valor_saque)
                        elif opcao == "3":
                            conta.exibir_extrato()
                        elif opcao == "0":
                            break
                        else:
                            print("Operação inválida, por favor selecione uma opção disponível.")
                else:
                    print("Opção inválida.")
            else:
                print("Nenhuma conta encontrada para este usuário.")
            return
    print("Usuário não encontrado. Use um CPF cadastrado.")

def listar_usuarios():
    if len(usuarios) > 0:
        print("\nUsuários cadastrados:")
        for i, usuario in enumerate(usuarios):
            print(f"\n===================== {usuario.nome} =====================")
            print(f"[{i+1}] Nome: {usuario.nome} CPF: {usuario.cpf}")
            print(f"Data de Nascimento: {usuario.data_nascimento}")
            print(f"Endereço: {usuario.endereco}")
            if usuario.contas:
                print("Detalhes da Conta:")
                for conta in usuario.contas:
                    print(f"Conta: {conta.numero_conta} Agencia: {conta.agencia}")
            print("\n======================= LISTAR USUÁRIOS =======================")        

    else:
        print("Nenhum usuário cadastrado.")

def listar_contas():
    if len(contas) > 0:
        print("\n======================= LISTAR CONTAS =======================")
        print("\nContas cadastradas:")
        for i, conta in enumerate(contas):
            print(f"[{i+1}] Conta: {conta.numero_conta} Agencia: {conta.agencia} Titular: {conta.usuario.nome}")
    else:
        print("Nenhuma conta cadastrada.")

def main():
    while True:
        opcao = menu_principal()
        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            acessar_conta()
        elif opcao == "4":
            listar_usuarios()
        elif opcao == "5":
            listar_contas()
        elif opcao == "0":
            print("Obrigado por usar nossos Serviços!")
            break
        else:
            print("Operação inválida, por favor selecione uma opção disponível.")

if __name__ == "__main__":
    main()
