import pygame
import sys
import main
import webbrowser

from tkinter import *

screen = pygame.display.set_mode((1000,750))
background = pygame.image.load('labirinto3.jpg')
git = pygame.image.load('github2.png')
screen.fill((0,0,0))
screen.blit(background, (0, 0))

carlos = 'https://github.com/carlloshenrry'
joao = 'https://github.com/joaohp2000'

class Menu:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.width = 1064
        self.GREY = (128, 128, 128)
        self.height = 712
        self.options = {}
        self.clicked = False
        self.command = None
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Menu")
        self.font = ("ZOMBIE.TTF")
        
    def draw_text(self, text, font_name, size, color, x, y, align="center"):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x + 60, y + 27)})
        self.screen.blit(text_surface, text_rect)
        
    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        return self.command
            
    def add_option(self, label, width, height, x, y, command):
        if(label == 'carlloshenrry' or label == 'joaohp2000'):
            surface = pygame.Surface((0, 0))
            surface.fill((173,216,230))
        else:
            surface = pygame.Surface((125, 50))
            surface.fill(self.GREY)
            
        rect = pygame.Rect(x, y, width, height)
        self.options[label] = {
                                'label': label,
                                'surface': surface,
                                'rect': rect,
                                'command': command
                            }
        
    def update(self):
        for option in self.options:
            if self.options[option]["rect"].collidepoint((self.mx, self.my)):
                self.options[option]["surface"].set_alpha(255)
                if self.clicked:
                    self.running = False
                    self.command = self.options[option]["command"]
            else:
                self.options[option]["surface"].set_alpha(0)
    
    def events(self):
        self.mx, self.my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.clicked = True
            else:
                self.clicked = False
                
    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(background, (0, 0))
        self.screen.blit(git, (0,635))
        self.draw_text("Menu", self.font, 50, (255, 255, 255), self.width//2, 50, align="center")
        for option in self.options:
            if(self.options[option]["command"] == 'carlloshenrry' or self.options[option]["command"] == 'joaohp2000' ):
                self.screen.blit(self.options[option]["surface"], self.options[option]["rect"])
                self.draw_text(self.options[option]["label"], self.font, 25, (173,216,230), self.options[option]["rect"].x, self.options[option]["rect"].y)
            else:
                self.screen.blit(self.options[option]["surface"], self.options[option]["rect"])
                self.draw_text(self.options[option]["label"], self.font, 50, (255, 255, 255), self.options[option]["rect"].x, self.options[option]["rect"].y)
        pygame.display.update()
    
Init = Menu()
Init.add_option("PLAY", 500, 50, Init.width//2, 300, "play")
Init.add_option("EXIT", 500, 50, Init.width//2, 350, "exit")
Init.add_option("carlloshenrry", 250, 20, 95, 665, "carlloshenrry")
Init.add_option("joaohp2000", 250, 20, 90, 640, "joaohp2000")
command = Init.run()
if command == "play":
    main.main(screen)
elif command == "exit":
    print("exit")
elif command == "carlloshenrry":
    webbrowser.open_new(carlos)
elif command == "joaohp2000":
    webbrowser.open_new(joao)


    
    
    