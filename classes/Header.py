import pygame

class Header():
    def __init__(self, screen):
        self.screen = screen
        self.width = 800
        self.height = 100
        self.pos = (0,0)
        
        self.cor_fundo = (255,255,255)
        self.quadrado_header = pygame.Rect((0,0), (self.width, self.height) )

        self.cor_slider = (0,0,0)
        self.slider = pygame.Rect((37,50), (self.width/2-50, self.height/4) )

        self.cor_quantidade_slider = (18,10,255)

        self.quantidade_slider = pygame.Rect((37, 50), ((self.width/2-50)*0.3, self.height/4) )

        self.porcentagem_forca = 0.3

        self.quit = pygame.Rect((570,15),(210,35))
    
    
    def desenha(self,pont,fase,bolas):
        
        pygame.draw.rect(self.screen, self.cor_fundo, self.quadrado_header)
        pygame.draw.rect(self.screen, self.cor_slider, self.slider)
        pygame.draw.rect(self.screen, self.cor_quantidade_slider, self.quantidade_slider)
        pygame.draw.rect(self.screen, "RED", self.quit)

        pos = pygame.mouse.get_pos()

        # highlight do botão onde o mouse está
        if self.atualiza_quit(pos):
            pygame.draw.rect(self.screen,(173, 23, 85),self.quit,3)

         # you have to call this at the start, 
                   # if you want to use this module.
        my_font = pygame.font.SysFont('Consolas', 27)
        text_surface = my_font.render(f'Velocidade {int(self.porcentagem_forca*100)}%', False, (0, 0, 0))
        self.screen.blit(text_surface, (37,10))

        my_font = pygame.font.SysFont('consolas', 17)
        text_surface = my_font.render(f'Pontuação - {int(pont)}', False, (0, 0, 0))
        self.screen.blit(text_surface, (440,20))
        text_surface = my_font.render(f'Fase - {int(fase)}', False, (0, 0, 0))
        self.screen.blit(text_surface, (440,60))
        text_surface = my_font.render(f'Bolinhas Restantes - {int(bolas)}', False, (0, 0, 0))
        self.screen.blit(text_surface, (570,60))
        text_surface = my_font.render('QUIT', False, "WHITE")
        rect = text_surface.get_rect()
        rect.center = (570+105,15+35/2)
        self.screen.blit(text_surface, rect)

        

   

    def atualiza_estado(self):
        
        mouse = pygame.mouse.get_pos()
        if self.slider.collidepoint(mouse):
            
            self.porcentagem_forca = (mouse[0] - 37)/ (self.width/2-50)

            self.quantidade_slider = pygame.Rect((37,50), ((self.width/2-50)*self.porcentagem_forca, self.height/4) )

    def get_porcentagem_forca(self):
        return self.porcentagem_forca

    def atualiza_quit(self,pos):
        return self.quit.collidepoint(pos)