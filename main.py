import pygame
import sys

import interface
import busca_cega
import busca_A


WHITE = (255, 255, 255)


pygame.init() # initializing the constructor
res = (1000,700) # screen resolution
screen = pygame.display.set_mode(res)
grid=[]
screen = pygame.display.set_mode((1000,700))
background = pygame.image.load('imagens_e_fontes/labirinto3.jpg')
screen.fill((0,0,0))
screen.blit(background, (0, 0))


def main(screen):
    mostra_botoes=0
    solucao=0
    entrada_botao=interface.botao(screen, [10,10,160,40], "arquivo de entrada" , [15,20])
   
    while True: 

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                Run = False
        #checks if a mouse is clicked
        if entrada_botao.click():
            matriz=interface.open_file()
            if(matriz != 0):    
                rect = pygame.Rect(10, 160, 150, 190)
                pygame.draw.rect(screen,WHITE, rect)
                entrada=matriz[0]
                saida=matriz[1]
                del matriz[0:2]
                print(entrada,saida)
                print(len(matriz))
                screen.fill(WHITE)
                grid=interface.cria_grid(screen, len(matriz))                        
                interface.Pinta_Grid(matriz, grid)
                mostra_botoes=1
        
        if mostra_botoes==1:
            busca_a_botao=interface.botao(screen, [10,60,160,40], "Busca A*" , [15,70]) 
            busca_cega_botao=interface.botao(screen, [10,110,160,40], "Busca Cega" , [15,120])

            if busca_cega_botao.click(): #busca cega
                rect = pygame.Rect(10, 160, 150, 190)
                pygame.draw.rect(screen,WHITE, rect)
                interface.Pinta_Grid(matriz, grid)
                solucao=busca_cega.busca_custo_uniforme(entrada,saida, matriz, grid)
                print(solucao)
                custo_total = solucao[0]
                numero_nos_visitados = solucao[-1]
                del solucao[0]
                del solucao[-1]
                interface.Pinta_solucao(grid, solucao)
                interface.custos(screen, custo_total, numero_nos_visitados, "Busca Cega", entrada, saida)
                pygame.display.update()
            
            if  busca_a_botao.click(): #botao de a*
                rect = pygame.Rect(10, 160, 150, 190)
                pygame.draw.rect(screen,WHITE, rect)
                interface.Pinta_Grid(matriz, grid)
                solucao=busca_A.func_busca_A(entrada,saida, matriz, grid)                  
                print(solucao)
                custo_total = solucao[1]
                numero_nos_visitados = solucao[-1]
                del solucao[0]
                del solucao[0]
                del solucao[-1]
                interface.Pinta_solucao(grid,solucao)
                interface.custos(screen, custo_total, numero_nos_visitados, "Busca A*", entrada, saida)
                pygame.display.update()
        
        entrada_botao=interface.botao(screen, [10,10,160,40], "arquivo de entrada" , [15,20])
        pygame.display.update()



