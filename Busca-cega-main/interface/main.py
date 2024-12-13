import pygame
import sys
import time
from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import interface
import busca_cega
import busca_A

color_light = (170,170,170)# light shade of the button
color_dark = (100,100,100) # dark shade of the button
WHITE = (255, 255, 255)


pygame.init() # initializing the constructor
res = (1000,800) # screen resolution
screen = pygame.display.set_mode(res)
grid=[]
screen = pygame.display.set_mode((1000,750))
background = pygame.image.load('labirinto2.jpg')
screen.fill((0,0,0))
screen.blit(background, (0, 0))
def main(screen):
    mostra_botoes=0
    solucao=0
    Run = True
    while Run:
        mouse = pygame.mouse.get_pos()
        flag=0
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                Run = False
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN and flag==0:
                if 10 <= mouse[0] <= 10+140 and 10 <= mouse[1] <= 10+40:
                    matriz=interface.open_file()
                    if(matriz != 0):    
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
                if 10 <= mouse[0] <= 10+140 and 110 <= mouse[1] <= 110+40 and pygame.mouse.get_pressed() == (1, 0, 0): #busca cega
                    interface.Pinta_Grid(matriz, grid)
                    mouse = pygame.mouse.get_pos()
                    flag=1
                    solucao=busca_cega.busca_custo_uniforme(entrada,saida, matriz, grid)
                    mouse = pygame.mouse.get_pos()
                    print(solucao)
                    custo_total = solucao[0]
                    del solucao[0]
                    interface.Pinta_solucao(grid, solucao)
                    pygame.display.update()
                if 10 <= mouse[0] <= 10+140 and 60 <= mouse[1] <= 60+40 and pygame.mouse.get_pressed() == (1, 0, 0): #botao de a*
                    interface.Pinta_Grid(matriz, grid)
                    flag=1
                    mouse = pygame.mouse.get_pos()
                    solucao=busca_A.func_busca_A(entrada,saida, matriz, grid)                  
                    print(solucao)
                    custo_total = solucao[1]
                    del solucao[0]
                    del solucao[0]
                    interface.Pinta_solucao(grid,solucao)
                    pygame.display.update()

        mouse = pygame.mouse.get_pos()

        flag=0
        if 10 <= mouse[0] <= 10+140 and 10 <= mouse[1] <= 10+40: # botao de entrada
            interface.botao(screen, color_light, [10,10,170,40], "Arquivo de entrada" , [15,20]) 
        else:
            interface.botao(screen, color_dark, [10,10,170,40], "Arquivo de entrada" , [15,20])
        
        if mostra_botoes==1:
            if 10 <= mouse[0] <= 10+140 and 60 <= mouse[1] <= 60+40: #botao de a*
                interface.botao(screen, color_light, [10,60,140,40], "Busca A*" , [15,70]) 
            else:
                interface.botao(screen, color_dark, [10,60,140,40], "Busca A*" , [15,70])

            if 10 <= mouse[0] <= 10+140 and 110 <= mouse[1] <= 110+40:
                interface.botao(screen, color_light, [10,110,140,40], "Busca Cega" , [15,120]) 
            else:
                interface.botao(screen, color_dark, [10,110,140,40], "Busca Cega" , [15,120])

        # updates the frames of the game
        pygame.display.update()

