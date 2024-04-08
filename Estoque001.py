def menu():
    print("\n---Menu---")
    print("1. Cadastrar produto")
    print("2. Retirar produto")
    print("3. Verificar estoque")
    print("4. Sair")
    return int(input("Escolha uma opção: "))

def cadastrar_produto(estoque):
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    estoque[produto] = estoque.get(produto, 0) + quantidade
    print(f"{quantidade} unidades de {produto} foram adicionadas ao estoque.")

def retirar_produto(estoque):
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    if estoque.get(produto, 0) >= quantidade:
        estoque[produto] -= quantidade
        print(f"{quantidade} unidades de {produto} foram retiradas do estoque.")
    else:
        print("Produto não disponível em quantidade suficiente.")

def verificar_estoque(estoque):
    print("\nEstoque atual:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade}")

def main():
    estoque = {}
    while True:
        opcao = menu()
        if opcao == 1:
            cadastrar_produto(estoque)
        elif opcao == 2:
            retirar_produto(estoque)
        elif opcao == 3:
            verificar_estoque(estoque)
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
