import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Definição de cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Labirinto')

# Relógio para controlar a taxa de atualização da tela
relogio = pygame.time.Clock()

# Tamanho do labirinto
tamanho_celula = 40
numero_linhas = altura // tamanho_celula
numero_colunas = largura // tamanho_celula

# Função para gerar um labirinto usando o algoritmo de Prim
def gerar_labirinto():
    labirinto = [[1 for _ in range(numero_colunas)] for _ in range(numero_linhas)]

    # Define a posição inicial e final do labirinto
    labirinto[1][1] = 0
    labirinto[numero_linhas - 2][numero_colunas - 2] = 0

    # Lista de células para visitar
    visitados = [(2, 2)]

    while visitados:
        celula_atual = visitados[-1]
        vizinhos = []

        # Verifica os vizinhos da célula atual
        for direcao in [(0, -2), (0, 2), (-2, 0), (2, 0)]:
            proxima_celula = (celula_atual[0] + direcao[0], celula_atual[1] + direcao[1])
            if 0 < proxima_celula[0] < numero_linhas - 1 and 0 < proxima_celula[1] < numero_colunas - 1 and labirinto[proxima_celula[0]][proxima_celula[1]] == 1:
                vizinhos.append(proxima_celula)

        if vizinhos:
            proxima_celula = random.choice(vizinhos)
            parede_x = (proxima_celula[1] + celula_atual[1]) // 2
            parede_y = (proxima_celula[0] + celula_atual[0]) // 2
            labirinto[parede_y][parede_x] = 0
            labirinto[proxima_celula[0]][proxima_celula[1]] = 0
            visitados.append(proxima_celula)
        else:
            visitados.pop()

    return labirinto

# Função para desenhar o labirinto na tela
def desenhar_labirinto(labirinto):
    for linha in range(numero_linhas):
        for coluna in range(numero_colunas):
            if labirinto[linha][coluna] == 1:
                pygame.draw.rect(tela, preto, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
            elif labirinto[linha][coluna] == 0:
                pygame.draw.rect(tela, branco, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# Função principal do jogo
def jogo():
    labirinto = gerar_labirinto()

    # Posição inicial do personagem
    personagem_x = tamanho_celula
    personagem_y = tamanho_celula

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Movimento do personagem
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    if personagem_y > 0 and labirinto[personagem_y // tamanho_celula - 1][personagem_x // tamanho_celula] == 0:
                        personagem_y -= tamanho_celula
                elif evento.key == pygame.K_DOWN:
                    if personagem_y < altura - tamanho_celula and labirinto[personagem_y // tamanho_celula + 1][personagem_x // tamanho_celula] == 0:
                        personagem_y += tamanho_celula
                elif evento.key == pygame.K_LEFT:
                    if personagem_x > 0 and labirinto[personagem_y // tamanho_celula][personagem_x // tamanho_celula - 1] == 0:
                        personagem_x -= tamanho_celula
                elif evento.key == pygame.K_RIGHT:
                    if personagem_x < largura - tamanho_celula and labirinto[personagem_y // tamanho_celula][personagem_x // tamanho_celula + 1] == 0:
                        personagem_x += tamanho_celula

        # Desenha o labirinto e o personagem na tela
        tela.fill(preto)
        desenhar_labirinto(labirinto)
        pygame.draw.rect(tela, verde, (personagem_x, personagem_y, tamanho_celula, tamanho_celula))
        pygame.display.flip()

        # Controla a taxa de atualização da tela
        relogio.tick(60)

# Inicia o jogo
jogo()
