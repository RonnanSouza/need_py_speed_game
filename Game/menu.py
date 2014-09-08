# coding: utf-8

import pygame, os, sys, time, pickle
from pygame import *
from pygame import mixer
pygame.init()

# Intrudução do jogo
def introducao_jogo():
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
    ufcg = pygame.image.load('imagens' + os.sep + 'logo_ufcg.png').convert()
    cc = pygame.image.load('imagens' + os.sep + 'logo_computacao.jpg').convert()
    logo_jogo = pygame.image.load('imagens' + os.sep + 'logo_jogo.jpg').convert()
    
    # Carregando Fonte Inicio
    fonte = pygame.font.Font('fontes' + os.sep + 'btseps2.TTF',200)
    texto_apresentacao = fonte.render("Py Game",True,CINZA)
    # Sequencias de imagens
    tela.fill(BRANCO)
    tela.blit(ufcg, posicao_imagem_inicio(ufcg, tam_tela))
    pygame.display.update()
    time.sleep(5)
    
    tela.fill(BRANCO)
    tela.blit(cc, posicao_imagem_inicio(cc, tam_tela))
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

# Menu reset
def menu_reset():   
    while True:
        '''menu = pygame.image.load('imagens' + os.sep + 'janela_apagar.jpg')
        tela.blit(menu, [512,0])'''
        pygame.draw.rect(tela,PRETO,[162,234,700,250],0)
        
        fonte_menu1 = pygame.font.Font('fontes' + os.sep + 'Staubach.ttf',40)
        fonte_menu2 = pygame.font.Font('fontes' + os.sep + 'Staubach.ttf',40)

        texto1 = fonte_menu1.render('SEU RECORDE SERA APAGADO',True,AZUL)
        texto2 = fonte_menu1.render('TEM CERTEZA QUE DESEJA CONTINUAR?',True,AZUL)
        texto3 = fonte_menu2.render('SIM',True,AZUL)
        texto4 = fonte_menu2.render('NAO',True,AZUL)
        
        tela.blit(texto1,[(largura_tela / 2) - (texto1.get_size()[0] / 2), 250])
        tela.blit(texto2,[(largura_tela / 2) - (texto2.get_size()[0] / 2), 300])
        tela.blit(texto3,[400, 384])
        tela.blit(texto4,[550, 384])
        
        if posicao_fonte(texto3, [400, 384]):
          tela.blit(fonte_menu2.render('SIM',True, VERMELHO), [400, 384])
        elif posicao_fonte(texto4, [550, 384]) or pygame.key.get_pressed()[K_ESCAPE]:
          tela.blit(fonte_menu2.render('NAO',True, VERMELHO), [550, 384])
          
        for event in pygame.event.get():
            if (pygame.mouse.get_pressed()[0] and posicao_fonte(texto3, [400, 384])):
                with open('salve_recordes' + os.sep + 'save_record.dat', 'wb') as f:
                    pickle.dump(0, f)
                return True
            elif (pygame.mouse.get_pressed()[0] and posicao_fonte(texto4, [550, 384])) or pygame.key.get_pressed()[K_ESCAPE]:
                return True
            elif event.type == pygame.QUIT:
                sys.exit()
                      
        pygame.display.update()
# Menu recorde
def menu_recorde():
    # Carregando Recorde
    with open('salve_recordes' + os.sep + 'save_record.dat', 'rb') as f:
        record = pickle.load(f)
        
    while True:
        menu = pygame.image.load('imagens' + os.sep + 'menu_recorde.jpg')
        tela.blit(menu, [0,0])
        fonte_menu1 = pygame.font.Font('fontes' + os.sep + 'Staubach.ttf',70)
        fonte_menu2 = pygame.font.Font('fontes' + os.sep + 'Staubach.ttf',50)

        texto1 = fonte_menu1.render('RECORDE',True,LARANJA)
        texto2 = fonte_menu2.render('MELHOR  SCORE  =  %d' % record,True,LARANJA)
        texto3 = fonte_menu1.render('VOLTAR',True,LARANJA)
        
        tela.blit(texto1,[(largura_tela / 2) - (texto1.get_size()[0] / 2), 20])
        tela.blit(texto2,[20, 200])
        tela.blit(texto3,[750, 650])
        
        if posicao_fonte(texto3, [750,650]) or pygame.key.get_pressed()[K_ESCAPE]:
          tela.blit(fonte_menu1.render('VOLTAR',True, VERMELHO), [750,650])
          
        for event in pygame.event.get():
            if (pygame.mouse.get_pressed()[0] and posicao_fonte(texto3, [750,650])) or pygame.key.get_pressed()[K_ESCAPE]:
              return True
            elif event.type == pygame.QUIT:
              sys.exit()
                      
        pygame.display.update()
