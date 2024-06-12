import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *

# Inicialização do Pygame
pygame.init()
largura, altura = 800, 600
pygame.display.set_mode((largura, altura), DOUBLEBUF|OPENGL)

# Configuração da câmera
gluPerspective(45, (largura/altura), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Função para desenhar um cubo
def desenhar_cubo():
    glBegin(GL_QUADS)
    glColor3fv((1, 0, 0))  # Vermelho
    glVertex3fv((-1, 1, -1))
    glVertex3fv((-1, -1, -1))
    glVertex3fv((1, -1, -1))
    glVertex3fv((1, 1, -1))
    
    glColor3fv((0, 1, 0))  # Verde
    glVertex3fv((-1, 1, 1))
    glVertex3fv((-1, -1, 1))
    glVertex3fv((1, -1, 1))
    glVertex3fv((1, 1, 1))
    
    glColor3fv((0, 0, 1))  # Azul
    glVertex3fv((1, 1, -1))
    glVertex3fv((1, -1, -1))
    glVertex3fv((1, -1, 1))
    glVertex3fv((1, 1, 1))
    
    glColor3fv((1, 1, 0))  # Amarelo
    glVertex3fv((-1, 1, -1))
    glVertex3fv((-1, -1, -1))
    glVertex3fv((-1, -1, 1))
    glVertex3fv((-1, 1, 1))
    
    glColor3fv((1, 0, 1))  # Magenta
    glVertex3fv((-1, 1, 1))
    glVertex3fv((-1, 1, -1))
    glVertex3fv((1, 1, -1))
    glVertex3fv((1, 1, 1))
    
    glColor3fv((0, 1, 1))  # Ciano
    glVertex3fv((-1, -1, 1))
    glVertex3fv((-1, -1, -1))
    glVertex3fv((1, -1, -1))
    glVertex3fv((1, -1, 1))
    glEnd()

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    # Limpa a tela e o buffer de profundidade
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    # Desenha um cubo
    desenhar_cubo()
    
    # Atualiza a tela
    pygame.display.flip()
    pygame.time.wait(10)
