import pygame
from network import Network
from player import Player
pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Button:
    def __init__(self, text , x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

def redrawWindow(win, game, p):
    win.fill((128, 128, 128))
    pass


def main():
    pass


main()
