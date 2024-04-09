# Cria uma Lista 'itens' para armazenar os equipamentos:
itens = []

print("Digite sua lista de equipamentos:")

# Cria um loop para solicitar os itens ao usuário:
for _ in range(3):
    # Solicita o item e armazena na variável "item":
    item = input()
    
    # Adiciona o item à lista "itens":
    itens.append(item)


# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
