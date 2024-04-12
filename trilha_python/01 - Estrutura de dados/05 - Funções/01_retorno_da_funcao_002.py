def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def antsec():
    num = int(input("Digite o número: "))  # Passando valor para num
    ant = num - 1
    sec = num + 1
    print("O antecessor de ",num," é ",ant,"\ne o sucessor de ",num," é ",sec)

print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

antsec()
