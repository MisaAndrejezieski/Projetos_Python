def calcular_total(numeros):
    return sum(numeros)



def retorna_antecessor_e_sucessor(numero):
    print("Estes são o antecessor e sucessor de ",numero)
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor, (10))  # (9, 11)
