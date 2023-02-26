import numpy
import pygame
import random

class Menu:
    def __init__(self) -> None:
        self.title_font = pygame.font.SysFont(None, 64)
        self.title_text = self.title_font.render("Smiling Foxes", True, (255, 255, 255))
        self.title_text_rect = self.title_text.get_rect()
        self.title_text_rect.center = (800 // 2, 600 // 3)

        self.play_button_font = pygame.font.SysFont(None, 32)
        self.play_button_text = self.play_button_font.render("Jogar", True, (255, 255, 255))
        self.play_button_text_rect = self.play_button_text.get_rect()
        self.play_button_text_rect.center = (800 // 2, 600 // 2)

        self.quit_button_font = pygame.font.SysFont(None, 32)
        self.quit_button_text = self.quit_button_font.render("Quit", True, (255, 255, 255))
        self.quit_button_text_rect = self.quit_button_text.get_rect()
        self.quit_button_text_rect.center = (800 // 2, 600 // 1.5)

        self.quit = pygame.Rect((0,0),(250,45))
        self.quit.center = (800 // 2, 600 // 1.5)
        self.start = pygame.Rect((0,0),(260,45))
        self.start.center = (800 // 2, 600 // 2)

        self.dica_button_font = pygame.font.SysFont(None, 22)
        self.dica_button_text = self.dica_button_font.render("Nova Dica", True, (255, 255, 255))
        self.dica_button_text_rect = self.dica_button_text.get_rect()
        self.dica_button_text_rect.center = (470, 550)

        self.quit = pygame.Rect((0,0),(250,45))
        self.quit.center = (800 // 2, 600 // 1.5)
        self.start = pygame.Rect((0,0),(260,45))
        self.start.center = (800 // 2, 600 // 2)
        self.dica_rect = pygame.Rect((0,0),(120,30))
        self.dica_rect.center = self.dica_button_text_rect.center

        self.som_click = pygame.mixer.Sound("./sons/click.mp3")


        self.dicas = ['Mudar a velocidade afeta TODOS os projéteis da tela',
'A hitbox das lixeiras é menor do que a imagem delas',
'Algumas fases impossíveis são possíveis por meio da sorte',
'Por favor dá uma nota alta Tiagão, nunca te pedi nada',
'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH',
'As vezes eu acho que a felicidade é momentânea e o sofrimento é eterno',
'A prática leva à perfeição, então continue apostando em casino online',
'A culpa nunca é dos desenvolvedores',
'Eu fico pensando que o motivo pelo qual eu sou tão sozinho é minha enorme raba',
'Siga "Emerson Perigo" nas redes sociais',
'Doce de leite ruim é melhor que brigadeiro bom',
'O homem nasce bom, mas bits Gui nasm o corrompe',
'O amor é uma flor roxa que nasce no coração dos troxa',
'To ficando Tchubiraumdaun das ideia',
'se tiver em dúvida entre Rivotril e Ritalina, use os dois',
'Nada é ilegal se a polícia não souber',
'Misture amônia com alvejante, muito legal',
'Se um dia for para maresias, visite o capeta do nenê. Ele é DJ',
'Frequente o Tomás Uma Bar, melhor espetinho da Santa Cecília',
'Conheci um cara que o pai dele também era seu primo',
'Tenho pena de quem não me conhece',
'Meu pai é agiota, minha mãe é filósofa e meu tio é carteiro',
'Eu não aguento mais',
'Visite Cascadura',
'Ainda bem que eu não sou você :)',
'O mundo gira e vacilão roda',
'Em dezembro de 81',
'Pra ter dica tem que comer legume',
'não',
'Quarto 309',
'O Leo é o novo Barros',
'Primeiro date na ROOM. Foi cagada...',
'Fecapejada',
'Jogo do Flamengo na CazéTV é sacanagem',
'Pra quem está começando na academia, recomendo trembolona',
'... mas foi pouco',
'Japonesas em Porto Seguro',
'Parmegiana de frango trocando batata por ovo',
'O Léo é a minhoca',
'Ações do robô: direita, esquerda, sugar',
'Quando eu morrer eu quero se enterrada de lado',
'Pelo amor de deus eu preciso de nota, tenha piedade']
        
        self.dica = self.dicas[random.randint(0,len(self.dicas)-1)]
        

    def desenha(self,screen,background_image,init,pont,new_dica):

        screen.blit(background_image, (0, 0))
        pos = pygame.mouse.get_pos()


        # Draw the title text (ou pontuação, se ela existir)
        if not init:
            title_text = self.title_font.render(f"Pontuação: {int(pont)}", True, (255, 255, 255))
            rect = title_text.get_rect()
            rect.center = (800 // 2, 600 // 3)
            screen.blit(title_text, rect)

            if new_dica:
                self.dica = self.dicas[random.randint(0,len(self.dicas)-1)]
            
            font = pygame.font.SysFont(None, 25)
            dicas = font.render(self.dica, True, (255, 255, 255))
            rect = dicas.get_rect()
            rect.center = (800 // 2, 600 * 0.8)
            screen.blit(dicas, rect)

            screen.blit(self.dica_button_text, self.dica_button_text_rect)

            if self.atualiza_dica(pos):
                 pygame.draw.rect(screen,(173, 23, 85),self.dica_rect,3)

        else:
                    screen.blit(self.title_text, self.title_text_rect)
        
        # Draw the play button
        pygame.draw.rect(screen, (0, 0, 0), (self.play_button_text_rect.left - 100, self.play_button_text_rect.top - 10, self.play_button_text_rect.width + 200, self.play_button_text_rect.height + 20))
        screen.blit(self.play_button_text, self.play_button_text_rect)
        
        # Draw the quit button
        pygame.draw.rect(screen, (0, 0, 50), (self.quit_button_text_rect.left - 100, self.quit_button_text_rect.top - 10, self.quit_button_text_rect.width + 200, self.quit_button_text_rect.height + 20))
        screen.blit(self.quit_button_text, self.quit_button_text_rect)

        # highlight do botão onde o mouse está
        if self.atualiza_jogo(pos):
            pygame.draw.rect(screen,(173, 23, 85),self.start,3)
        elif self.atualiza_quit(pos):
            pygame.draw.rect(screen,(173, 23, 85),self.quit,3)

    
    def atualiza_jogo(self,pos):
        return self.start.collidepoint(pos)

    def atualiza_quit(self,pos):
        return self.quit.collidepoint(pos)
    
    def atualiza_dica(self,pos):
         return self.dica_rect.collidepoint(pos)
    
