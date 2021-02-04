import pygame, sys, random
from pygame.locals import *
pygame.init()
win = pygame.display.set_mode((100, 100))


class Pacman(pygame.sprite.Sprite):
    def __init__(self, group, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self, group)
        self.image = pygame.transform.scale(pygame.image.load('pacman.png'), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.pos = pos
        self.current_dir = ()
        self.next_dir = ()
        self.num_pellets = 0
        print(self.rect)


sprites = pygame.sprite.Group()
p = Pacman(sprites)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    sprites.draw(win)
    pygame.display.update()
