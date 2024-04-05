class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, nome, quantidade):
        if nome not in self.produtos:
            self.produtos[nome] = Produto(nome, quantidade)
        else:
            self.produtos[nome].quantidade += quantidade

    def retirar_produto(self, nome, quantidade):
        if nome in self.produtos and self.produtos[nome].quantidade >= quantidade:
            self.produtos[nome].quantidade -= quantidade
        else:
            print("Produto não disponível em quantidade suficiente")

    def mostrar_estoque(self):
        for produto in self.produtos.values():
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}")

estoque = Estoque()
estoque.cadastrar_produto("Produto1", 10)
estoque.cadastrar_produto("Produto2", 5)
estoque.retirar_produto("Produto1", 3)
estoque.mostrar_estoque()
