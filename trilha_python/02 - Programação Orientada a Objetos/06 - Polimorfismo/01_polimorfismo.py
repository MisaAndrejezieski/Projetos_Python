# Polimorfismo:

class Passaro:
    def voar(self, asa):
        self.asa = asa
        print("Voando...")
    
        def __init__(self, asa):
            self.asa = asa

        def __str__(self):
            return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

class galinha(Passaro):
    def voar(self):
        print("Voô de galinha.")

# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj): # Defini o objeto, onde obj é filho de pássaro e defini o voar para cada classe.
    obj.voar()


passaro = Passaro()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(galinha())
plano_voo(Aviao())
print(passaro()) # depois eu resolvo. 17/04/2024