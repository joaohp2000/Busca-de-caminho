import pygame
import sys
from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
#cores

color_light = (170,170,170)# light shade of the button
color_dark = (100,100,100) # dark shade of the button

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
MARROM = (75, 54, 33)

class botao: #classe botão
    def __init__(self, tela, color): #construtor recebe a tela e sua cor
        self.tela=tela
        self.color=color
        smallfont = pygame.font.SysFont('Corbel',20) # configura texto
        text = smallfont.render('Arquivo de Entrada' , True , WHITE)
        pygame.draw.rect(self.tela,self.color,[10,10,140,40])  
        screen.blit(text , (15,20))

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
            rect = pygame.Rect(int(blockSize)*x+300, int(blockSize)*y+20, int(blockSize)-1, int(blockSize)-1)
            if matriz[y][x] == 1:
                pygame.draw.rect(tela, GREEN, rect)
            elif matriz[y][x] == 2:
                pygame.draw.rect(tela, MARROM, rect )
            elif matriz[y][x] == 3: 
                pygame.draw.rect(tela, BLUE, rect )
            elif matriz[y][x] == 4: 
                pygame.draw.rect(tela, RED, rect)
            


pygame.init() # initializing the constructor
res = (0,0) # screen resolution
screen = pygame.display.set_mode(res,pygame.RESIZABLE)# opens up a window
screen.fill(WHITE) #pinta tela de branco
def main(screen):
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= mouse[0] <= 10+140 and 10 <= mouse[1] <= 10+40:
                    matriz=open_file()
                    if(matriz != 0):    
                        entrada=matriz[0]
                        saida=matriz[1]
                        del matriz[0:2]
                        print(entrada,saida)
                        print(len(matriz))
                        flag=1
                        screen.fill(WHITE)
                        cria_grid(screen, len(matriz))
                        Pinta_Grid(screen, matriz)
                    
        # fills the screen with a color
        
       
        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade 
        if 10 <= mouse[0] <= 10+140 and 10 <= mouse[1] <= 10+40:
            botao(screen, color_light) 
        else:
            botao(screen, color_dark)

        # updates the frames of the game
        pygame.display.update()

main(screen)