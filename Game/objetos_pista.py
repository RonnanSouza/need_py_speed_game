import pygame, sys, os, random

class Carro_inimigo(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.objetos = ['adv_car.png'] #, 'adv_car2.png', 'adv_car3.png', 'adv_car4.png']
        self.objeto =  pygame.image.load('imagens' + os.sep + random.choice(self.objetos))
        self.tam_objeto_x = 100
        self.tam_objeto_y = 100
        self.pos_objeto_x = 505
        self.pos_objeto_y = 350 
        self.objeto_print = pygame.transform.scale(self.objeto, (self.tam_objeto_x, self.tam_objeto_y))
        self.rect_objeto= self.objeto_print.get_rect()
        self.rect_objeto.x, self.rect_objeto.y = (505, 350)
    
    def mover_objeto(self):
        self.pos_objeto_x += 0.1 * (self.tam_objeto_x / 10) 
        self.pos_objeto_y += 0.1 * (self.tam_objeto_y / 10)
        self.tam_objeto_x += 1 
        self.tam_objeto_y += 1 
        self.rect_objeto = self.objeto_print.get_rect()
        self.rect_objeto.x, self.rect_objeto.y = (self.pos_objeto_x, self.pos_objeto_y)
        if self.pos_objeto_y > 800 or self.pos_objeto_x > 1600:
            self.objeto =  pygame.image.load('imagens' + os.sep + random.choice(self.objetos))
            self.pos_objeto_y = 350
            self.pos_objeto_x = 505
            self.tam_objeto_x = 20
            self.tam_objeto_y = 20
            self.rect_objeto = self.objeto_print.get_rect()
            self.rect_objeto.x, self.rect_objeto.y = (self.pos_objeto_x, self.pos_objeto_y)
    def print_objeto(self, screen):
        self.objeto_print = pygame.transform.scale(self.objeto, (self.tam_objeto_x, self.tam_objeto_y))
        self.screen.blit(self.objeto_print, (self.pos_objeto_x, self.pos_objeto_y)) 
        #self.rect_objeto.normalize()