# Menu Creditos   
def menu_creditos():
    while True:
        menu = pygame.image.load('imagens' + os.sep + 'fundo_menu4.jpg')
        tela.blit(menu, [0,0])
        fonte_menu3 = pygame.font.Font('fontes' + os.sep + 'TURNBB__.TTF',50)
        fonte_menu4 = pygame.font.Font('fontes' + os.sep + 'TURNBB__.TTF',35)
        
        texto1 = fonte_menu3.render('CREDITOS',True,LARANJA)
        texto2 = fonte_menu4.render('DESEMVOLVEDORES:',True,LARANJA)
        texto3 = fonte_menu4.render('NATAN MACENA RIBEIRO',True,LARANJA)
        texto4 = fonte_menu4.render('RONAN DE ARAUJO SOUZA',True,LARANJA)
        texto5 = fonte_menu4.render('AGRADECIMENTOS:',True,LARANJA)
        texto6 = fonte_menu4.render('Luiz Augusto Morais',True,LARANJA)
        texto7 = fonte_menu4.render('Dalton Dario Serey Guerrero',True,LARANJA)
        texto8 = fonte_menu4.render('Jorge Cesar A. de Figueiredo',True,LARANJA)
        texto9 = fonte_menu3.render('VOLTAR',True,LARANJA)
        
        tela.blit(texto1,[(largura_tela / 2) - (texto1.get_size()[0] / 2), 30])
        tela.blit(texto2,[40, 150])
        tela.blit(texto3,[60, 250])
        tela.blit(texto4,[60, 300])
        tela.blit(texto5,[40, 400])
        tela.blit(texto6,[60, 500])
        tela.blit(texto7,[60, 550])
        tela.blit(texto8,[60, 600])
        tela.blit(texto9,[750, 700])
        
        if posicao_fonte(texto9, [750,700]) or pygame.key.get_pressed()[K_ESCAPE]:
          tela.blit(fonte_menu3.render('VOLTAR',True, VERMELHO), [750,700])
          
        for event in pygame.event.get():
            if (pygame.mouse.get_pressed()[0] and posicao_fonte(texto9, [750,700])) or pygame.key.get_pressed()[K_ESCAPE]:
              return True
            elif event.type == pygame.QUIT:
              sys.exit()
        
        pygame.display.update()

