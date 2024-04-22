def calcular(operacao):
    def somar(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    if operacao == "+":
        return somar
    else:
        return subtracao

while True:
    a = int(input("Digite o primeiro número (ou -1 para sair): "))
    if a == -1:
        break

    b = int(input("Digite o segundo número: "))
    operacao = input("Digite sua operação: ")

    funcao = calcular(operacao)
    resultado = funcao(a, b)

    print("O resultado é: ", resultado)
