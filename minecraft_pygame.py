import sys

import pygame

# Inicialização do Pygame
pygame.init()

# Definição de cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)

# Configurações da tela
largura = 800
altura = 600
tamanho_bloco = 40
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Minecraft Simples')

# Relógio para controlar a taxa de atualização da tela
relogio = pygame.time.Clock()

# Função para desenhar o mundo
def desenhar_mundo(mundo):
    for linha in range(len(mundo)):
        for coluna in range(len(mundo[linha])):
            cor = branco if mundo[linha][coluna] == 0 else verde
            pygame.draw.rect(tela, cor, (coluna * tamanho_bloco, linha * tamanho_bloco, tamanho_bloco, tamanho_bloco))

# Função principal do jogo
def jogo():
    # Definição do mundo
    mundo = [[0] * (largura // tamanho_bloco) for _ in range(altura // tamanho_bloco)]

    # Posição inicial do personagem
    personagem_x = 0
    personagem_y = 0

    # Variável para controlar se está colocando ou removendo blocos
    colocando_bloco = True

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mudança entre colocar e remover blocos
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    colocando_bloco = not colocando_bloco

            # Movimento do personagem
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                coluna = posicao_mouse[0] // tamanho_bloco
                linha = posicao_mouse[1] // tamanho_bloco
                if colocando_bloco:
                    mundo[linha][coluna] = 1
                else:
                    mundo[linha][coluna] = 0

        # Desenha o mundo na tela
        tela.fill(preto)
        desenhar_mundo(mundo)
        pygame.draw.rect(tela, (255, 0, 0), (personagem_x, personagem_y, tamanho_bloco, tamanho_bloco))  # Personagem
        pygame.display.update()

        # Controla a taxa de atualização da tela
        relogio.tick(60)

# Inicia o jogo
jogo()
