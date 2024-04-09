class Banco:
    def __init__(self):
        self.usuarios = {}
        self.contas = {}
        self.extratos = {}

    def gerar_numero_conta(self):
        while True:
            numero_conta = str(random.randint(100000, 999999))
            if numero_conta not in self.contas:
                return numero_conta

    def criar_conta(self):
        """
        Função para criar uma nova conta.
        """
        nome = input("Digite o nome do usuário: ")
        senha = input("Digite a senha desejada: ")
        # Hash da senha para segurança
        senha_hashed = hashlib.sha256(senha.encode()).hexdigest()

        numero_conta = self.gerar_numero_conta()
        self.contas[numero_conta] = {'nome': nome, 'senha': senha_hashed, 'saldo': 500, 'tipo': 'corrente'}

        print("Conta criada com sucesso!")
        print("Seu número de conta é:", numero_conta)
