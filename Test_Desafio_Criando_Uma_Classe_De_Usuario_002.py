class UsuarioTelefone:
    def __init__(self, nome, telefone, plano):
        self.__nome = nome
        self.__telefone = telefone
        self.__plano = plano

    def criar_usuario(self):
        # Aqui você pode adicionar lógica adicional se necessário
        return f'Usuário {self.__nome} criado com sucesso.'

    # Métodos getters e setters para encapsulamento
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_plano(self):
        return self.__plano

    def set_plano(self, plano):
        self.__plano = plano

    # Método especial `__str__` atualizado para trabalhar com atributos privados
    def __str__(self):
        return f"Usuário {self.get_nome()} criado com sucesso."

# Entrada:
nome = input("Digite o nome do usuário: ")  
numero = input("Digite o número de telefone: ")  
plano = input("Digite o plano: ")  

# Criação de um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)

# Saída:
print(usuario)
