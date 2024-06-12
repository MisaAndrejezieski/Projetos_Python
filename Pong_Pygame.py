import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição de cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Pong')

# Relógio para controlar a taxa de atualização da tela
relogio = pygame.time.Clock()

# Variáveis do jogo
barra_largura = 10
barra_altura = 100
bola_tamanho = 15
barra_velocidade = 5
bola_velocidade_inicial = 5

# Posições iniciais da barra do jogador 1 e jogador 2
barra1_x = 20
barra1_y = altura / 2 - barra_altura / 2
barra2_x = largura - barra_largura - 20
barra2_y = altura / 2 - barra_altura / 2

# Posição inicial da bola
bola_x = largura / 2 - bola_tamanho / 2
bola_y = altura / 2 - bola_tamanho / 2

# Direção inicial da bola
bola_dx = random.choice([-1, 1]) * bola_velocidade_inicial
bola_dy = random.choice([-1, 1]) * bola_velocidade_inicial

# Função para desenhar as barras na tela
def desenhar_barras():
    pygame.draw.rect(tela, branco, [barra1_x, barra1_y, barra_largura, barra_altura])
    pygame.draw.rect(tela, branco, [barra2_x, barra2_y, barra_largura, barra_altura])

# Função para desenhar a bola na tela
def desenhar_bola():
    pygame.draw.rect(tela, branco, [bola_x, bola_y, bola_tamanho, bola_tamanho])

# Função principal do jogo
def jogo():
    global barra1_y, barra2_y, bola_x, bola_y, bola_dx, bola_dy

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Movimentação das barras
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and barra1_y > 0:
            barra1_y -= barra_velocidade
        if teclas[pygame.K_s] and barra1_y < altura - barra_altura:
            barra1_y += barra_velocidade
        if teclas[pygame.K_UP] and barra2_y > 0:
            barra2_y -= barra_velocidade
        if teclas[pygame.K_DOWN] and barra2_y < altura - barra_altura:
            barra2_y += barra_velocidade

        # Movimentação da bola
        bola_x += bola_dx
        bola_y += bola_dy

        # Verificação de colisão com as bordas da tela
        if bola_y <= 0 or bola_y >= altura - bola_tamanho:
            bola_dy *= -1

        # Verificação de colisão com as barras
        if bola_x <= barra1_x + barra_largura and barra1_y <= bola_y <= barra1_y + barra_altura:
            bola_dx *= -1
        elif bola_x >= barra2_x - bola_tamanho and barra2_y <= bola_y <= barra2_y + barra_altura:
            bola_dx *= -1

        # Verificação de pontos
        if bola_x <= 0:
            bola_x = largura / 2 - bola_tamanho / 2
            bola_y = altura / 2 - bola_tamanho / 2
            bola_dx = random.choice([-1, 1]) * bola_velocidade_inicial
            bola_dy = random.choice([-1, 1]) * bola_velocidade_inicial
        elif bola_x >= largura - bola_tamanho:
            bola_x = largura / 2 - bola_tamanho / 2
            bola_y = altura / 2 - bola_tamanho / 2
            bola_dx = random.choice([-1, 1]) * bola_velocidade_inicial
            bola_dy = random.choice([-1, 1]) * bola_velocidade_inicial

        # Atualiza a tela
        tela.fill(preto)
        desenhar_barras()
        desenhar_bola()
        pygame.display.update()

        # Controla a taxa de atualização da tela
        relogio.tick(60)

# Inicia o jogo
jogo()
