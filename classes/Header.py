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
    
    
    def desenha(self):
        
        pygame.draw.rect(self.screen, self.cor_fundo, self.quadrado_header)
        pygame.draw.rect(self.screen, self.cor_slider, self.slider)
        pygame.draw.rect(self.screen, self.cor_quantidade_slider, self.quantidade_slider)

         # you have to call this at the start, 
                   # if you want to use this module.
        my_font = pygame.font.SysFont('arial', 30)
        # print(self.porcentagem_forca)
        text_surface = my_font.render(f'Força {int(self.porcentagem_forca*100)}%', False, (0, 0, 0))

        self.screen.blit(text_surface, (37,10))

   

    def atualiza_estado(self):
        
        mouse = pygame.mouse.get_pos()
        if self.slider.collidepoint(mouse):
            
            self.porcentagem_forca = (mouse[0] - 37)/ (self.width/2-50)

            self.quantidade_slider = pygame.Rect((37,50), ((self.width/2-50)*self.porcentagem_forca, self.height/4) )

    def get_porcentagem_forca(self):
        return self.porcentagem_forca