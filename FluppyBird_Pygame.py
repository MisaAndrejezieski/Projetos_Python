import random

import pygame

# Inicialização do Pygame
pygame.init()

# Definição de cores
branco = (255, 255, 255)
azul = (0, 0, 255)

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Flappy Bird')

# Relógio para controlar a taxa de atualização da tela
relogio = pygame.time.Clock()

# Variáveis do jogo
gravidade = 0.5
impulso = -10
velocidade = 0
obstaculo_largura = 70
espaco_obstaculos = 200
distancia_obstaculos = 300
altura_obstaculos = [random.randint(50, 400) for _ in range(5)]
obstaculos_x = [largura + i * distancia_obstaculos for i in range(5)]
pontuacao = 0

# Carregamento de imagens
bird_img = pygame.image.load('bird.png')
bird_img = pygame.transform.scale(bird_img, (50, 50))
obstaculo_img = pygame.image.load('pipe.png')

# Função para desenhar o pássaro na tela
def desenhar_passaro():
    tela.blit(bird_img, (100, altura / 2))

# Função para desenhar os obstáculos na tela
def desenhar_obstaculos():
    for i in range(5):
        tela.blit(obstaculo_img, (obstaculos_x[i], 0 - altura_obstaculos[i]))
        tela.blit(pygame.transform.flip(obstaculo_img, False, True), (obstaculos_x[i], altura_obstaculos[i] + espaco_obstaculos))

# Função principal do jogo
def jogo():
    global velocidade, pontuacao

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    velocidade = impulso

        # Atualiza a posição do pássaro
        velocidade += gravidade
        deslocamento = velocidade
        if 0 <= 100 + deslocamento <= altura - 50:
            desenhar_passaro()
            deslocamento = velocidade
        else:
            pygame.quit()
            quit()

        # Atualiza a posição dos obstáculos
        for i in range(5):
            obstaculos_x[i] -= 5
            if obstaculos_x[i] < -obstaculo_largura:
                obstaculos_x[i] = largura
                altura_obstaculos[i] = random.randint(50, 400)
                pontuacao += 1

        # Verifica colisão com os obstáculos
        for i in range(5):
            if 100 + 50 > obstaculos_x[i] and 100 < obstaculos_x[i] + obstaculo_largura:
                if 100 < altura_obstaculos[i] or 100 + 50 > altura_obstaculos[i] + espaco_obstaculos:
                    pygame.quit()
                    quit()

        # Desenha os obstáculos na tela
        tela.fill(branco)
        desenhar_obstaculos()
        pygame.display.update()

        # Controla a taxa de atualização da tela
        relogio.tick(30)

# Inicia o jogo
jogo()
