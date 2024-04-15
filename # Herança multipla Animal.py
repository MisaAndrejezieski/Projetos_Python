# Herança multipla Animal
class Animal:
    pass

class Mamifero(Animal):
    pass

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Onitorico(Animal, Mamifero):
    pass


