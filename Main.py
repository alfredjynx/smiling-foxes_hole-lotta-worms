import os
import pygame
import numpy as np
from classes.Planetas import Planeta
from classes.Ret import Ret
from classes.Header import Header

# inicialização do Pygame
pygame.init()

# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

# cor do fundo básico
BLACK = (0, 0, 0, 0.2)
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
fase = {"fase":1,'corpo':[Planeta(np.array([200,200]),350),Planeta(np.array([600,300]),350)],"v":v,"s":s,"goal":Ret((350,350),(50,50)),"obst":Ret((250,250),(50,50))}

# Personagem
personagem = pygame.Surface((5, 5))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem

f = 0

# se "rodando" for true, entrar no while
while rodando:

    # checa o número de bolinhas em jogo, também adiciona bolinhas a cada 10 níveis atingidos
    if f!=0 and f%10==0 and reset:
        b+=15
        reset = False
    else:
        reset = True

    # inicialização de variáveis da fase
    corpo = fase['corpo']
    v = fase['v']
    s = fase['s']
    goal = fase['goal']
    obst = fase['obst']

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mous_pos[1]>100:
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
            for i in range(len(corpo)):
                corpo[i].randomized()
            goal.randomized()
            obst.randomized()
        # se não, checar se elas ainda estão na tela e não no header
        else:
            # valor inicializado como em jogo, e depois há uma checagem
            valor = True
            if (s[i][0]<10 or s[i][0]>790 or s[i][1]<110 or s[i][1]>590) or obst.collide(s[i]): # Se eu chegar ao limite da tela, reinicio a posição do personagem
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
        rodando=False


    # Processar posicoes
    for i in range(n):
        v[i] = v[i] + corpo[0].calcula_a(s[i])*10 + corpo[1].calcula_a(s[i])*50
        s[i] = s[i] + header.get_porcentagem_forca() * v[i]


    # Desenhar fundo
    
    screen.blit(pygame.image.load("./sprites/fundo2.png"), (0,0))


    # Desenhar personagem
    for i in range(n):
        rect = pygame.Rect(s[i], (10, 10))  # First tuple is position, second is size.
        screen.blit(personagem, rect)

    pygame.draw.circle(screen,"BLUE",corpo[0].get_pos(),15,0)
    # pygame.draw.circle(screen,"RED", corpo[1].get_pos(),15,0)


    # BLIT PLANETAS 
    
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

    # Update!

    # reinicialização das listas de vetores, para possibilitar a utilização em loops posteriores
    fase['v'] = v
    fase['s'] = s

# Terminar tela
pygame.quit()