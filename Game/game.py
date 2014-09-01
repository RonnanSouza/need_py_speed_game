# coding : utf-8

import pygame, os, sys, time
from pygame import *
from faixa import *
from carro import *
from arvores import *
from intro_menu import *

pygame.init()

# Carregando intro do jogo
introducao_jogo(True)

# Menu Raiz
if menu_raiz(True):    
    tela =  pygame.display.set_mode((1024, 768))
    screen = pygame.display.get_surface()
    fundo = pygame.image.load('imagens' + os.sep + 'road3.png')
    pygame.display.set_caption('Need Py Speed - The Game')
        
    
    clock = pygame.time.Clock()
    
    carro = Carro(screen)
    faixas = [Faixa(screen)]
    arvores_direita = [Arvores(screen, 'direita')]
    arvores_esquerda = [Arvores(screen, 'esquerda')]
    pygame.key.set_repeat(1,1)
    i= 0
    combustivel = 1000
    
    while True:
        clock.tick(500)
        if combustivel <= 0:
            sys.exit()
        # Fechar o game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif pygame.key.get_pressed()[K_ESCAPE]:
                menu_raiz(True)
        ##
        
        tecla = pygame.key.get_pressed()
        carro.mover_carro(tecla)
        if tecla[pygame.K_UP] and velocidade < 2:
            velocidade += 0.1
        elif tecla[pygame.K_DOWN]:
            if velocidade < 1:
                velocidae = 0
            else: velocidade -= 1
    
        tela.blit(fundo, (0, 0))
        if i % 10 == 0 and len(arvores_direita) < 6:
            arvores_direita.append(Arvores(screen, 'direita'))
            arvores_esquerda.append(Arvores(screen, 'esquerda'))
            faixas.append(Faixa(screen))
       
        for j in range(len(arvores_direita)):
            arvores_direita[j].muda_pos_arvore('direita')
            arvores_esquerda[j].muda_pos_arvore('esquerda')
    
            arvores_direita[j].muda_tam_arvore()
            arvores_esquerda[j].muda_tam_arvore()
    
            faixas[j].muda_pos_faixa()
            faixas[j].muda_tam_faixa()
        for j in range(len(arvores_direita)):
            faixas[j].print_faixa(screen)
            arvores_direita[j].print_arvore(screen)
            arvores_esquerda[j].print_arvore(screen)
    
        carro.print_carro(screen)
        pygame.display.update()        
        i += 1 
        combustivel -= 0.1
