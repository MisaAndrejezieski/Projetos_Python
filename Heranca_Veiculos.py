class Veiculos:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self. __class__.__name__}:{', '.join([ f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculos):
    pass

class Carro(Veiculos):
    pass

class Caminhao(Veiculos):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__{cor, placa, numero_rodas}
        self.carregado = carregado

    
    def esta_carregado(self):
        print( f"{'Sim' if self.carregado else 'Não'} Estou carregado.")

# moto = Motocicleta('preta', 'abc1234',2)
# moto.ligar_motor()
# print(moto)
Caminhao = Caminhao("roxo", "dfg-7894", 6, False)
print(Caminhao)
Caminhao.esta_carregado()
