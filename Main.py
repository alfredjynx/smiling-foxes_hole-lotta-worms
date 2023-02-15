import pygame
import numpy as np
from classes.Header import Header

pygame.init()
pygame.font.init()

# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

BLACK = (0, 0, 0, 0.2)
COR_PERSONAGEM = (30, 200, 20)
N = 1000
# Inicializar posicoes
s0 = np.array([50,200])
v0 = np.array([10, -10])
# a = np.array([0, 0.2])
v = [v0 for i in range(N)]
s = [s0 for i in range(N)]
corpo = np.array([100,100])
corpo2 = np.array([300,300])
# corpo = np.array([200,200])
# v = v0
# s = s0

# Personagem
personagem = pygame.Surface((5, 5))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem


header = Header(screen)

rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("mouse down")
                header.atualiza_estado()

    for i in range(N):
        if s[i][0]<10 or s[i][0]>390 or s[i][1]<10 or s[i][1]>390: # Se eu chegar ao limite da tela, reinicio a posição do personagem
            rndm = np.random.randn(2)
            mous_pos = pygame.mouse.get_pos()
            v1 = mous_pos-s0
            norm = np.linalg.norm(v1)
            s[i], v[i] = s0, v1/norm*10+rndm*4

    # Controlar frame rate
    clock.tick(FPS)

    # Processar posicoes
    for i in range(N):
        C = 350
        y = corpo - s[i]
        d = np.linalg.norm(y)
        direcao_a = y /d

        mag_a = C / d**2
        a = direcao_a * mag_a

        y2 = corpo2 - s[i]
        d2 = np.linalg.norm(y2)
        direcao_a2 = y2/d2

        mag_a2 = C/d2**2
        a2 = direcao_a2 * mag_a2

        v[i] = v[i] + a*5 + a2*15 
        # v[i] = v[i] + a*10
        s[i] = s[i] + 0.1 * v[i]

    # v = v + a
    # s = s + 0.1 * v

    # Desenhar fundo
    screen.fill(BLACK)

    # Desenhar personagem
    for i in range(N):
        rect = pygame.Rect(s[i], (10, 10))  # First tuple is position, second is size.
        screen.blit(personagem, rect)

    # Desenhar header
    header.desenha()

    pygame.draw.circle(screen,"BLUE",corpo,15,0)
    pygame.draw.circle(screen,"RED",corpo2,15,0)

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()