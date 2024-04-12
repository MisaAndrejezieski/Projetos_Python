# Cria uma lista vazia para armazenar os equipamentos
equipamentos = []

# Solicita ao usuário para inserir três equipamentos
for i in range(3):
    equipamento = input("Por favor, insira o nome do equipamento: ")
    equipamentos.append(equipamento)

# Exibe a lista de equipamentos
print("\nLista de Equipamentos:")
for equipamento in equipamentos:
    print("- " + equipamento)