x = [1,2,3] # cria uma lista mutável.
y = x       # a variavel y recebe x.
y[1] = 4    # coloca o valor 4 na posição 1, como começa no 0 troca 2 por 4.
print(x)    # retorna [1,4,3].

###############################################################################

numbers = (1,2,3,4,5) # criação de uma tupla, tupla são imutaveis. 
numbers [0] = 10      # tenta trocar na posição 0 o número 1 por 10.
print(numbers)        # como tuplas são imutáveis retorna ERRO.

###############################################################################

nums = [1,2,3]        # cria uma lista
nums.insert(4,3)      # Em seguida, a função insert(4, 3) é chamada. Isso significa que o valor 3 será inserido na posição 4 da lista (lembrando que as posições em Python começam em 0).
print(nums)           # retorna  [1,2,3,3]


