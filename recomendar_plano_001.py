def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
        print("Plano de 50Mbps por $50,00, nesta promação.")
    elif consumo <= 50:
        return "Plano Prata Fibra - 100Mbps"
        print("Plano de 100Mbps por $100,00, nesta promação.")
    else:
        
        print("Plano de 300Mbps por $200,00, nesta promação.")
        return "Plano Premium Fibra - 300Mbps"


try:
    # Solicita ao usuário que insira o consumo médio mensal de dados:
    print("Digite seu consumo médio por mês: ")
    consumo = float(input())
    # Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
    print(recomendar_plano(consumo))
except ValueError as e:
    print(f"Error: {e}")

print('Continuo processando')