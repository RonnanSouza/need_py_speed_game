# coding : utf-8

import pygame, os, sys, time
from pygame import *
from faixa import *
from carro import *
from arvores import *
from intro_menu import *
from objetos_pista import *
from combustivel import *
#from fuel import *

pygame.init()

# Carregando intro do jogo
#introducao_jogo(True)

# Menu Raiz
def jogar(self):
    if menu_raiz(True):
        tela =  pygame.display.set_mode((1024, 768))
        screen = pygame.display.get_surface()
        fundo = pygame.image.load('imagens' + os.sep + 'road3.png')
        pygame.display.set_caption('Need Py Speed - The Game')
        
        PRETO = (0, 0, 0)  
        VERMELHO = (255, 0, 0)
        BRANCO = (255, 255, 255)
        
        clock = pygame.time.Clock()
    
        comb = Combustivel(screen)
        carro = Carro(screen)
        faixas = [Faixa(screen)]
        objeto = Carro_inimigo(screen)
        arvores_direita = [Arvores(screen, 'direita')]
        arvores_esquerda = [Arvores(screen, 'esquerda')]
        pygame.key.set_repeat(1,1)
        i= 0
        combustivel = 1000
        print_comb = False
        mostrar_comb = False
        cont = 21
        while True:
            clock.tick(20)
            if i % 200 == 0 and i != 0:
                print_comb = True
                mostrar_comb = True
            clock.tick(500)
            if combustivel <= 0:
                sys.exit()
            # Fechar o game/ Pausar o game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif pygame.key.get_pressed()[K_p]:
                    if menu_sair(True):
                        jogar(True)
            ##
            
            tecla = pygame.key.get_pressed()
            carro.mover_carro(tecla)
        
            if i % 10 == 0 and len(arvores_direita) < 6:
                arvores_direita.append(Arvores(screen, 'direita'))
                arvores_esquerda.append(Arvores(screen, 'esquerda'))
                faixas.append(Faixa(screen))
            tela.blit(fundo, (0, 0))
          
            for j in range(len(arvores_direita)):
                faixas[j].print_faixa(screen)
                arvores_direita[j].print_arvore(screen)
                arvores_esquerda[j].print_arvore(screen)
                objeto.print_objeto(screen)
            if mostrar_comb == True:
                comb.print_comb(screen)
            carro.print_carro(screen)
            
            # Gasolina
            if cont < 98:
                fonte = pygame.font.Font('fontes' + os.sep + 'nextwaveboldital.ttf',50)
                texto_gasolina = fonte.render("FUEL",True,PRETO)
                screen.blit(texto_gasolina,[910,10])
                
                pygame.draw.rect(screen,PRETO,[950,55,20,100],3)
                pygame.draw.rect(screen,VERMELHO,[951,56,18,98],0)
                pygame.draw.rect(screen,BRANCO,[951,56,18,cont],0)
                cont += 0.1
                print cont
            else:
                if fim_de_jogo(True):
                   jogar(True)
            
            pygame.display.update()
             
            carrorect = carro.rect_carro
            objetorect =  objeto.rect_objeto
            combrect = comb.rect_comb
            
            if carrorect.colliderect(objetorect):
                if fim_de_jogo(True):
                    jogar(True)
            if comb.rect_comb.colliderect(carro.rect_carro):
                print "Pegou Comb" 
                Comb = 1000
                mostrar_comb = False
                cont = 21
                fonte = pygame.font.Font('fontes' + os.sep + 'nextwaveboldital.ttf',50)
                texto_gasolina = fonte.render("FUEL",True,PRETO)
                screen.blit(texto_gasolina,[910,10])

                pygame.draw.rect(screen,PRETO,[950,55,20,100],3)
                pygame.draw.rect(screen,VERMELHO,[951,56,18,98],0)
                pygame.draw.rect(screen,BRANCO,[951,56,18,cont],0)
            
            for j in range(len(arvores_direita)):
                arvores_direita[j].mover_arvores('direita')
                arvores_esquerda[j].mover_arvores('esquerda')
                faixas[j].mover_faixa()
                objeto.mover_objeto()
                if print_comb == True:
                    print_comb = comb.mover_comb(print_comb)
                
    
            print carrorect, objetorect
            
            if comb.rect_comb.colliderect(carro.rect_carro):
                    print "Bateu"   
           
            i += 1 
            combustivel -= 1


jogar(True)
