x = [1,2,3] # cria uma lista mutável.
y = x       # a variavel y recebe x.
y[1] = 4    # coloca o valor 4 na posição 1, como começa no 0 troca 2 por 4.
print(x)    # retorna [1,4,3].

###############################################################################

numbers = (1,2,3,4,5) # criação de uma tupla, tupla são imutaveis. 
#numbers [0] = 10      # tenta trocar na posição 0 o número 1 por 10.
print(numbers)        # como tuplas são imutáveis retorna ERRO.

###############################################################################

nums = [1,2,3]        # cria uma lista
nums.insert(4,3)      # Em seguida, a função insert(4, 3) é chamada. Isso significa que o valor 3 será inserido na posição 4 da lista (lembrando que         as posições em Python começam em 0).
print(nums)           # Como a lista original tem apenas 3 elementos, o Python adiciona o valor 3 na última posição disponível, retorna  [1,2,3,3]

###############################################################################

list_x = [1,2,3,4,5]     
result = list_x.pop()
print(result)                   # Inicialmente, temos a lista list_x com os elementos [1, 2, 3, 4, 5].
                                # Em seguida, a função pop() é chamada sem argumentos. Isso remove o último elemento da lista e retorna esse elemento.
                                # O último elemento da lista original é 5, portanto, o valor retornado pela função pop() é 5.
                                # A lista list_x agora contém os elementos [1, 2, 3, 4], pois o 5 foi removido.

################################################################################

text = "hello world"
expr = ('d', 'rld')
result = text.endswith(expr)
print(result)                   # Inicialmente, temos a string text com o valor "hello world".
                                # A função endswith(expr) verifica se a string text termina com o sufixo especificado em expr.
                                # O valor de expr é ('d', 'rld'). Isso significa que estamos verificando se a string text termina com a sequência de caracteres 'd' seguida por 'rld'.
                                # Como a string text termina com a sequência 'rld', o resultado da função endswith(expr) é True.

################################################################################

text = "hello world"
result = text.swapcase()
print(result)                   # Inicialmente, temos a string text com o valor "hello world".
                                # A função swapcase() é chamada na string text. Essa função inverte as letras maiúsculas para minúsculas e vice-versa.
                                # Portanto, a string resultante após a aplicação de swapcase() é HELLO WORLD.

################################################################################
text = "Hello world"
res = '-'.join(text.split())
print(res)                      # Inicialmente, temos a string text com o valor "Hello world".
                                # A função split() é chamada na string text. Isso divide a string em palavras, criando uma lista de palavras: ["Hello", "world"].
                                # Em seguida, a função join() é aplicada à lista de palavras, usando o caractere '-' como separador. Isso combina as palavras da lista com o separador, resultando na string "Hello-world".

################################################################################
dict_x = {"name": "Prakash", "age": 23}
dict_y = {"name": "joy"}
dict_y.update(dict_x)
print(dict_y)                    # retorna {'name', 'prakash', 'age':23}

################################################################################




################################################################################