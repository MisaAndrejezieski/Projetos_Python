def obter_palavra_escolhida():
    return input("Digite uma palavra para o jogo da forca: ").lower()

def obter_jogador_adivinhador():
    return input("Digite o nome do jogador que vai adivinhar a palavra: ")

def obter_jogadores():
    num_jogadores = int(input("Quantos jogadores vão participar? "))
    jogadores = []
    for i in range(num_jogadores):
        nome_jogador = input(f"Digite o nome do jogador {i + 1}: ")
        jogadores.append(nome_jogador)
    return jogadores

def jogo_da_forca():
    jogadores = obter_jogadores()
    palavra_escolhida = obter_palavra_escolhida()
    letras_palavra = set(palavra_escolhida)
    letras_ocultas = ["_" for _ in palavra_escolhida]
    max_tentativas = 6
    tentativas = 0
    
    while tentativas < max_tentativas:
        print("\n" + " ".join(letras_ocultas))
        letra_adivinhada = input(f"{jogadores[1]} (jogador que adivinha), digite uma letra: ").lower()
        
        if letra_adivinhada in letras_palavra:
            for i, letra in enumerate(palavra_escolhida):
                if letra == letra_adivinhada:
                    letras_ocultas[i] = letra
        else:
            tentativas += 1
            print(f"Letra '{letra_adivinhada}' não está na palavra. Tentativas restantes: {max_tentativas - tentativas}")
        
        if "_" not in letras_ocultas:
            print(f"Parabéns, {jogadores[1]}! Você ganhou! A palavra era: {palavra_escolhida}")
            break
    
    # Se o usuário que adivinhou usou mais que o triplo de letras da palavra, o primeiro jogador ganha
    if tentativas >= 3 * len(letras_palavra):
        print(f"{jogadores[0]} (jogador que escolheu a palavra) ganha! A palavra era: {palavra_escolhida}")
    else:
        print(f"{jogadores[1]} (jogador que adivinhou) ganha! A palavra era: {palavra_escolhida}")

# Inicia o jogo
jogo_da_forca()
