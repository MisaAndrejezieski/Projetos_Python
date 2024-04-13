class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzina(self):
        print("plinplim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada.")

    def correr(self):
        print("vrum.........")    


b1 = bicicleta("vermelha", "caloi", 2022, 600)

b1.buzina()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = bicicleta("verde","monark",2000,1890)
bicicleta.buzina(b2)
b2.correr()
print(b2.cor, b2.modelo, b2.ano, b2.valor)
