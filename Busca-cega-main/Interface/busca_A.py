import math
import pygame
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)

class Local:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        
    def get_pos(self):
    	return self.row, self.col
      
    def is_start(self):
        return self.color == GREEN
    
    def is_border(self):
        return self.color == RED
    
    def is_final(self):
        return self.color == BLACK
        
    def make_start(self):
        self.color = GREEN
    
    def make_path(self):
        self.color = GREY
    
    def make_border(self):
        self.color = RED
     
    def make_end(self):
        self.color = BLACK
        
    def make_search(self):
        self.color = ORANGE
    
    def reset(self):
        self.color = WHITE
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_vizinhos(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 : #sub_block
            self.neighbors.append(grid[self.row + 1][self.col])
            
        if self.row > 0 : #up_block
            self.neighbors.append(grid[self.row - 1][self.col])
            
        if self.col < self.total_rows - 1 : #dir_block
            self.neighbors.append(grid[self.row][self.col + 1])
            
        if self.col > 0 : #esq_block
            self.neighbors.append(grid[self.row][self.col - 1])
            
    def __lt__(self, other):
        return False


def heuristic(point1,point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Local(i, j, gap, rows)
            grid[i].append(spot)
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range (rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))
 
            
def draw(win, grid, rows, width):
    win.fill(WHITE)
    
    for row in grid:
        for spot in row:
            spot.draw(win)
            
    draw_grid(win, rows, width)
    pygame.display.update()
  
    
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    
    row = y // gap
    col = x // gap
    
    return row, col 

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()
        

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())
    
    open_set_hash = {start}
    
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end() 
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_border()
        
        draw()
        
        if current != start:
            current.make_search()
            
    return False                
    



def func_busca_A(origem, destino, matriz):
   no = 0
   
   y1, x1 = origem
   y2, x2 = destino
   
   run = True
   if(matriz[y1][x1] != matriz[y2][x2]):
       while run:
           right = Heuristica(y1 + 1, x1, destino)
           print(right)
           print(matriz[y1 + 1][x1])
           right = right + matriz[y1 + 1][x1] #right
           
           left = Heuristica(y1 - 1, x1, destino)
           left + matriz[y1 - 1][x1] #left
           
           down = Heuristica(y1, x1 + 1, destino) 
           down + matriz[y1][x1 + 1] #down
           
           up = Heuristica(y1, x1 - 1, destino) 
           up + matriz[y1][x1 - 1] #up
           
           print(right)
           run = False
           


def Heuristica(ordenada, abscissa, destino):
    y1 = ordenada
    x1= abscissa
    y2, x2 = destino
    Heu = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return Heu
    
func_busca_A(origem, destino, matriz)     
    
    
       

