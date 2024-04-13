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
    def __str__(self):
        print("-------------------------------")
        return f"bicicleta: Cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"


#b1 = bicicleta("vermelha", "caloi", 2022, 600)

#b1.buzina()
#b1.correr()
#b1.parar()
#print(b1.cor, b1.modelo, b1.ano, b1.valor)

#b2 = bicicleta("verde","monark",2000,1890)
b3 = bicicleta("azul","bmx",2012,1500)
#bicicleta.buzina(b2)
#b2.correr()
#print(b2.cor, b2.modelo, b2.ano, b2.valor)

print(b3)
