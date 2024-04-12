import re


 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
    pattern = r'\(\d{2}\) 9\d{4}-\d{4}'
    if re.match(pattern, phone_number):
        print(phone_number)
        return 'Número de telefone válido.'
    
    else:
        return 'Número de telefone inválido.'


# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()


# Chama a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazena o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

  # TODO: Agora crie um return, para retornar que o número de telefone é válido:
       
       # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.

# Imprime o resultado:
print(result)