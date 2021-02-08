import pygame, sys, random
from pygame.locals import *
pygame.init()
surf = pygame.display.set_mode((300, 300), RESIZABLE)
Clock = pygame.time.Clock()
win = pygame.Surface((500, 500))
offset = [0, 0]
tile_width = 10
pellets = pygame.sprite.Group()
sprites = pygame.sprite.Group()
ghosts = pygame.sprite.Group()


class Pellet(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, (255, 255, 255), (7, 7), 6)

        self.rect = self.image.get_rect()
        self.rect.center = pos


class SuperPellet(Pellet):
    def __init__(self, pos):
        Pellet.__init__(self, pos)


class Pacman(pygame.sprite.Sprite):
    def __init__(self, group, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self, group)
        self.image = pygame.image.load('pacman.png')
        self.rect = self.image.get_rect()
        self.rect.center = (25, 25)
        self.pos = pos
        self.current_dir = (0, 0)
        self.next_dir = (0, 0)
        self.num_pellets = 0
        self.time_for_move = 100
        self.time = 0

    def can_go(self, dir):
        return True

    def update(self, time):
        self.time += time
        if self.time >= self.time_for_move:
            self.time -= self.time_for_move
            self.move()

    def move(self):
        if self.can_go(self.next_dir):
            self.rect = self.rect.move(self.next_dir[0]*10, self.next_dir[1]*10)
            self.current_dir = self.next_dir
        elif self.can_go(self.current_dir):
            self.rect.move(self.current_dir[0], self.current_dir[1])
        pelletList = pygame.sprite.spritecollide(self, pellets, True)
        self.num_pellets += len(pelletList)
        for i in pelletList:
            if i is SuperPellet:
                print("super")


pacman = Pacman(sprites)
pellets.add(Pellet((100, 100)))
sprites.add(pellets)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == VIDEORESIZE:
            if event.w > event.h:
                offset[0] = (event.w - event.h)//2
                offset[1] = 0
            else:
                offset[0] = 0
                offset[1] = (event.h - event.w)//2
            surf = pygame.display.set_mode((event.w, event.h), RESIZABLE)
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                pacman.next_dir = (0, -1)
            elif event.key == K_DOWN:
                pacman.next_dir = (0, 1)
            elif event.key == K_LEFT:
                pacman.next_dir = (-1, 0)
            elif event.key == K_RIGHT:
                pacman.next_dir = (1, 0)
    sprites.update(Clock.tick())
    win.fill((0, 0, 0))
    sprites.draw(win)
    surf.blit(pygame.transform.scale(win, (surf.get_width() - offset[0]*2, surf.get_height() - offset[1]*2)), (offset[0], offset[1]))
    pygame.display.update()
