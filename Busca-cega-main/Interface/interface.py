import pygame
import sys
import time
from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename

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

class botao: #classe botão
    def __init__(self, tela, color, pos_tam, texto, pos_tex): #construtor recebe a tela e sua cor
        self.tela=tela
        self.color=color
        smallfont = pygame.font.SysFont('Corbel',20) # configura texto
        text = smallfont.render(texto , True , WHITE)
        pygame.draw.rect(self.tela,self.color, pos_tam )  
        self.tela.blit(text , pos_tex )
  
def open_file():  #função para abrir e ler arquivo e retorna a matriz de dados
    matriz=0
    root=Tk()
    root.filename = askopenfilename() #
    root.destroy()
    name_file=root.filename
    try:
        with open(name_file, 'r') as arquivo:
            matriz = [[int(num) for num in line.split(',')] for line in arquivo]
        arquivo.close()
    except TypeError:
        print("O arquivo não foi aberto")
        matriz=0
    except FileNotFoundError:
        print("O arquivo não foi aberto")
        matriz=0
    return matriz

def cria_grid(tela, tamanho_matriz): #cria o grind, recebe a tela onde sera criado e o tamanho da matriz
    blockSize = 700/tamanho_matriz #Set the size of the grid block
    for x in range(tamanho_matriz):
        for y in range(tamanho_matriz):
            rect = pygame.Rect(int(blockSize)*x+300, int(blockSize)*y+20, int(blockSize), int(blockSize))
            pygame.draw.rect(tela, BLACK, rect, 1)
            

def Pinta_Grid(tela, matriz): #pinta o grid feito, recebe a tela e a matriz
    #screen.fill(WHITE)
    blockSize = (700/len(matriz))#Set the size of the grid block
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            if x==0 and y==0:
                rect = pygame.Rect(int(blockSize)*x+301, int(blockSize)*y+21, int(blockSize)-2, int(blockSize)-2)
            
            elif x==0:
                rect = pygame.Rect(int(blockSize)*x+301, int(blockSize)*y+20, int(blockSize)-2, int(blockSize)-1)
            elif y==0:
                rect = pygame.Rect(int(blockSize)*x+300, int(blockSize)*y+21, int(blockSize)-1, int(blockSize)-2)
            else:
                rect = pygame.Rect(int(blockSize)*x+300, int(blockSize)*y+20, int(blockSize)-1, int(blockSize)-1)
            if matriz[y][x] == 1:
                pygame.draw.rect(tela, GREEN, rect)
            elif matriz[y][x] == 2:
                pygame.draw.rect(tela, MARROM, rect )
            elif matriz[y][x] == 3: 
                pygame.draw.rect(tela, BLUE, rect )
            elif matriz[y][x] == 4: 
                pygame.draw.rect(tela, RED, rect)

def Pinta_borda(tela, matriz, p, flag):
    blockSize = (700/len(matriz))#Set the size of the grid block
    if p[0]==0 and p[1]==0:
        rect = pygame.Rect(int(blockSize)*p[0]+301, int(blockSize)*p[1]+21, int(blockSize)-2, int(blockSize)-2)
    elif p[0]==0:
        rect = pygame.Rect(int(blockSize)*p[0]+301, int(blockSize)*p[1]+20, int(blockSize)-2, int(blockSize)-1)
    elif p[1]==0:
        rect = pygame.Rect(int(blockSize)*p[0]+300, int(blockSize)*p[1]+21, int(blockSize)-1, int(blockSize)-2)
    else:
        rect = pygame.Rect(int(blockSize)*p[0]+300, int(blockSize)*p[1]+20, int(blockSize)-1, int(blockSize)-1)
    if flag==0:
        if matriz[p[1]][p[0]] == 1:
            pygame.draw.rect(tela, DARK_GREEN, rect)
        elif matriz[p[1]][p[0]] == 2:
            pygame.draw.rect(tela, MARROM_ESCURO, rect )
        elif matriz[p[1]][p[0]] == 3: 
            pygame.draw.rect(tela, DARK_BLUE, rect )
        elif matriz[p[1]][p[0]] == 4: 
            pygame.draw.rect(tela, DARK_RED, rect)
    else:
        pygame.draw.rect(tela, color_light, rect)
    pygame.display.update()
    time.sleep(0.01)
def Pinta_solucao(tela, matriz, solucao, flag): #pinta o grid feito, recebe a tela e a matriz
    #screen.fill(WHITE)
    
    blockSize = (700/len(matriz))#Set the size of the grid block
    for p in solucao:
        if p[0]==0 and p[1]==0:
                rect = pygame.Rect(int(blockSize)*p[0]+301, int(blockSize)*p[1]+21, int(blockSize)-2, int(blockSize)-2)
        elif p[0]==0:
            rect = pygame.Rect(int(blockSize)*p[0]+301, int(blockSize)*p[1]+20, int(blockSize)-2, int(blockSize)-1)
        elif p[1]==0:
            rect = pygame.Rect(int(blockSize)*p[0]+300, int(blockSize)*p[1]+21, int(blockSize)-1, int(blockSize)-2)
        else:
            rect = pygame.Rect(int(blockSize)*p[0]+300, int(blockSize)*p[1]+20, int(blockSize)-1, int(blockSize)-1)
    
        time.sleep(0.15)
        pygame.draw.rect(tela, WHITE, rect)
        pygame.display.update()
        
   

