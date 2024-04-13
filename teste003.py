import re

def validate_numero_telefone(phone_number):
    pattern = r'\(\d{2}\) 9\d{4}-\d{4}'
    if re.match(pattern, phone_number):
        return 'Número de telefone válido.'
    else:
        return 'Número de telefone inválido.'

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input("Por favor, insira um número de telefone: ")  

# Chama a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazena o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)
