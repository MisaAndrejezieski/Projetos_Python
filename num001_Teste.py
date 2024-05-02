print(":: PROGRAMA DE MOSTRAR NÚMERO PARES E IMPARES ::")

# Lista original de números pares elevados ao quadrado se maior que 2, ou o próprio número se 2 ou menos
numeros_pares = [n**2 if n > 2 else n for n in range(10) if n % 2 == 0]

# Criando uma lista para armazenar os números ímpares
numeros_impares = [n for n in range(10) if n % 2 != 0]

print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
