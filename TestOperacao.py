def calcular(operacao):
    def somar(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    if operacao == "+":
        return somar
    else:
        return subtracao

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
operacao = input("Digite sua operação: ")

funcao = calcular(operacao)
resultado = funcao(a, b)

print("O resultado é: ", resultado)
