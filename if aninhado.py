print("if aninhado é só um if dentro de outro if.")

x = int(input("Digite um número: ")) 
y = int(input("Digite um número: ")) 
z = int(input("Digite um número: ")) 

maior_numero = max(x, y, z)
menor_numero = min(x, y, z)

if maior_numero == x:
    print("x é o maior número.")
elif maior_numero == y:
    print("y é o maior número.")
else:
    print("z é o maior número.")

if menor_numero == x:
    print("x é o menor número.")
elif menor_numero == y:
    print("y é o menor número.")
else:
    print("z é o menor número.")
if ((x > y) and (z > x)) or ((x > z) and (y > x)):
    print("x é o número do meio.")
if ((y > x) and (z > y)) or ((y > z ) and (x > y)):
    print("y é o número do meio.")
if ((z > x) and (y > z)) or ((z > y) and (x > z)):
    print("y é o número do meio.")    
