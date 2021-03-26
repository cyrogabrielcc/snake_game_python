import pygame
import sys
from cobrinha import Cobra
from comida import Comida
import time

temp = pygame.time.Clock()

frames = 12

pygame.font.init()
fonte = pygame.font.SysFont('Arial', 20)

#iniciar o jogo
pygame.init()
TAM_TELA = (300,400)     
tela = pygame.display.set_mode(TAM_TELA)

points = 0;


cobra = Cobra()
comida = Comida()
posicao_comida = comida.posicao



while True:

    tela.fill((7,0,35)) #rgb

    for event in pygame.event.get():
        #listener - mouse ou teclado
        if event.type == pygame.QUIT:
            #interromper o pygame
            pygame.quit()
            #sair do JOGO
            sys.exit()

        #Se uma tecla for pressionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                 cobra.muda_direcao('DIREITA')
            if event.key == pygame.K_UP:
                 cobra.muda_direcao('CIMA')
            if event.key == pygame.K_DOWN:
                 cobra.muda_direcao('BAIXO')
            if event.key == pygame.K_LEFT:
                 cobra.muda_direcao('ESQUERDA')

    posicao_comida = comida.gera_nova_comida()

    if cobra.move(posicao_comida):
        comida.devorada = True
        frames += 2
        points += 1 

    if cobra.verifica_colisao():
        perdeu = fonte.render('PERRRDEU!', True, (255,255,255))
        tela.blit(perdeu, (80, 180))
        
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        sys.exit()

    #pontos
    pontos = fonte.render(f'Pontuação: {points}', True, (255,255,255))
    tela.blit(pontos, (10,10))


    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(255, 204, 0),
                               pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(tela, pygame.Color(255, 0, 0),
                     pygame.Rect(posicao_comida[0], posicao_comida[1], 10, 10))

    pygame.display.update()
    
    temp.tick(frames)






