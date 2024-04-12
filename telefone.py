import re
print("::: Válidando telefone :::".center(50))
nome_usuario = input("Digite seu nome:")


def validate_numero_telefone(phone_number):
    pattern = r'\(\d{2}\) 9\d{4}-\d{4}'
    if re.match(pattern, phone_number):
        print("Olá,", nome_usuario, "Seu número é: ",phone_number)
        return '::: Número de telefone válido :::'.center(50)
    
    else:
        return '::: Número de telefone inválido :::'.center(50)


# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input("Digite o número do telefone seguindo o modelo '(42) 9xxxx-xxxx':")


# Chama a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazena o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)


# Imprime o resultado:
print(result)