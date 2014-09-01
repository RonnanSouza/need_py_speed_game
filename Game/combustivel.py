import pygame

class Combustivel(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.comb = pygame.image.load('imagens/fuel.png')
        self.tam_comb_x = 10
        self.tam_comb_y = 10
        self.pos_comb_x = 490
        self.pos_comb_y = 350
        self.comb_print = pygame.transform.scale(self.comb, (self.tam_comb_x, self.tam_comb_y))
        self.rect_comb = self.comb_print.get_rect() 
        self.rect_comb.x, self.rect_comb.y = (450, 350)
        

    def mover_comb(self):
        self.pos_comb_x -= 0.1 * (self.tam_comb_x / 5)
        self.pos_comb_y += 0.1 * (self.tam_comb_y / 10)
        self.tam_comb_x += 1 
        self.tam_comb_y += 1
        if self.pos_comb_y > 1100:
            self.tam_comb_x = 10
            self.tam_comb_y = 10
            self.pos_comb_x = 490 
            self.pos_comb_y = 350


    def print_comb(self, screen):
        self.comb_print = pygame.transform.scale(self.comb, (self.tam_comb_x, self.tam_comb_y))
        self.screen.blit(self.comb_print, (self.pos_comb_x, self.pos_comb_y))
        self.rect_comb.normalize()


        
        
    
        
