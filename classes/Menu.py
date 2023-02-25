import numpy
import pygame

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

        self.dicas = ['Mudar a velocidade afeta todos os projéteis da tela, não só os que serão disparados','As lixerias nem sempre ']
        

    def desenha(self,screen,background_image,init,pont):

        screen.blit(background_image, (0, 0))

        # Draw the title text (com pontuação se ela existir)
        if not init:
            title_text = self.title_font.render(f"Pontuação: {int(pont)}", True, (255, 255, 255))
            rect = title_text.get_rect()
            rect.center = (800 // 2, 600 // 3)
            screen.blit(title_text, rect)



        else:
            screen.blit(self.title_text, self.title_text_rect)

        
        # Draw the play button
        pygame.draw.rect(screen, (0, 0, 0), (self.play_button_text_rect.left - 100, self.play_button_text_rect.top - 10, self.play_button_text_rect.width + 200, self.play_button_text_rect.height + 20))
        screen.blit(self.play_button_text, self.play_button_text_rect)
        
        # Draw the quit button
        pygame.draw.rect(screen, (0, 0, 50), (self.quit_button_text_rect.left - 100, self.quit_button_text_rect.top - 10, self.quit_button_text_rect.width + 200, self.quit_button_text_rect.height + 20))
        screen.blit(self.quit_button_text, self.quit_button_text_rect)

        pos = pygame.mouse.get_pos()

        # highlight do botão onde o mouse está
        if self.atualiza_jogo(pos):
            pygame.draw.rect(screen,(173, 23, 85),self.start,3)
        elif self.atualiza_quit(pos):
            pygame.draw.rect(screen,(173, 23, 85),self.quit,3)

    
    def atualiza_jogo(self,pos):
        return self.start.collidepoint(pos)

    def atualiza_quit(self,pos):
        return self.quit.collidepoint(pos)
    