# Menu Ajuda
def menu_ajuda():
    while True:
        menu = pygame.image.load('imagens' + os.sep + 'menu_ajuda.jpg')
        tecla1 = pygame.image.load('imagens' + os.sep + 'computer_key_Arrow_Left.png')
        tecla2 = pygame.image.load('imagens' + os.sep + 'computer_key_Arrow_Right.png')
        tecla3 = pygame.image.load('imagens' + os.sep + 'computer_key_Esc.png')
        
        
        tela.blit(menu, [0,0])
        tela.blit(pygame.transform.scale(tecla1, [50,50]), [20,480])
        tela.blit(pygame.transform.scale(tecla2, [50,50]), [80,480])
        tela.blit(pygame.transform.scale(tecla3, [50,50]), [20,550])
        
        fonte_menu3 = pygame.font.Font('fontes' + os.sep + 'Staubach.ttf',65)
        fonte_menu4 = pygame.font.Font('fontes' + os.sep + 'Staubach.ttf',50)
        
        texto1 = fonte_menu3.render('AJUDA',True,LARANJA_2)
        
        texto2 = fonte_menu4.render('O que fazer?',True,LARANJA)
        texto3 = fonte_menu4.render('Voce tera que desviar dos carros que',True,LARANJA)
        texto4 = fonte_menu4.render('estao na contra mao, alem de manter',True,LARANJA)
        texto5 = fonte_menu4.render('o tanque abastecido coletando as',True,LARANJA)
        texto6 = fonte_menu4.render('gasolinas que estao no caminho.',True,LARANJA)
        
        texto7 = fonte_menu4.render('Acoes do Jogo:',True,LARANJA)
        texto8 = fonte_menu4.render('Mivimentar carro (ESQUER / DIREI)',True,LARANJA)
        texto9 = fonte_menu4.render('Pausar / Voltar',True,LARANJA)
        
        
        texto10 = fonte_menu3.render('VOLTAR',True,LARANJA_2)
        
        tela.blit(texto1,[(largura_tela / 2) - (texto1.get_size()[0] / 2), 10])
        tela.blit(texto2,[20, 100])
        tela.blit(texto3,[40, 170])
        tela.blit(texto4,[40, 220])
        tela.blit(texto5,[40, 270])
        tela.blit(texto6,[40, 320])
        
        tela.blit(texto7,[20, 390])
        tela.blit(texto8,[150, 460])
        tela.blit(texto9,[150, 530])
        
        tela.blit(texto10,[730, 630])
        
        if posicao_fonte(texto10, [730,630]) or pygame.key.get_pressed()[K_ESCAPE]:
          tela.blit(fonte_menu3.render('VOLTAR',True, BRANCO), [730,630])
          
        for event in pygame.event.get():
            if (pygame.mouse.get_pressed()[0] and posicao_fonte(texto9, [730,630])) or pygame.key.get_pressed()[K_ESCAPE]:
              return True
            elif event.type == pygame.QUIT:
              sys.exit()
        
        pygame.display.update()

# Menu Sair
def menu_sair():
    escape = 0
    while True:
        fonte_sair = pygame.font.Font('fontes' + os.sep + 'Staubach.ttf',70)
        
        texto_sair = fonte_sair.render("Ir voltar para o Menu?",True,VERMELHO)
        
        sub_texto_sair1 = fonte_sair.render("Sim",True,VERMELHO)
        sub_texto_sair2 = fonte_sair.render("Continuar Jogando",True,VERMELHO)
        
        tela.blit(texto_sair, [(512 - texto_sair.get_size()[0] / 2),200])
        tela.blit(sub_texto_sair1, [120,300])
        tela.blit(sub_texto_sair2, [330,300])
        
        if posicao_fonte(sub_texto_sair1, [120,300]):
            tela.blit(fonte_sair.render("Sim",True,CINZA),[120,300])
        elif posicao_fonte(sub_texto_sair2, [330,300]):
            tela.blit(fonte_sair.render("Continuar Jogando",True,CINZA),[330,300])
            
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_sair1, [120,300]):
                return True
            elif pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_sair2, [330,300]):
                return False
            if pygame.key.get_pressed()[K_ESCAPE] and escape > 10:
                return False
                    
        pygame.display.update()
        escape += 1

# Game Over
def fim_de_jogo(score):
    score = int(score)
    imprima_record = False
    
    # Carregando recorde
    with open('salve_recordes' + os.sep + 'save_record.dat', 'rb') as f:
        record = pickle.load(f)
    
    if score > record:
        record = score
        print record
        # Salvando record
        with open('salve_recordes' + os.sep + 'save_record.dat', 'wb') as f:
            pickle.dump(score, f)
            ''', protocol=2)'''
            imprima_record = True
    
            fonte_record = pygame.font.Font('fontes' + os.sep + 'nextwaveboldital.ttf',90)
            texto_record = fonte_record.render("NEW RECORD",True,LARANJA_2)
            texto_score = fonte_record.render("%d" % record,True,LARANJA_2)
    
    while True:
        fonte_fim = pygame.font.Font('fontes' + os.sep + 'JUSTFIST2.ttf',70)
        texto_fim = fonte_fim.render("GAME OVER",True,VERMELHO)
        
        tela.blit(texto_fim, [(1024 / 2) - (texto_fim.get_size()[0] / 2), 200])
        if imprima_record:
            tela.blit(texto_record, [(1024 / 2) - (texto_record.get_size()[0] / 2), 300])
            tela.blit(texto_score, [(1024 / 2) - (texto_score.get_size()[0] / 2), 350])
        
        pygame.display.update()
        pygame.time.delay(5000)
        return True
        
