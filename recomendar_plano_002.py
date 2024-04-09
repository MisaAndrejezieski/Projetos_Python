plano = "plano de internet"
def recomendar_plano(nome, consumo):
    if consumo <= 10:
        print(f"{nome}, recomendamos o Plano de 50Mbps por $50,00, nesta promoção.")
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 50:
        print(f"{nome}, recomendamos o Plano de 100Mbps por $100,00, nesta promoção.")
        return "Plano Prata Fibra - 100Mbps"
    else:
        print(f"{nome}, recomendamos o Plano de 300Mbps por $200,00, nesta promoção.")
        return "Plano Premium Fibra - 300Mbps"

try:
    # Solicita ao usuário que insira o nome:
    print("Digite seu nome: ")
    nome = input()
    # Solicita ao usuário que insira o consumo médio mensal de dados:
    print("Digite seu consumo médio por mês: ")
    consumo = float(input())
    # Chama a função recomendar_plano com o nome e o consumo inseridos e imprime o plano recomendado:

    print(".".join(plano.upper))
    print(recomendar_plano(nome.title().center(20,"_"), consumo))
except ValueError as e:
    print(f"Error: {e}")

print('Continuo processando')
