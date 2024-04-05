estoque = {}

while True:
    print("\n---Menu---")
    print("1. Cadastrar produto")
    print("2. Retirar produto")
    print("3. Verificar estoque")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade
        print(f"{quantidade} unidades de {produto} foram adicionadas ao estoque.")

    elif opcao == 2:
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
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

    else:
        print("Opção inválida. Tente novamente.")
