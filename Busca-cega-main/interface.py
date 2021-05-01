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
        rect = pygame.Rect(self.celula_size*self.x+200, self.celula_size*self.y+10, self.celula_size+1, self.celula_size+1)
        pygame.draw.rect(self.tela, self.color, rect, 1)

    def pinta_celula(self, cor):
        self.color = cor 
        rect = pygame.Rect(self.celula_size*self.x+201, self.celula_size*self.y+11, self.celula_size-1, self.celula_size-1)
        pygame.draw.rect(self.tela, self.color, rect)
    
    def relevo(self, cor):
         
        celula_tamanho = self.celula_size//1.4
        pos = (self.celula_size-celula_tamanho)//2

        x1=self.celula_size*self.x+200+self.celula_size
        y1=self.celula_size*self.y+10+self.celula_size

        x2=self.celula_size*self.x+200+celula_tamanho+pos
        y2=self.celula_size*self.y+10+celula_tamanho+pos

        rect = pygame.Rect(self.celula_size*self.x+200+pos, self.celula_size*self.y+10+pos, celula_tamanho, celula_tamanho)
        pygame.draw.rect(self.tela, cor, rect)

        pygame.draw.rect(self.tela, BLACK, rect, 1)
        pygame.draw.line(self.tela, BLACK, (x1,y1),(x2,y2))
        pygame.draw.line(self.tela, BLACK, (x1,y1-self.celula_size),(x2,y2-celula_tamanho))
        pygame.draw.line(self.tela, BLACK, (x1-self.celula_size,y1-self.celula_size),(x2-celula_tamanho,y2-celula_tamanho))
        pygame.draw.line(self.tela, BLACK, (x1-self.celula_size,y1),(x2-celula_tamanho,y2))
        
class botao: #classe botão
    def __init__(self, tela, pos_tam, texto, pos_tex): #construtor recebe a tela e sua cor
        self.tela=tela
        self.pos_tam= pos_tam

        smallfont = pygame.font.SysFont('Corbel',20) # configura texto
        text = smallfont.render(texto , True , WHITE) 
        self.tela.blit(text , pos_tex )
        mouse = pygame.mouse.get_pos()
        if pos_tam[0] <= mouse[0] <= pos_tam[0]+pos_tam[2] and pos_tam[1] <= mouse[1] <= pos_tam[1]+pos_tam[3]: # botao de entrada
            pygame.draw.rect(self.tela,color_light, pos_tam )
            self.tela.blit(text , pos_tex )
        else:
            pygame.draw.rect(self.tela,color_dark, pos_tam )
            self.tela.blit(text , pos_tex )
    
    def click(self):
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0) and self.pos_tam[0] <= mouse[0] <= self.pos_tam[0]+self.pos_tam[2] and self.pos_tam[1] <= mouse[1] <= self.pos_tam[1]+self.pos_tam[3]:
            return True
        else:
            return False

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
        if matriz[p[0]][p[1]] == 1:
            grid[p[0]][p[1]].relevo(DARK_GREEN)
        elif matriz[p[0]][p[1]] == 2:
            grid[p[0]][p[1]].relevo(MARROM_ESCURO)
        elif matriz[p[0]][p[1]] == 3: 
            grid[p[0]][p[1]].relevo(DARK_BLUE)
        elif matriz[p[0]][p[1]] == 4: 
            grid[p[0]][p[1]].relevo(DARK_RED)
        
    
    pygame.display.update()
    
def Pinta_solucao(grid, solucao): #pinta na tela o caminho encontrado de branco 
    time.sleep(0.5)
    for p in solucao:                      #recebe matriz de objetos, e lista com coordenadas da solucao
        time.sleep(0.05)
        grid[p[0]][p[1]].pinta_celula(WHITE)
        pygame.display.update()

def custos(tela, custo_total, nos_visitados, busca, entrada, saida):
    
    rect = pygame.Rect(10, 160, 150, 190)
    pygame.draw.rect(tela, DARK_GREEN, rect)
    
    smallfont = pygame.font.SysFont('Calibri', 20) # configura o Titulo
    
    text = smallfont.render( busca , True , WHITE)
    if busca == "Busca Cega":
        tela.blit(text , (30, 170) )
    else:
        tela.blit(text , (50, 170) )

    
    text = smallfont.render( ("Entrada:") , True , WHITE)
    tela.blit(text , (12, 200) )
    text = smallfont.render("(%d,%d)" %(entrada[0], entrada[1]) , True , WHITE)
    tela.blit(text , (80, 200) )

    
    text = smallfont.render( "Saida:" , True , WHITE)
    tela.blit(text , (12, 230) )
    text = smallfont.render( "(%d,%d)" %(saida[0], saida[1]) , True , WHITE)
    tela.blit(text , (70, 230) )

    text = smallfont.render("Custo Total: %d" %custo_total , True , WHITE)
    tela.blit(text , (12, 260) )
    
    text = smallfont.render("Numero de Nos" , True , WHITE) 
    tela.blit(text , (12, 290) )
    text = smallfont.render("Expandidos: %d" %nos_visitados , True , WHITE) 
    tela.blit(text , (12, 310) )



def main():
    pygame.init() # initializing the constructor
    res = (1000,700) # screen resolutions
    screen = pygame.display.set_mode(res)
    screen.fill(WHITE)
    while True: 
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

        x=Celula(42, screen, [0,0])
        x.pinta_celula(GREEN)
        x.relevo(DARK_GREEN)

        x1=Celula(42, screen, [1,0])
        x1.pinta_celula(GREEN)
        x1.relevo(DARK_GREEN)

        x2=Celula(42, screen, [0,1])
        x2.pinta_celula(GREEN)
        x2.relevo(DARK_GREEN)

        x3=Celula(42, screen, [1,1])
        x3.pinta_celula(GREEN)
        x3.relevo(DARK_GREEN)
        pygame.display.update()

#main()
