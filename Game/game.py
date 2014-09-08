# coding : utf-8

import pygame, os, sys, time
from pygame import *
from faixa import *
from carro import *
from arvores import *
from menu import *
from objetos_pista import *
from combustivel import *
from pygame import mixer
mixer.init()

pygame.init()

# Carregando intro do jogo
#introducao_jogo()

# Menu Raiz
def jogar():
    record = 0
    if menu_raiz():
        tela =  pygame.display.set_mode((1024, 768))
        screen = pygame.display.get_surface()
        fundo = pygame.image.load('imagens' + os.sep + 'road.png')
        pygame.display.set_caption('Need Py Speed - The Game')
        
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
        
        cont_gasolina = 1
        cont_score = 0
        cont_exibir = 15
        bateu = False
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
                elif pygame.key.get_pressed()[K_ESCAPE]:
                    if menu_sair():
                        jogar()
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
            
            # Score
            fonte = pygame.font.Font('fontes' + os.sep + 'nextwaveboldital.ttf',55)
            texto_score = fonte.render("Score",True,PRETO)
            
            score = cont_score * 10
            texto_valor_score = fonte.render("%d" % score,True,PRETO)
            
            screen.blit(texto_score,[370,15])
            screen.blit(texto_valor_score,[540,15])
            
            if int(score) % 600 == 0 and score > 0 and int(score) % 1000 != 0:
                cont_score += 2.0
                cont_exibir = 0
                bonus = 2
                cor_font = LARANJA
                bateu = False
                        
            if int(score) % 1000 == 0 and score > 0:
                cont_score += 5.0
                cont_exibir = 0
                bonus = 5
                cor_font = LARANJA_2
                bateu = False
                
            if cont_exibir < 15:
                fonte = pygame.font.Font('fontes' + os.sep + 'nextwaveboldital.ttf',75)
                texto_good = fonte.render("+ %d0 BONUS" % bonus,True,cor_font)
                
                screen.blit(texto_good,[320,80])
                cont_exibir += 1
            ##
            
            # Gasolina
            if cont_gasolina < 96:
                fonte = pygame.font.Font('fontes' + os.sep + 'nextwaveboldital.ttf',50)
                texto_gasolina = fonte.render("FUEL",True,PRETO)
                screen.blit(texto_gasolina,[910,10])
                
                pygame.draw.rect(screen,PRETO,[950,55,20,100],3)
                pygame.draw.rect(screen,VERMELHO,[952,57,16,96],0)
                pygame.draw.rect(screen,BRANCO,[952,57,16,cont_gasolina],0)
                cont_gasolina += 0.1
            else:
                if fim_de_jogo(score):
                   jogar()
            ##
            
            pygame.display.update()
             
            carrorect = carro.rect_carro
            objetorect =  objeto.rect_objeto
            combrect = comb.rect_comb
            
            if carrorect.colliderect(objetorect):
                if fim_de_jogo(score):
                    jogar()
            if comb.rect_comb.colliderect(carro.rect_carro):
                print "Pegou Comb" 
                Comb = 1000
                mostrar_comb = False
                cont_gasolina = 1
                cont_exibir = 0
                bateu = True
            if cont_exibir < 15 and bateu:
                cont_score += 1.0
                bonus = 1
                cor_font = AMARELO
            
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
            cont_score += 0.1

# Iniciar Jogo
jogar()
