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

# Exemplo de uso:
usuario1 = UsuarioTelefone('Ana', '(11) 91111-1111', 'Plano Essencial Fibra')
print(usuario1.criar_usuario())

usuario2 = UsuarioTelefone('Sofia', '(22) 92222-2222', 'Plano Prata Fibra')
print(usuario2.criar_usuario())

usuario3 = UsuarioTelefone('Pedro', '(33) 93333-3333', 'Plano Premium Fibra')
print(usuario3.criar_usuario())
