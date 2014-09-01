# coding : utf-8

import pygame, os, sys, time
from pygame import *

def introducao_jogo(sim):
    import time
    def posicao_imagem_inicio(imagem, tam_tela):
      largura_imagem , altura_imagem = imagem.get_size()
      largura, altura = tam_tela
      
      return [(largura / 2) - (largura_imagem / 2),(altura / 2) - (altura_imagem / 2)]
    
    # Carregando sons
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.music.load('musicas' + os.sep + 'Tema_PS2.mp3')
    pygame.mixer.music.play(1)
    
    # Carregando imagens
    ufcg = pygame.image.load('imagens' + os.sep + 'imagem10.png').convert()
    ccc = pygame.image.load('imagens' + os.sep + 'imagem11.jpg').convert()
    logo_jogo = pygame.image.load('imagens' + os.sep + 'imagem6.jpg').convert()
    
    # Carregando Fonte Inicio
    fonte = pygame.font.Font('fontes' + os.sep + 'btseps2.TTF',200)
    texto_apresentacao = fonte.render("Py Game",True,CINZA)
    # Sequencias de imagens
    tela.fill(BRANCO)
    tela.blit(ufcg, posicao_imagem_inicio(ufcg, tam_tela))
    pygame.display.update()
    time.sleep(5)
    
    tela.fill(BRANCO)
    tela.blit(ccc, posicao_imagem_inicio(ccc, tam_tela))
    pygame.display.update()
    time.sleep(6)
    
    tela.fill(PRETO)
    tela.blit(logo_jogo, posicao_imagem_inicio(logo_jogo, tam_tela))
    pygame.display.update()
    time.sleep(5.5)
    
    tela.fill(PRETO)
    tela.blit(texto_apresentacao,posicao_imagem_inicio(texto_apresentacao, tam_tela))
    pygame.display.update()
    time.sleep(2)
   
def posicao_fonte(imagem, pos_inicial):
    x, y = pygame.mouse.get_pos()
    largura, altura = imagem.get_size()
    x_imagem = pos_inicial[0]
    y_imagem = pos_inicial[1]
    if x >= x_imagem and x <= x_imagem + largura and y >= y_imagem and y <= y_imagem + altura:
        return True
    return False
      
def menu_creditos(sim):
    while True:
        menu = pygame.image.load('imagens' + os.sep + 'fundo_menu4.jpg')
        tela.blit(menu, [0,0])
        fonte_menu3 = pygame.font.Font('fontes' + os.sep + 'TURNBB__.TTF',50)
        fonte_menu4 = pygame.font.Font('fontes' + os.sep + 'TURNBB__.TTF',35)
        
        texto1 = fonte_menu3.render('CREDITOS',True,VERDE)
        texto2 = fonte_menu4.render('DESEMVOLVEDORES:',True,VERDE)
        texto3 = fonte_menu4.render('NATAN MACENA RIBEIRO',True,VERDE)
        texto4 = fonte_menu4.render('RONAN DE ARAUJO SOUZA',True,VERDE)
        texto5 = fonte_menu4.render('AGRADECIMENTOS:',True,VERDE)
        texto6 = fonte_menu4.render('LUIZ',True,VERDE)
        texto7 = fonte_menu4.render('DALTON',True,VERDE)
        texto8 = fonte_menu4.render('JORGE',True,VERDE)
        texto9 = fonte_menu3.render('VOLTAR',True,VERDE)
        
        tela.blit(texto1,[(largura_tela / 2) - (texto1.get_size()[0] / 2), 30])
        tela.blit(texto2,[40, 150])
        tela.blit(texto3,[60, 250])
        tela.blit(texto4,[60, 300])
        tela.blit(texto5,[40, 400])
        tela.blit(texto6,[60, 500])
        tela.blit(texto7,[60, 550])
        tela.blit(texto8,[60, 600])
        tela.blit(texto9,[700, 700])
        
        if posicao_fonte(texto9, [700,700]):
          tela.blit(fonte_menu3.render('VOLTAR',True, VERMELHO), [700,700])
          
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] and posicao_fonte(texto9, [700,700]):
              return True
            elif event.type == pygame.QUIT:
              sys.exit()
        
        pygame.display.update()
    
def menu_raiz(sim):
    # Carregando fontes
    fonte_menu = pygame.font.Font('fontes' + os.sep + 'Mostwasted.ttf',70)
    fonte_menu2 = pygame.font.Font('fontes' + os.sep + 'Mostwasted.ttf',65)
    
    texto_menu = fonte_menu.render("Need Py Speed",True,AMARELO)
    
    sub_texto_menu1 = fonte_menu2.render("Jogar",True,AMARELO)
    sub_texto_menu2 = fonte_menu2.render("Creditos",True,AMARELO)
    sub_texto_menu3 = fonte_menu2.render("Sair",True,AMARELO)
    # Som do menu
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.music.load('musicas' + os.sep + 'som_menu.mp3')
    pygame.mixer.music.play(-1)
    
    while True:
        menu = pygame.image.load('imagens' + os.sep + 'fundo_menu.jpg')
        # Imagem do menu
        tela.blit(menu, [0,0])
        
        tela.blit(texto_menu, [(largura_tela / 2) - (texto_menu.get_size()[0] / 2), 30])
        tela.blit(sub_texto_menu1, [40,150])
        tela.blit(sub_texto_menu2, [40,250])
        tela.blit(sub_texto_menu3, [40,350])
        
        if posicao_fonte(sub_texto_menu1, [40,150]):
          tela.blit(fonte_menu2.render("Jogar",True, VERMELHO), [40,150])
        elif posicao_fonte(sub_texto_menu2, [40,250]):
          tela.blit(fonte_menu2.render("Creditos",True,VERMELHO),[40,250])
        elif posicao_fonte(sub_texto_menu3, [40,350]):
          tela.blit(fonte_menu2.render("Sair",True,VERMELHO),[40,350])
        
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_menu1, [40,150]):
              pygame.mixer.music.stop()
              return True
            elif pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_menu2, [40,250]):
                if menu_creditos(True):
                    continue
            elif pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_menu3, [40,350]):
              sys.exit()
            elif event.type == pygame.QUIT:
              sys.exit()
            elif pygame.key.get_pressed()[K_ESCAPE]:    
              sys.exit()
        
        pygame.display.update()
        
        
# Configurando Tela
tam_tela = largura_tela, altura_leta = (1024, 768)
tela = pygame.display.set_mode(tam_tela)
pygame.display.set_caption('Need Py Speed - The Game')

# Carregando cores
PRETO = (0, 0, 0)
VERDE = (173, 216, 230)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
CINZA = (128, 128, 128)
BRANCO = (255, 255, 255)
