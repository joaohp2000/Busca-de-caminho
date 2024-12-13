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
MARROM_ESCURO = (40,19,0)


class Celula:
    def __init__(self, tamanho_matriz, tela, pos):
        self.tela= tela
        self.tamanho_matriz= tamanho_matriz
        self.color = BLACK
        self.x = pos[1]
        self.y = pos[0]
        self.celula_size = 700//self.tamanho_matriz
        rect = pygame.Rect(self.celula_size*self.x+200, self.celula_size*self.y+20, self.celula_size, self.celula_size)
        pygame.draw.rect(self.tela, self.color, rect, 1)

    def pinta_celula(self, cor):
        self.color = cor 
        rect = pygame.Rect(self.celula_size*self.x+201, self.celula_size*self.y+21, self.celula_size-1, self.celula_size-1)
        pygame.draw.rect(self.tela, self.color, rect)
        
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
    root.withdraw()
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
    matriz=[]
    for y in range(tamanho_matriz):
        matriz.append([])
        for x in range(tamanho_matriz):
            celula=Celula(tamanho_matriz, tela, [y,x])
            matriz[y].append(celula)

    return matriz         

def Pinta_Grid(matriz, grid): #pinta o grid feito, recebe a tela e a matriz
    #screen.fill(WHITE)z
    for y in range(len(matriz)):
        for x in range(len(matriz)):
            if matriz[y][x] == 1:
                grid[y][x].pinta_celula(GREEN)
            elif matriz[y][x] == 2:
                grid[y][x].pinta_celula(MARROM)
            elif matriz[y][x] == 3: 
                grid[y][x].pinta_celula(BLUE)
            elif matriz[y][x] == 4:
                grid[y][x].pinta_celula(RED)

def Pinta_borda(grid, matriz, p, flag):

    if flag==0:
        if matriz[p[0]][p[1]] == 1:
            grid[p[0]][p[1]].pinta_celula(DARK_GREEN)
        elif matriz[p[0]][p[1]] == 2:
            grid[p[0]][p[1]].pinta_celula(MARROM_ESCURO)
        elif matriz[p[0]][p[1]] == 3: 
            grid[p[0]][p[1]].pinta_celula(DARK_BLUE)
        elif matriz[p[0]][p[1]] == 4: 
            grid[p[0]][p[1]].pinta_celula(DARK_RED)

    else:
        x=1
        
    
    pygame.display.update()
    
def Pinta_solucao(grid, solucao): #pinta na tela o caminho encontrado de branco 
    for p in solucao:                      #recebe matriz de objetos, e lista com coordenadas da solucao
        time.sleep(0.05)
        grid[p[0]][p[1]].pinta_celula(WHITE)
        pygame.display.update()

        
