class Veiculos:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculos):
    print("moto")
    pass

class Carro(Veiculos):
    pass

class Caminhao(Veiculos):
    pass

moto = Motocicleta("vermelha","ABC-1234",2)
moto.ligar_motor()
print(moto)
