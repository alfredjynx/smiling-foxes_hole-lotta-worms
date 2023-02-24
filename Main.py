import os
import pygame
import numpy as np
from classes.Planetas import Planeta
from classes.Ret import Ret
from classes.Header import Header

pygame.init()

# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

BLACK = (0, 0, 0, 0.2)
COR_PERSONAGEM = (30, 200, 20)

header = Header(screen)

# Inicializar posicoes
s0 = np.array([200,500])
v0 = np.array([10, -10])
# a = np.array([0, 0.2])
v = list()
s = list()
# c = 350
# pos1 = np.array([200,200])
# corpo = Planeta(pos1,c)
# pos2 = np.array([600,300])
# corpo2 = Planeta(pos2,c)

# Inicializar fases
fases = [
    {"fase":1,'corpo':[Planeta(np.array([200,200]),350),Planeta(np.array([600,300]),350)],"v":v,"s":s,"goal":Ret((350,350),(50,50)),"obst":Ret((250,250),(50,50))},
    {"fase":2,'corpo':[Planeta(np.array([200,200]),350),Planeta(np.array([600,300]),350)],"v":v,"s":s,"goal":Ret((550,450),(50,50)),"obst":Ret((250,250),(50,50))},
    {"fase":3,'corpo':[Planeta(np.array([200,200]),350),Planeta(np.array([600,300]),350)],"v":v,"s":s,"goal":Ret((500,250),(50,50)),"obst":Ret((250,250),(50,50))}
]

n = len(v)
# Personagem
personagem = pygame.Surface((5, 5))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem

f = 0

# coisas da pagina inicial:
# Set up the title text
title_font = pygame.font.SysFont(None, 64)
title_text = title_font.render("Smiling Foxes", True, (255, 255, 255))
title_text_rect = title_text.get_rect()
title_text_rect.center = (800 // 2, 600 // 3)

# Set up the play button
play_button_font = pygame.font.SysFont(None, 32)
play_button_text = play_button_font.render("Jogar", True, (255, 255, 255))
play_button_text_rect = play_button_text.get_rect()
play_button_text_rect.center = (800 // 2, 600 // 2)

# Set up the quit button
quit_button_font = pygame.font.SysFont(None, 32)
quit_button_text = quit_button_font.render("Quit", True, (255, 255, 255))
quit_button_text_rect = quit_button_text.get_rect()
quit_button_text_rect.center = (800 // 2, 600 // 1.5)

background_image = pygame.image.load("./sprites/buraco.png")


pagina_atual = "inicio"

rodando = True
mouse_click = False
while rodando:

    corpo = fases[f]['corpo']
    v = fases[f]['v']
    s = fases[f]['s']
    goal = fases[f]['goal']
    obst = fases[f]['obst']

    mous_pos = pygame.mouse.get_pos()
    rndm = np.array([1,1])
    v1 = mous_pos-s0
    norm = np.linalg.norm(v1)

    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if play_button_text_rect.collidepoint(event.pos):
                pagina_atual = "jogo"

            elif mous_pos[1]>100 and pagina_atual == "jogo":
                mouse_click = True
            elif event.button == 1:
                # print("mouse down")
                header.atualiza_estado()

    if mouse_click:
        v.append((v1/norm*10+rndm))
        s.append(s0)
        mouse_click = False
        n = len(v)

    em_jogo = list()

    for i in range(n):
        if goal.collide(s[i]):
            # rodando = False
            f+=1
        else:
            valor = True
            if (s[i][0]<10 or s[i][0]>790 or s[i][1]<110 or s[i][1]>590) or obst.collide(s[i]): # Se eu chegar ao limite da tela, reinicio a posição do personagem
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
        v[i] = v[i] + corpo[0].calcula_a(s[i])*10 + corpo[1].calcula_a(s[i])*50
        s[i] = s[i] + 0.1 * v[i]


    if pagina_atual == "jogo":
    
        screen.blit(pygame.image.load("./sprites/fundo2.png"), (0,0))

        # Desenhar personagem
        for i in range(n):
            rect = pygame.Rect(s[i], (10, 10))  # First tuple is position, second is size.
            screen.blit(personagem, rect)

        pygame.draw.circle(screen,"BLUE",corpo[0].get_pos(),15,0)    
        planeta1 = pygame.image.load("./sprites/planeta1.png")
        planeta2 = pygame.image.load("./sprites/planeta2.png")
        lixo = pygame.image.load("./sprites/lixo.png")
        
        planeta1 = pygame.transform.scale(planeta1, (80, 80))
        planeta2 = pygame.transform.scale(planeta2, (80, 80))
        lixo = pygame.transform.scale(lixo, (150, 150))

        screen.blit(planeta1, (corpo[0].get_pos()[0]-25 ,corpo[0].get_pos()[1] -25))
        screen.blit(planeta2, (corpo[1].get_pos()[0]-25,corpo[1].get_pos()[1]-25))
        screen.blit(lixo, (obst.getRect()[0]-50 ,obst.getRect()[1] -50))
        pygame.draw.rect(screen,"GREEN",goal.getRect())
        header.desenha()
        pygame.display.update()
        
    elif pagina_atual == "inicio":
        screen.blit(background_image, (0, 0))
    
        # Draw the title text
        screen.blit(title_text, title_text_rect)
        
        # Draw the play button
        pygame.draw.rect(screen, (0, 0, 0), (play_button_text_rect.left - 100, play_button_text_rect.top - 10, play_button_text_rect.width + 200, play_button_text_rect.height + 20))
        screen.blit(play_button_text, play_button_text_rect)
        
        # Draw the quit button
        pygame.draw.rect(screen, (0, 0, 50), (quit_button_text_rect.left - 100, quit_button_text_rect.top - 10, quit_button_text_rect.width + 200, quit_button_text_rect.height + 20))
        screen.blit(quit_button_text, quit_button_text_rect)
        
        # Update the screen
        pygame.display.flip()


    # Desenhar fundo

    # Update!

    fases[f]['v'] = v
    fases[f]['s'] = s

# Terminar tela
pygame.quit()