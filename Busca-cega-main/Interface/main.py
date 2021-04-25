import pygame
import sys
import time
from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import interface
import busca_cega

color_light = (170,170,170)# light shade of the button
color_dark = (100,100,100) # dark shade of the button

RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 40, 0)
DARK_BLUE = (0, 0, 40)
DARK_RED = (120, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
MARROM = (75, 54, 33)
MARROM_ESCURO = (36,0,0)

pygame.init() # initializing the constructor
res = (0,0) # screen resolution
screen = pygame.display.set_mode(res,pygame.RESIZABLE)# opens up a window
screen.fill(WHITE) #pinta tela de branco
def main(screen):
    mostra_botoes=0
    solucao=0
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= mouse[0] <= 10+140 and 10 <= mouse[1] <= 10+40:
                    matriz=interface.open_file()
                    if(matriz != 0):    
                        entrada=matriz[0]
                        saida=matriz[1]
                        del matriz[0:2]
                        print(entrada,saida)
                        print(len(matriz))
                        flag=1
                        screen.fill(WHITE)
                        interface.cria_grid(screen, len(matriz))
                        interface.Pinta_Grid(screen, matriz)
                        mostra_botoes=1
            
            if mostra_botoes==1:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if 10 <= mouse[0] <= 10+140 and 60 <= mouse[1] <= 60+40: 
                        #FAZ ALGO
                        x=0
                    if 10 <= mouse[0] <= 10+140 and 110 <= mouse[1] <= 110+40: #busca cega
                        solucao=busca_cega.busca_custo_uniforme(entrada,saida, matriz, screen)
                        print(solucao)
                        custo_total = solucao[0]
                        del solucao[0]
                        print(solucao)
                        interface.Pinta_solucao(screen, matriz, solucao, 0)
                        pygame.display.update()
                    
        # fills the screen with a color
        
       
        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade 

        
        if 10 <= mouse[0] <= 10+140 and 10 <= mouse[1] <= 10+40: # botao de entrada
            interface.botao(screen, color_light, [10,10,140,40], "arquivo de entrada" , [15,20]) 
        else:
            interface.botao(screen, color_dark, [10,10,140,40], "arquivo de entrada" , [15,20])
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

main(screen)