import pygame
import numpy as np
from classes.Planetas import Planeta
from classes.Ret import Ret
from classes.Header import Header
from classes.Menu import Menu
import random
import pygame.mixer

# inicialização do Pygame
pygame.init()
pygame.mixer.init()

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

menu = Menu()

background_image = pygame.image.load("./sprites/buraco.png")

planeta = pygame.image.load("./sprites/planet_pixel.png")
# lixo = pygame.image.load("./sprites/lixo.png")

# Origem da imagem do lixo: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Ffree-png-nhvgc&psig=AOvVaw2SIPcnyBhCR9_JSLz4dZF3&ust=1677415653254000&source=images&cd=vfe&ved=0CBAQjhxqFwoTCOjoxK_asP0CFQAAAAAdAAAAABAE
lixo = pygame.image.load("./sprites/garbage-removebg.png")

# Origem da iamgem do lixo: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Ffree-png-nhvgc&psig=AOvVaw3mx7-cZVaF9vqfaWQ86gd5&ust=1677417200573000&source=images&cd=vfe&ved=0CBEQjhxqFwoTCPjx_5HgsP0CFQAAAAAdAAAAABAK
# lixo = pygame.image.load("./sprites/lixo.png")

planeta = pygame.transform.scale(planeta, (80, 80))
lixo = pygame.transform.scale(lixo, (10, 10))

fox = pygame.image.load("./sprites/fox.png")
fox = pygame.transform.scale(fox, (10, 10))

# load dos sons
som_tiro = pygame.mixer.Sound("./sons/tiro.mp3")
som_tiro.set_volume(0.5)
som_explosao = pygame.mixer.Sound("./sons/explosao.mp3")
som_click = pygame.mixer.Sound("./sons/click.mp3")
som_click.set_volume(0.5)

# Inicialização das variáveis utilizadas nas verificações do código
n = len(v) #número de bolinhas na tela
f = 0 #número da fase, incrementado a cada Goal atingido
b = 15 #número de bolinhas restantes (possíveis de serem "atiradas")
reset = False #reset de bolinhas, um +5 no número de bolinhas
mais_obst = False #checa se está na hora de adicionar mais um obstáculo
check_n = False #após a utilização de todas as bolinhas, vê se ainda há bolinhas em jogo antes de interromper o pygame
rodando = True #básico: utilizado para entrar ou sair do gameloop
mouse_click = False #vê se houve click do mouse, muda para true caso há uma click do mouse
pagina_atual = "inicio" # página atual do jogo, inicialmente é a página inicial
pont = 0 # pontuação
init = True # Vê se é a primeira vez que o Pygame é rodado
p = True
new_dica = False

# se "rodando" for true, entrar no while
while rodando:

    # inicialização de variáveis da fase
    corpo = fase['corpo']
    v = fase['v']
    s = fase['s']
    goal = fase['goal']
    obst = fase['obst']

    # checa o número de bolinhas em jogo, também adiciona bolinhas a cada 10 níveis atingidos
    if f!=0 and f%5==0 and mais_obst:
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
            if pagina_atual=="inicio":
                if menu.atualiza_jogo(event.pos):
                    som_click.play()
                    pagina_atual = "jogo"
                    p = True
                    init = False
                    new_dica=True
                elif menu.atualiza_quit(event.pos):
                    som_click.play()
                    rodando = False
                elif menu.atualiza_dica(event.pos):
                    som_click.play()
                    new_dica = True

            else:
                # se não for no Header, registrar o click
                if mous_pos[1]>100 and pagina_atual == "jogo":
                    mouse_click = True
                # se for no header, atualizar o estado do slider de força
                elif event.button == 1:
                    # print("mouse down")
                    header.atualiza_estado()
                    if header.atualiza_quit(mous_pos):
                        som_click.play()
                        pagina_atual = "inicio"

    if not rodando:
        break

    # se houve click na tela, adicionar uma bolinha na lista e retirar um dos valores das bolinhas disponíveis (apenas funciona se houver click e bolinhas disponíveis)
    if mouse_click and b>0:
        som_tiro.play()
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
        # se você atingir o objetivo (Goal), randomizar o nível e adicionar um valor na variável de "número de fase" (f), assim como +2 blinhas adicionadas no "pente" da arma
        if goal.collide(s[i]):
            som_explosao.play()
            f+=1
            b+=2
            pont+=10*(1 + f/10)
            corpo.randomized(0,690,150,450)
            # continua randomizando a posição até que o planeta esteja longe o suficiente do lançador
            while corpo.get_pos()[0]<150 and corpo.get_pos()[1]>400:
                corpo.randomized(0,690,150,450)
            
            # continua randomizando a posição até que o alvo não colida com o lançador
            goal.random()
            while goal.collide(s0):
                goal.random()

            for i in range(len(obst)):
                obst[i].random()
                # continua randomizando a posição até os obstáculos não colidirem com o lançador
                while obst[i].collide(s0) or obst[i].getRect().colliderect(goal.getRect()):
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
        v[i] = v[i] + corpo.calcula_a(s[i])*50 
        s[i] = s[i] + header.get_porcentagem_forca() * v[i]


    if pagina_atual == "jogo":
        
        # Desenhar fundo
        # screen.blit(pygame.image.load("./sprites/fundo2.png"), (0,0))

        # link do fundo, feito pelo artista Norma2D: https://twitter.com/norma_2d/status/1374371658920722441
        screen.blit(pygame.transform.scale(pygame.image.load("./sprites/fundo_pixel.png"),(1000,600)), (0,0))


        header.desenha(pont,f,b)

        # Desenhar personagem
        for i in range(n):
            rect = pygame.Rect(s[i]-np.array([3,3]), (10,10))  # First tuple is position, second is size.
            screen.blit(fox, rect)

        # BLIT PLANETAS 
        # planeta = pygame.image.load("./sprites/planeta1.png")
        planeta = pygame.Surface((100,100))
        planeta = pygame.transform.scale(planeta,(50,50))

        lixo = pygame.transform.scale(lixo, (80, 80))
        screen.blit(planeta, (corpo.get_pos()[0]-25 ,corpo.get_pos()[1] -25))

        for i in range(len(obst)):
            screen.blit(lixo, (obst[i].getRect()[0]-25,obst[i].getRect()[1]-25))

        # Desenhar goal
        pygame.draw.circle(screen,"WHITE",s0,5)
        pygame.draw.rect(screen,"GREEN",goal.getRect())

        # Update!
        pygame.display.update()
        

    elif pagina_atual == "inicio":
        if p:
            pont_pass = pont
        menu.desenha(screen,background_image,init,pont_pass,new_dica)
        
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
        pont = 0 #pontuação
        p = False
        new_dica = False


    # reinicialização das listas de vetores, para possibilitar a utilização em loops posteriores
    fase['v'] = v
    fase['s'] = s

# Terminar tela
pygame.quit()