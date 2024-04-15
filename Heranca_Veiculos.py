class Veiculos:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculos):
    pass

class Carro(Veiculos):
    pass

class Caminhao(Veiculos):
    pass

moto = Motocicleta("vermelha", "123", 2)
print(moto)

