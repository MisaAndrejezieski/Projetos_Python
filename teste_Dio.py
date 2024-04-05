import json
import os

def carregar_estoque():
    if os.path.exists('estoque.json'):
        with open('estoque.json', 'r') as f:
            return json.load(f)
    else:
        return {}

def salvar_estoque(estoque):
    with open('estoque.json', 'w') as f:
        json.dump(estoque, f)

estoque = carregar_estoque()

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

        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade

        print(f"{quantidade} unidades de {produto} foram adicionadas ao estoque.")

    elif opcao == 2:
        produto = input("Nome do produto: ")
        quantidade = input("Quantidade: ")

        if not quantidade.isdigit() or int(quantidade) < 0:
            print("Quantidade inválida. Tente novamente.")
            continue

        quantidade = int(quantidade)

        if produto in estoque and quantidade <= estoque[produto]:
            estoque[produto] -= quantidade
            print(f"{quantidade} unidades de {produto} foram retiradas do estoque.")
        else:
            print("Produto não disponível em quantidade suficiente.")

    elif opcao == 3:
        print("\nEstoque atual:")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade}")

    elif opcao == 4:
        break

    salvar_estoque(estoque)
