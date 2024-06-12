import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição de cores
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Relógio para controlar a taxa de atualização da tela
relogio = pygame.time.Clock()

# Fonte para o placar
fonte = pygame.font.SysFont(None, 30)

# Função para desenhar a cobrinha na tela
def desenhar_cobrinha(cobrinha):
    for posicao in cobrinha:
        pygame.draw.rect(tela, verde, [posicao[0], posicao[1], 10, 10])

# Função para desenhar a borda na tela
def desenhar_borda():
    pygame.draw.rect(tela, branco, [0, 0, largura, 10])  # Topo
    pygame.draw.rect(tela, branco, [0, 0, 10, altura])   # Esquerda
    pygame.draw.rect(tela, branco, [largura-10, 0, 10, altura])  # Direita
    pygame.draw.rect(tela, branco, [0, altura-10, largura, 10])   # Baixo

# Função principal do jogo
def jogo():
    cobrinha = [[largura / 2, altura / 2]]
    comprimento = 1
    direcao = 'direita'
    pontuacao = 0

    comida_x = round(random.randrange(20, largura - 30) / 10.0) * 10
    comida_y = round(random.randrange(20, altura - 30) / 10.0) * 10

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    direcao = 'esquerda'
                elif evento.key == pygame.K_RIGHT:
                    direcao = 'direita'
                elif evento.key == pygame.K_UP:
                    direcao = 'cima'
                elif evento.key == pygame.K_DOWN:
                    direcao = 'baixo'

        if direcao == 'esquerda':
            cobrinha[0][0] -= 10
        elif direcao == 'direita':
            cobrinha[0][0] += 10
        elif direcao == 'cima':
            cobrinha[0][1] -= 10
        elif direcao == 'baixo':
            cobrinha[0][1] += 10

        # Verifica se a cabeça da cobrinha colidiu com a borda ou com o próprio corpo
        if cobrinha[0][0] <= 10 or cobrinha[0][0] >= largura - 20 or cobrinha[0][1] <= 10 or cobrinha[0][1] >= altura - 20:
            pygame.quit()
            quit()

        # Verifica se a cabeça da cobrinha colidiu com a comida
        if cobrinha[0][0] == comida_x and cobrinha[0][1] == comida_y:
            comprimento += 1
            pontuacao += 10
            comida_x = round(random.randrange(20, largura - 30) / 10.0) * 10
            comida_y = round(random.randrange(20, altura - 30) / 10.0) * 10

        # Atualiza a tela
        tela.fill(branco)
        desenhar_borda()
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, 10, 10])
        desenhar_cobrinha(cobrinha)
        placar_texto = fonte.render("Pontuação: " + str(pontuacao), True, verde)
        tela.blit(placar_texto, [10, 10])
        pygame.display.update()

        # Controla a taxa de atualização da tela
        relogio.tick(15)

# Inicia o jogo
jogo()
