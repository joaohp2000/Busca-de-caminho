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

class cubo: #classe botão
    def __init__(self, tela, tamanho, p, matriz): #construtor recebe a tela e sua cor
        self.tela=tela
        self.tamanho=tamanho
        self.p=p
        
        rect = pygame.Rect(self.tamanho*self.p[0]+300, self.tamanho*self.p[1]+20,self.tamanho-1, self.tamanho-1)
        rect2 = pygame.Rect(self.tamanho*self.p[0]+300, self.tamanho*self.p[1]+20,self.tamanho, self.tamanho)
      #  pygame.draw.rect(self.tela, BLUE, rect)
       # pygame.draw.rect(self.tela, BLACK, rect2, 1)
        
        x1=(tamanho*p[0]+299+tamanho)
        y1=(tamanho*p[1]+19+tamanho)
        x2=(tamanho*p[0]+296+tamanho)
        y2=(tamanho*p[1]+16+tamanho)
        x3=(tamanho*p[0]+300)
        y3=(tamanho*p[1]+23)
        x4=(tamanho*p[0]+303)
        y4=(tamanho*p[1]+20)
        
        
        
        
        pygame.draw.polygon(tela,BLACK,[(x1,y1),(x2,y2)],1)
        pygame.draw.polygon(tela,BLACK,[(x1,y4),(x2,y3)],1)

        pygame.draw.polygon(tela,BLACK,[(x3,y1),(x4,y2)],1)
        pygame.draw.polygon(tela,BLACK,[(x3,y4),(x4,y3)],1)
        #pygame.draw.polygon(screen,RED,[(x1,y1),(x2,y2),(x2-tamanho, y2),(x1-tamanho, y1)],0)

        #pygame.draw.polygon(screen,BLACK,[(x1,y1),(x2,y2),(x3,y3),(x4,y4)],1)
        #pygame.draw.polygon(screen,BLACK,[(x1,y1),(x2,y2),(x2-tamanho, y2),(x1-tamanho, y1)],1)
        
        
        rect2 = pygame.Rect(self.tamanho*self.p[0]+304, self.tamanho*self.p[1]+24,tamanho-8,tamanho-8)
        
        
        #pygame.draw.rect(tela,BLACK, (296, 16, 20,20), 1)
        if matriz[p[1]][p[0]] == 1:
            color=DARK_GREEN
        elif matriz[p[1]][p[0]] == 2:
            color=MARROM_ESCURO
        elif matriz[p[1]][p[0]] == 3: 
            color=DARK_BLUE
        elif matriz[p[1]][p[0]] == 4:
            color=DARK_RED
        pygame.draw.rect(tela, color, rect2)
        pygame.draw.rect(tela,BLACK, rect2, 1)

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
    rect2 = pygame.Rect(int(blockSize)*p[1]+300, int(blockSize)*p[0]+20, int(blockSize), int(blockSize))
    if p[0]==0 and p[1]==0:
        rect = pygame.Rect(int(blockSize)*p[1]+301, int(blockSize)*p[0]+21, int(blockSize)-2, int(blockSize)-2)
    elif p[1]==0:
        rect = pygame.Rect(int(blockSize)*p[1]+301, int(blockSize)*p[0]+20, int(blockSize)-2, int(blockSize)-1)
    elif p[0]==0:
        rect = pygame.Rect(int(blockSize)*p[1]+300, int(blockSize)*p[0]+21, int(blockSize)-1, int(blockSize)-2)
    else:
        rect = pygame.Rect(int(blockSize)*p[1]+300, int(blockSize)*p[0]+20, int(blockSize)-1, int(blockSize)-1)
    
    if flag==0:
        if matriz[p[0]][p[1]] == 1:
            pygame.draw.rect(tela, DARK_GREEN, rect)
            #pygame.draw.rect(tela, BLACK, rect2, 1)
        elif matriz[p[0]][p[1]] == 2:
            pygame.draw.rect(tela, MARROM_ESCURO, rect )
            #pygame.draw.rect(tela, BLACK, rect2, 1)
        elif matriz[p[0]][p[1]] == 3: 
            pygame.draw.rect(tela, DARK_BLUE, rect )
            #pygame.draw.rect(tela, BLACK, rect2, 1)
        elif matriz[p[0]][p[1]] == 4: 
            pygame.draw.rect(tela, DARK_RED, rect)
            #pygame.draw.rect(tela, BLACK, rec2t, 1)
    else:
        x=1
        #cubo(tela, int(blockSize), p, matriz )
        #pygame.draw.rect(tela, color_light, rect)
    
    pygame.display.update()
    
def Pinta_solucao(tela, matriz, solucao, flag): #pinta o grid feito, recebe a tela e a matriz
    #screen.fill(WHITE)
    
    blockSize = (700/len(matriz))#Set the size of the grid block
    for p in solucao:
        if p[0]==0 and p[1]==0:
                rect = pygame.Rect(int(blockSize)*p[1]+301, int(blockSize)*p[0]+21, int(blockSize)-2, int(blockSize)-2)
        elif p[1]==0:
            rect = pygame.Rect(int(blockSize)*p[1]+301, int(blockSize)*p[0]+20, int(blockSize)-2, int(blockSize)-1)
        elif p[0]==0:
            rect = pygame.Rect(int(blockSize)*p[1]+300, int(blockSize)*p[0]+21, int(blockSize)-1, int(blockSize)-2)
        else:
            rect = pygame.Rect(int(blockSize)*p[1]+300, int(blockSize)*p[0]+20, int(blockSize)-1, int(blockSize)-1)
    
        time.sleep(0.05)
        pygame.draw.rect(tela, WHITE, rect)
        pygame.display.update()

        
        
   

