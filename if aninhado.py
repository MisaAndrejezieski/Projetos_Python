x = int(input("Digite um número: ")) 
y = int(input("Digite um número: ")) 
z = int(input("Digite um número: ")) 

maior_numero = max(x, y, z)
menor_numero = min(x, y, z)
medio_numero = med(x, y, z)

if maior_numero == x:
    print("x é o maior número.")
elif maior_numero == y:
    print("y é o maior número.")
else:
    print("z é o maior número.")

if menor_numero == x:
    print("x é o menor número.")
elif maior_numero == y:
    print("y é o menor número.")
else:
    print("z é o maior número.")
