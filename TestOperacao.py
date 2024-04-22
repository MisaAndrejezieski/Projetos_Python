def calcular(operacao):
    def somar(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b
    
    def divisao(a, b):
        return a / b
    
    match operacao:
        case "+":
            return somar
        case "-":
            return subtracao
        case "*":
            return multiplicacao
        case "/":
            return divisao
        

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
operacao = input("Digite sua operação: ")

funcao = calcular(operacao)
resultado = funcao(a, b)

print("O resultado é: ", resultado)
