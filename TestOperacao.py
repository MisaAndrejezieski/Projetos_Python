def calcular(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero não é permitida"

    if operacao == "+":
        return somar
    elif operacao == "-":
        return subtrair
    elif operacao == "*":
        return multiplicar
    elif operacao == "/":
        return dividir

while True:
    a = int(input("Digite o primeiro número (ou -1 para sair): "))
    if a == -1:
        break

    b = int(input("Digite o segundo número: "))
    operacao = input("Digite sua operação (+, -, *, /): ")

    funcao = calcular(operacao)
    resultado = funcao(a, b)

    print("O resultado é: ", resultado)
