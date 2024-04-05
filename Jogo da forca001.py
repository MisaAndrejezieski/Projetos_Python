# Jogo da Forca em Python feito por A.I.

# Escolha da palavra secreta pelo usuario
palavra_secreta = input("Digite a palavra secreta: ").lower()

# Inicializacao das variáveis
letras_adivinhadas = []
chances_restantes = 25
ganhou = False

# Loop principal do jogo
while True:
    # Exibir a palavra com as letras adivinhadas
    palavra_mostrada = ""
    for letra in palavra_secreta:
        if letra in letras_adivinhadas:
            palavra_mostrada += letra
        else:
            palavra_mostrada += "_ "
    print(f"Palavra: {palavra_mostrada}")

    # Adivinhar uma letra
    letra_adivinhada = input("Digite uma letra: ").lower()

    # Verificar se a letra esta na palavra
    if letra_adivinhada in palavra_secreta:
        letras_adivinhadas.append(letra_adivinhada)
    else:
        chances_restantes -= 1
        print(f"Letra não encontrada! Chances restantes: {chances_restantes}")

    # Verificar se o usuario ganhou ou perdeu
    if palavra_mostrada == palavra_secreta:
        ganhou = True
        break
    elif chances_restantes == 0:
        break

# Exibir mensagem de resultado
if ganhou:
    print(f"Parabéns, você ganhou! A palavra era: {palavra_secreta}")
else:
    print(f"Você perdeu! A palavra era: {palavra_secreta}")
