# Herança multipla Animal
class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

class Mamifero(Animal):
    def __init__(self, num_patas)
        super().__init__(num_patas)

class Ave(Animal):
    def __init__(self, num_patas):
        self.num_patas = num_patas
        super().__init__(num_patas)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Onitorico(Ave, Mamifero):
    pass


