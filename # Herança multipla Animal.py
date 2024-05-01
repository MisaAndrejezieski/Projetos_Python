# Herança multipla Animal
class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f"{self. __class__.__name__}:{', '.join([ f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
     

class Mamifero(Animal):
    def __init__(self, cor_pelo, **Kw):
        self.cor_pelo = cor_pelo
        super(). __init__(**Kw)


class Ave(Animal):
    def __init__(self, cor_bico, **Kw):
        self.cor_bico = cor_bico
        super(). __init__(**Kw)




 
class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrico(Mamifero, Ave):
    pass

gato = Gato(cor_pelo="preto", num_patas=4)
print(gato)
ornitorrinco = Ornitorrico(cor_pelo="cinza_escuro", cor_bico="cinza_claro", num_patas=4)
print(ornitorrinco)
leao = Leao("cinza", 4)
print(leao)
