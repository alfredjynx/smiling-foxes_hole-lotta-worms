import pygame
import numpy as np
from classes.Planetas import Planeta
from classes.Ret import Ret
from classes.Header import Header
import random

# inicialização do Pygame
pygame.init()

# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

# cor do fundo básico
BLACK = (0, 0, 0, 0.2)

# cor do "personagem" (bolinha)
COR_PERSONAGEM = (30, 200, 20)

# classe header, responsável pelo cabeçalho do jogo (com o slider de força)
header = Header(screen)

# posição e velocidade inicial dos pontos básicos
s0 = np.array([200,500])
v0 = np.array([10, -10])

# inicialização da lista de velocidae de pontos e da posição dos mesmos
v = list()
s = list()

# Inicializar a fase básica

# fase comentada: fase com dois planetas
fase = {"fase":1,'corpo':Planeta(np.array([200,200]),350),"v":v,"s":s,"goal":Ret((350,350),(50,50)),"obst":[Ret((250,250),(50,50))]}

# Personagem
personagem = pygame.Surface((5, 5))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem

# fontes e botoes
title_font = pygame.font.SysFont(None, 64)
title_text = title_font.render("Smiling Foxes", True, (255, 255, 255))
title_text_rect = title_text.get_rect()
title_text_rect.center = (800 // 2, 600 // 3)

play_button_font = pygame.font.SysFont(None, 32)
play_button_text = play_button_font.render("Jogar", True, (255, 255, 255))
play_button_text_rect = play_button_text.get_rect()
play_button_text_rect.center = (800 // 2, 600 // 2)

quit_button_font = pygame.font.SysFont(None, 32)
quit_button_text = quit_button_font.render("Quit", True, (255, 255, 255))
quit_button_text_rect = quit_button_text.get_rect()
quit_button_text_rect.center = (800 // 2, 600 // 1.5)

background_image = pygame.image.load("./sprites/buraco.png")

planeta1 = pygame.image.load("./sprites/planeta1.png")
planeta2 = pygame.image.load("./sprites/planeta2.png")
lixo = pygame.image.load("./sprites/lixo.png")

planeta1 = pygame.transform.scale(planeta1, (80, 80))
planeta2 = pygame.transform.scale(planeta2, (80, 80))
lixo = pygame.transform.scale(lixo, (150, 150))

fox = pygame.image.load("./sprites/fox.png")
fox = pygame.transform.scale(fox, (50, 50))


# Inicialização das variáveis utilizadas nas verificações do código
n = len(v) #número de bolinhas na tela
f = 0 #número da fase, incrementado a cada Goal atingido
b = 15 #número de bolinhas restantes (possíveis de serem "atiradas")
reset = False #reset de bolinhas, um +15 no número de bolinhas
mais_obst = False #checa se está na hora de adicionar mais um obstáculo
check_n = False #após a utilização de todas as bolinhas, vê se ainda há bolinhas em jogo antes de interromper o pygame
rodando = True #básico: utilizado para entrar ou sair do gameloop
mouse_click = False #vê se houve click do mouse, muda para true caso há uma click do mouse
pagina_atual = "inicio" # página atual do jogo, inicialmente é a página inicial

# se "rodando" for true, entrar no while
while rodando:

    # inicialização de variáveis da fase
    corpo = fase['corpo']
    v = fase['v']
    s = fase['s']
    goal = fase['goal']
    obst = fase['obst']

    # checa o número de bolinhas em jogo, também adiciona bolinhas a cada 10 níveis atingidos
    if f!=0 and f%10==0 and reset:
        b+=15
        reset = False
    elif f!=0 and f%5==0 and mais_obst:
        obst.append(Ret((random.randint(0,690),random.randint(150,500)),(50,50)))
        mais_obst = False
    elif f%5!=0:
        mais_obst = True
    else:
        reset = True

    # básicos de algumas operações. Ex.: ver se o mouse está na tela principal ou no header, cria um vetor de aceleração mirando no mouse na hora do click
    mous_pos = pygame.mouse.get_pos()
    rndm = np.array([1,1])
    v1 = mous_pos-s0
    norm = np.linalg.norm(v1)

    # Capturar eventos
    for event in pygame.event.get():
        # quando quiser fechar a janela, dá pra fechar
        if event.type == pygame.QUIT:
            rodando = False
        # se houver click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            # se o click for no botão de inicio, mudar a página atual para "jogo"
            if play_button_text_rect.collidepoint(event.pos):
                pagina_atual = "jogo"

            # se não for no Header, registrar o click
            if mous_pos[1]>100 and pagina_atual == "jogo":
                mouse_click = True
            # se for no header, atualizar o estado do slider de força
            elif event.button == 1:
                # print("mouse down")
                header.atualiza_estado()

    # se houve click na tela, adicionar uma bolinha na lista e retirar um dos valores das bolinhas disponíveis (apenas funciona se houver click e bolinhas disponíveis)
    if mouse_click and b>0:
        b-=1
        v.append((v1/norm*10+rndm))
        s.append(s0)
        mouse_click = False
        n = len(v)
    # se as bolinhas acabarem, checar se ainda há bolinhas em jogo
    elif b==0:
        check_n = True

    # para a checagem de se as bolas estão em jogo
    em_jogo = list()

    # checar todas as bolinhas que estão na tela
    for i in range(n):
        # se você atingir o objetivo (Goal), randomizar o nível e adicionar um valor na variável de "número de fase" (f)
        if goal.collide(s[i]):
            f+=1
            corpo.randomized(0,690,150,450)
            goal.random()
            while goal.collide(s0):
                goal.random()
            for i in range(len(obst)):
                obst[i].random()
                while obst[i].collide(s0):
                    obst[i].random()
        # se não, checar se elas ainda estão na tela e não no header
        else:
            # valor inicializado como em jogo, e depois há uma checagem
            valor = True
            if (s[i][0]<10 or s[i][0]>790 or s[i][1]<110 or s[i][1]>590): # Se eu chegar ao limite da tela, reinicio a posição do personagem
                valor = False
            
            for o in obst:
                if o.collide(s[i]):
                    valor = False

            # utilizado para fazer um update na lista de vetores e posições principal ("v" e "s" respectivamente)
            em_jogo.append(valor)

    # se houverem bolinhas em jogo
    if n>0:
        # listas vazias para a possibilidade de append existir
        v_novo = list()
        s_novo = list()
        # contador que só é modificado quando uma bolinhas em jogo é adicionada nas novas listas
        cont = 0
        # checagem de bolinhas a bolinhas, que só são adicionadas a nova lista se estiverem em jogo
        for value in em_jogo:
            if value:
                v_novo.append(v[cont])
                s_novo.append(s[cont])
            cont+=1
        # novas listas substituem as antigas, possibilitando a permanecência e bolinhas antigas e a eliminação de novas
        v = v_novo
        s = s_novo
        n = len(v)
    
    # Controlar frame rate
    clock.tick(FPS)

    # checar o número de bolinhas em jogo se b=0, parar o jogo se todas forem eliminadas
    if check_n and n<=0:
        pagina_atual = "inicio"


    # Processar posicoes
    for i in range(n):
        v[i] = v[i] + corpo.calcula_a(s[i])*30 
        s[i] = s[i] + header.get_porcentagem_forca() * v[i]


    if pagina_atual == "jogo":
        
        # Desenhar fundo
        screen.blit(pygame.image.load("./sprites/fundo2.png"), (0,0))

        header.desenha()

        # Desenhar personagem
        for i in range(n):
            rect = pygame.Rect(s[i]-np.array([10,10]), (10, 10))  # First tuple is position, second is size.
            screen.blit(fox, rect)

        # BLIT PLANETAS 
        planeta1 = pygame.image.load("./sprites/planeta1.png")
        lixo = pygame.image.load("./sprites/lixo.png")
        planeta1 = pygame.transform.scale(planeta1, (80, 80))
        lixo = pygame.transform.scale(lixo, (150, 150))
        screen.blit(planeta1, (corpo.get_pos()[0]-25 ,corpo.get_pos()[1] -25))
        for i in range(len(obst)):
            screen.blit(lixo, (obst[i].getRect()[0]-50 ,obst[i].getRect()[1] -50))

        # Desenhar goal
        pygame.draw.rect(screen,"GREEN",goal.getRect())
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

        # Reset de variáveis
        fase = {"fase":1,'corpo':Planeta(np.array([200,200]),350),"v":v,"s":s,"goal":Ret((350,350),(50,50)),"obst":[Ret((250,250),(50,50))]}
        n = len(v) #número de bolinhas na tela
        f = 0 #número da fase, incrementado a cada Goal atingido
        b = 15 #número de bolinhas restantes (possíveis de serem "atiradas")
        reset = False #reset de bolinhas, um +15 no número de bolinhas
        mais_obst = False #checa se está na hora de adicionar mais um obstáculo
        check_n = False #após a utilização de todas as bolinhas, vê se ainda há bolinhas em jogo antes de interromper o pygame
        rodando = True #básico: utilizado para entrar ou sair do gameloop
        mouse_click = False #vê se houve click do mouse, muda para true caso há uma click do mouse
        pagina_atual = "inicio"

    # Update!
    

    # reinicialização das listas de vetores, para possibilitar a utilização em loops posteriores
    fase['v'] = v
    fase['s'] = s

# Terminar tela
pygame.quit()