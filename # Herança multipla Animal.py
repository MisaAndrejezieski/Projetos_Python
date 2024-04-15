# Herança multipla Animal
class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f"{self. __class__.__name__}:{', '.join([ f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    

class Mamifero(Animal):
    def __init__(self, num_patas, cor_pelo):
        self.num_patas = num_patas
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, num_patas, cor_bico):
        self.num_patas = num_patas
        self.cor_bico = cor_bico
        

    

    
class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorico(Ave, Mamifero):
    pass

gato = Gato(4, "preto")
print(gato)
ornitorinco = Ornitorico(12, "vermelho")
print(ornitorinco)
