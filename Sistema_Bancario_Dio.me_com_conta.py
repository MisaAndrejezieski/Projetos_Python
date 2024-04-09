class ContaBancaria:
    def __init__(self, nome, numero_conta,):
        self.nome = nome
        self.numero_conta = numero_conta[:4]
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def menu(self):
        return f"""
        SISTEMA BANCÁRIO DESAFIO PYTHON DIO.ME

        Nome: {self.nome}
        Número da Conta: {self.numero_conta,("##")}

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair

    => """

    def iniciar(self):
        while True:
            opcao = input(self.menu())

            if opcao == "1":
                self.depositar()

            elif opcao == "2":
                self.sacar()

            elif opcao == "3":
                self.imprimir_extrato()

            elif opcao == "0":
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

        print("É sempre um prazer ter você como cliente.")

    def depositar(self):
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
            print("Para fazer depósito obrigatoriamente tem que ser um valor positivo.")

    def sacar(self):
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    def imprimir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


# Para usar a classe ContaBancaria
conta = ContaBancaria("misael".title(), "123456",)
conta.iniciar()
