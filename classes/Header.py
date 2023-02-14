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
        self.slider = pygame.Rect((37,37), (self.width/2-50, self.height/4) )

        self.cor_quantidade_slider = (18,10,255)
        self.quantidade_slider = pygame.Rect((37,37), ((self.width/2-50)*0.3, self.height/4) )

        self.porcentagem_forca = 0.3
    
    
    def desenha(self):
        
        pygame.draw.rect(self.screen, self.cor_fundo, self.quadrado_header)
        pygame.draw.rect(self.screen, self.cor_slider, self.slider)
        pygame.draw.rect(self.screen, self.cor_quantidade_slider, self.quantidade_slider)

   

    def atualiza_estado(self):
        # see if the mouse is over the button
        
        mouse = pygame.mouse.get_pos()
        if self.slider.collidepoint(mouse):
            
            self.quantidade_de_forca = (mouse[0] - 37)/ (self.width/2-50)

            self.quantidade_slider = pygame.Rect((37,37), ((self.width/2-50)*self.quantidade_de_forca, self.height/4) )