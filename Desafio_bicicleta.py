print("DESAFIO BICICLETA".center(40,"-"))
class bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzina(self):
        print("plinplim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada.")

    def correr(self):
        print("vrum.........")

    def __str__(self):
        print("-------------------------------")
        return f"bicicleta: Cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"

    def __str__(self):
        return f"{self. __class__.__name__}:{', '.join([ f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = bicicleta("vermelha", "caloi", 2022, 600)
b2 = bicicleta("verde","monark",2000,1890)
b3 = bicicleta("azul","bmx",2012,1500)

b1.buzina() # chama a função buzinar.
b1.correr() # chama a função correr.
b1.parar()  # chama a função parar.
b2.correr() # chama a função correr.
print(b2.cor, b2.modelo, b2.ano, b2.valor) # printa o objeto bicicleta b2.
print(b1.cor, b1.modelo, b1.ano, b1.valor) # printa o objeto bicicleta b1.
print(b2)
print(b3)
