# coding: utf-8

import pygame, os, sys, time
from bebida import *
from pygame import *
from menu import *
from faixa import *
from carro import *
from arvores import *
from objetos_pista import *
from combustivel import *
#from mensagens_jogo import *
#from efeitos_jogo import *

pygame.init()

# Carregando intro do jogo
#introducao_jogo()

# Menu Raiz
def jogar():
    record = 0
    if menu_raiz():
        pygame.mixer.music.load('musicas' + os.sep + 'Rally - song' + os.sep + random.choice(lista_musicas))
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
        print_comb = False
        mostrar_comb = False
        print_bebida = False
        mostrar_bebida = False
        bebida = Bebida(screen)
        cont_bebida = 0
        
        cont_gasolina = 1
        velocidade_carro = 20
        cont_score = 0
        cont_exibir = 15
        bateu = False
        
        # Musica de Fundo 
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        
        som = False
        while True:
            clock.tick(20)
            if i % 200 == 0 and i != 0:
                print_comb = True
                mostrar_comb = True
            # Fechar o game/ Pausar o game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif pygame.key.get_pressed()[K_ESCAPE]:
                    pygame.mixer.music.pause()
                    som_pausa.play(0)
                    if menu_sair():
                        jogar()
                    pygame.mixer.music.unpause()
            ##
            
            tecla = pygame.key.get_pressed()
            carro.mover_carro(tecla, velocidade_carro)
            if i % 250 == 0:
                mostrar_bebida = True
                print_bebida = True
                
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
            if mostrar_bebida == True:
                bebida.print_bebida(screen)

            carro.print_carro(screen)
            
            '''if cont_score < 5 and inicio_de_jogo():
                True'''
            if cont_gasolina > 70 and not som:
                som = True
                som_fuel.play(0)
            '''elif cont_gasolina < 96:
                som_fuel.stop()'''
            
            # Score
            fonte = pygame.font.Font('fontes' + os.sep + 'nextwaveboldital.ttf',55)
            texto_score = fonte.render("Score",True,PRETO)
            
            score = cont_score * 10
            texto_valor_score = fonte.render("%d" % score,True,PRETO)
            screen.blit(texto_score,[370,15])
            screen.blit(texto_valor_score,[540,15])
            
            if int(score) % 600 == 0 and score > 0 and int(score) % 1000 != 0:
                som_bonus.play(0)
                cont_score += 2.0
                cont_exibir = 0
                bonus = 2
                cor_font = LARANJA
                bateu = False
                        
            if int(score) % 1000 == 0 and score > 0:
                som_bonus.play(0)
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
                cont_gasolina += 0.25
            else:
                if fim_de_jogo(score):
                   jogar()
            ##
            
            pygame.display.update()
             
            carrorect = carro.rect_carro
            objetorect =  objeto.rect_objeto
            combrect = comb.rect_comb
            bebidarect = bebida.rect_comb

            
            if carrorect.colliderect(objetorect):
                pygame.mixer.music.stop()
                if fim_de_jogo(score):
                    jogar()
            if comb.rect_comb.colliderect(carro.rect_carro):
                som_bonus.play(0)
                mostrar_comb = False
                print cont_gasolina
                cont_gasolina = 1 
                cont_exibir = 0
                bateu = True

            if carrorect.colliderect(bebidarect):
                velocidade_carro = 10 
                cont_bebida = 0
                mostrar_bebida = False 

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
                if print_bebida == True:
                    print_bebida = bebida.mover_bebida(print_bebida)
                
    
            i += 1 
            cont_score += 0.1
            '''if inicio_de_jogo():
                continue'''
            if cont_bebida == 100:
                velocidade_carro = 20
            cont_bebida += 1
                

# Iniciar Jogo
jogar()
