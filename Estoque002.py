import json
import os

print("==================================================")
print("Estoque do MISA")
print("==================================================")


class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self, arquivo='estoque.json'):
        self.arquivo = arquivo
        if os.path.exists(arquivo):
            with open(arquivo, 'r') as f:
                self.produtos = json.load(f)
        else:
            self.produtos = {}

    def adicionar(self, produto, quantidade):
        if produto in self.produtos:
            self.produtos[produto] += quantidade
        else:
            self.produtos[produto] = quantidade

    def remover(self, produto, quantidade):
        if produto in self.produtos and quantidade <= self.produtos[produto]:
            self.produtos[produto] -= quantidade
            if self.produtos[produto] == 0:
                del self.produtos[produto]
        else:
            raise ValueError("Produto não disponível em quantidade suficiente.")

    def verificar(self):
        return self.produtos

    def salvar(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.produtos, f)

def main():
    estoque = Estoque()

    while True:
        print("\nMenu:")
        print("1. Cadastrar produto")
        print("2. Retirar produto")
        print("3. Verificar estoque")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if not opcao.isdigit() or int(opcao) < 1 or int(opcao) > 4:
            print("Opção inválida. Tente novamente.")
            continue

        opcao = int(opcao)

        if opcao == 1:
            produto = input("Nome do produto: ")
            quantidade = input("Quantidade: ")

            if not quantidade.isdigit() or int(quantidade) < 0:
                print("Quantidade inválida. Tente novamente.")
                continue

            quantidade = int(quantidade)

            estoque.adicionar(produto, quantidade)
            print(f"{quantidade} unidades de {produto} foram adicionadas ao estoque.")

        elif opcao == 2:
            produto = input("Nome do produto: ")
            quantidade = input("Quantidade: ")

            if not quantidade.isdigit() or int(quantidade) < 0:
                print("Quantidade inválida. Tente novamente.")
                continue

            quantidade = int(quantidade)

            try:
                estoque.remover(produto, quantidade)
                print(f"{quantidade} unidades de {produto} foram retiradas do estoque.")
            except ValueError as e:
                print(e)

        elif opcao == 3:
            produtos = estoque.verificar()
            print("\nEstoque atual:")
            for produto, quantidade in produtos.items():
                print(f"{produto}: {quantidade}")

        elif opcao == 4:
            break

        estoque.salvar()

if __name__ == "__main__":
    main()
