import pygame, sys, random
from pygame.locals import *
pygame.init()
win = pygame.display.set_mode((100, 100))

class Pacman:
    def __init__(self, pos=(0, 0)):
        self.pos = pos
        self.current_dir = ()
        self.next_dir = ()
        self.num_pellets = 0

p = Pacman()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()