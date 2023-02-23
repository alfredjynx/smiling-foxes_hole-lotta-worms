import pygame
import numpy as np
from classes.Planetas import Planeta

pygame.init()

# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

BLACK = (0, 0, 0, 0.2)
COR_PERSONAGEM = (30, 200, 20)
# Inicializar posicoes
s0 = np.array([200,500])
v0 = np.array([10, -10])
# a = np.array([0, 0.2])
v = list()
s = list()
c = 350
pos1 = np.array([200,200])
corpo = Planeta(pos1,c)
pos2 = np.array([600,300])
corpo2 = Planeta(pos2,c)
# corpo = np.array([200,200])
# v = v0
# s = s0
n = len(v)
# Personagem
personagem = pygame.Surface((5, 5))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem

rodando = True
mouse_click = False
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True

    mous_pos = pygame.mouse.get_pos()
    # rndm = np.random.randn(2)*0.2
    rndm = np.array([1,1])
    v1 = mous_pos-s0
    norm = np.linalg.norm(v1)

    if mouse_click:
        v.append((v1/norm*10+rndm))
        s.append(s0)
        mouse_click = False
        n = len(v)

    em_jogo = list()

    for i in range(n):
        valor = True
        if s[i][0]<10 or s[i][0]>790 or s[i][1]<10 or s[i][1]>590: # Se eu chegar ao limite da tela, reinicio a posição do personagem
            # s[i], v[i] = s0, v1/norm*10+rndm
            valor = False
        em_jogo.append(valor)

    if n>0:
        v_novo = list()
        s_novo = list()
        cont = 0
        for value in em_jogo:
            if value:
                v_novo.append(v[cont])
                s_novo.append(s[cont])
            cont+=1
        v = v_novo
        s = s_novo
        n = len(v)
    # Controlar frame rate
    clock.tick(FPS)

    # Processar posicoes
    for i in range(n):
        v[i] = v[i] + corpo.calcula_a(s[i])*0 + corpo2.calcula_a(s[i])*50
        s[i] = s[i] + 0.1 * v[i]


    # Desenhar fundo
    screen.fill(BLACK)

    # Desenhar personagem
    for i in range(n):
        rect = pygame.Rect(s[i], (10, 10))  # First tuple is position, second is size.
        screen.blit(personagem, rect)

    pygame.draw.circle(screen,"BLUE",corpo.get_pos(),15,0)
    pygame.draw.circle(screen,"RED",corpo2.get_pos(),15,0)

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()