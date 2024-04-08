print("Um if aninhado é apenas um if dentro de outro if.")

numeros = [int(input("Digite um número: ")) for _ in range(3)]
nomes = ['x', 'y', 'z']

maior_numero = max(numeros)
menor_numero = min(numeros)
numero_do_meio = sum(numeros) - maior_numero - menor_numero

print(f"{nomes[numeros.index(maior_numero)]} é o maior número: {maior_numero}")
print(f"{nomes[numeros.index(menor_numero)]} é o menor número: {menor_numero}")
print(f"{nomes[numeros.index(numero_do_meio)]} é o número do meio: {numero_do_meio}")