# Menu Principal
def menu_raiz():
    # Carregando fontes
    fonte_menu = pygame.font.Font('fontes' + os.sep + 'Mostwasted.ttf',70)
    fonte_menu2 = pygame.font.Font('fontes' + os.sep + 'Mostwasted.ttf',65)
    
    texto_menu = fonte_menu.render("Need Py Speed",True,AMARELO)
    
    sub_texto_menu1 = fonte_menu2.render("Jogar",True,AMARELO)
    sub_texto_menu2 = fonte_menu2.render("Ajuda",True,AMARELO)
    sub_texto_menu3 = fonte_menu2.render("Recorde",True,AMARELO)
    sub_texto_menu4 = fonte_menu2.render("Creditos",True,AMARELO)
    sub_texto_menu5 = fonte_menu2.render("Reset Recorde",True,AMARELO)
    sub_texto_menu6 = fonte_menu2.render("Sair",True,AMARELO)
    
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
        tela.blit(sub_texto_menu4, [40,450])
        tela.blit(sub_texto_menu5, [40,550])
        tela.blit(sub_texto_menu6, [40,650])
        
        if posicao_fonte(sub_texto_menu1, [40,150]):
          mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
          pygame.mixer.init()
          s = pygame.mixer.Sound('abrindo_porta.wav')
          s.play()
          tela.blit(fonte_menu2.render("Jogar",True, VERMELHO), [40,150])
        elif posicao_fonte(sub_texto_menu2, [40,250]):
          tela.blit(fonte_menu2.render("Ajuda",True,VERMELHO),[40,250])
        elif posicao_fonte(sub_texto_menu3, [40,350]):
          tela.blit(fonte_menu2.render("Recorde",True,VERMELHO),[40,350])
        elif posicao_fonte(sub_texto_menu4, [40,450]):
          tela.blit(fonte_menu2.render("Creditos",True,VERMELHO),[40,450])
        elif posicao_fonte(sub_texto_menu5, [40,550]):
          tela.blit(fonte_menu2.render("Reset Recorde",True,VERMELHO),[40,550])
        elif posicao_fonte(sub_texto_menu6, [40,650]):
          tela.blit(fonte_menu2.render("Sair",True,VERMELHO),[40,650])
        
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_menu1, [40,150]):
              pygame.mixer.music.stop()
              return True
            elif pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_menu2, [40,250]):
                if menu_ajuda():
                    continue
            elif pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_menu3, [40,350]):
                if menu_recorde():
                    continue            
            elif pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_menu4, [40,450]):
                if menu_creditos():
                    continue
            elif pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_menu5, [40,550]):
                if menu_reset():
                    continue
            elif pygame.mouse.get_pressed()[0] and posicao_fonte(sub_texto_menu6, [40,650]):
              sys.exit()
            elif event.type == pygame.QUIT:
              sys.exit()
        
        pygame.display.update()
        
        
# Configurando Tela
tam_tela = largura_tela, altura_leta = (1024, 768)
tela = pygame.display.set_mode(tam_tela)
pygame.display.set_caption('Need Py Speed - The Game')

# Carregando cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
LARANJA = (255, 165, 0)
LARANJA_2 = (251, 79, 12)
VERMELHO = (255, 0, 0)
VERDE = (0, 128, 0)
AZUL = (51, 181, 205)
CINZA = (128, 128, 128)
BRANCO = (255, 255, 255)
