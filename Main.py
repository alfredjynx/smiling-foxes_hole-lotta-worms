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
fase = {"fase":1,'corpo':[Planeta(np.array([200,200]),350),Planeta(np.array([600,300]),350)],"v":v,"s":s,"goal":Ret((350,350),(50,50)),"obst":[Ret((250,250),(50,50))]}

# Personagem
personagem = pygame.Surface((5, 5))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem

# Inicialização das variáveis utilizadas nas verificações do código
n = len(v) #número de bolinhas na tela
f = 0 #número da fase, incrementado a cada Goal atingido
b = 10 #número de bolinhas restantes (possíveis de serem "atiradas")
reset = False #reset de bolinhas, um +15 no número de bolinhas
check_n = False #após a utilização de todas as bolinhas, vê se ainda há bolinhas em jogo antes de interromper o pygame
rodando = True #básico: utilizado para entrar ou sair do gameloop
mouse_click = False #vê se houve click do mouse, muda para true caso há uma click do mouse


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
    elif f!=0 and f%5==0:
        obst.append(Ret((random.randint(0,690),random.randint(150,500)),(50,50)))
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
            # se não for no Header, registrar o click
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
            goal.random()
            for i in range(len(obst)):
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
        rodando=False


    # Processar posicoes
    for i in range(n):
        v[i] = v[i] + corpo[0].calcula_a(s[i])*10 + corpo[1].calcula_a(s[i])*50
        s[i] = s[i] + header.get_porcentagem_forca() * v[i]


    # Desenhar fundo
    screen.blit(pygame.image.load("./sprites/fundo2.png"), (0,0))


    # Desenhar personagem/bolinhas
    for i in range(n):
        rect = pygame.Rect(s[i], (10, 10))  # First tuple is position, second is size.
        screen.blit(personagem, rect)


    # BLIT PLANETAS 
    
    planeta1 = pygame.image.load("./sprites/planeta1.png")
    planeta2 = pygame.image.load("./sprites/planeta2.png")
    lixo = pygame.image.load("./sprites/lixo.png")
    planeta1 = pygame.transform.scale(planeta1, (80, 80))
    planeta2 = pygame.transform.scale(planeta2, (80, 80))
    lixo = pygame.transform.scale(lixo, (150, 150))
    screen.blit(planeta1, (corpo[0].get_pos()[0]-25 ,corpo[0].get_pos()[1] -25))
    screen.blit(planeta2, (corpo[1].get_pos()[0]-25,corpo[1].get_pos()[1]-25))
    for i in range(len(obst)):
        screen.blit(lixo, (obst[i].getRect()[0]-50 ,obst[i].getRect()[1] -50))

    # desenho do objetivo
    pygame.draw.rect(screen,"GREEN",goal.getRect())
    

    # desenho do Header 
    header.desenha()

    # Update!
    pygame.display.update()

    # reinicialização das listas de vetores, para possibilitar a utilização em loops posteriores
    fase['v'] = v
    fase['s'] = s

# Terminar tela
pygame.quit()