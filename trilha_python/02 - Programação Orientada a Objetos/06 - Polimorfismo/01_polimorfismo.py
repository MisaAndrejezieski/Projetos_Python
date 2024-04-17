# Polimorfismo:

class Passaro:
    def voar(self):
        print("Voando...")


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


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(galinha())
plano_voo(Aviao())
print(Passaro)