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
walls = pygame.sprite.Group()
# pellet_setup = ["11111111111100111111111111",
#                 "10000100000100100000100001",
#                 "10000100000100100000100001",
#                 "20000100000100100000100002",
#                 "11111111111111111111111111",
#                 "10000100100000000100100001",
#                 "10000100100000000100100001",
#                 "11111100111100111100111111",
#                 "00000100000000000000100000",
#                 "00000100000000000000100000",
#                 "00000100000000000000100000",
#                 "00000100000000000000100000",
#                 "00000100000000000000100000",
#                 "00000100000000000000100000",
#                 "00000100000000000000100000",
#                 "00000100000000000000100000",
#                 "00000100000000000000100000",
#                 "00000100000000000000100000",
#                 "00000100000000000000100000",
#                 "11111111111100111111111111",
#                 "10000100000100100000100001",
#                 "10000100000100100000100001",
#                 "211001111111p1111111100112",
#                 "00100100100000000100100100",
#                 "00100100100000000100100100",
#                 "11111100111100111100111111",
#                 "10000000000100100000000001",
#                 "10000000000100100000000001",
#                 "11111111111111111111111111"
#                 ]
# temp = []
# temp2 = []
# for y in range(len(pellet_setup)):
#     for x in range(len(pellet_setup[y])):
#         if pellet_setup[y][x] == "1":
#             temp.append((x, y))
#         elif pellet_setup[y][x] == "2":
#             temp2.append((x, y))
# print(temp)
# print(temp2)

pellet_setup = ([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0), (21, 0), (22, 0), (23, 0), (24, 0), (25, 0), (0, 1), (5, 1), (11, 1), (14, 1), (20, 1), (25, 1), (0, 2), (5, 2), (11, 2), (14, 2), (20, 2), (25, 2), (5, 3), (11, 3), (14, 3), (20, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (14, 4), (15, 4), (16, 4), (17, 4), (18, 4), (19, 4), (20, 4), (21, 4), (22, 4), (23, 4), (24, 4), (25, 4), (0, 5), (5, 5), (8, 5), (17, 5), (20, 5), (25, 5), (0, 6), (5, 6), (8, 6), (17, 6), (20, 6), (25, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (8, 7), (9, 7), (10, 7), (11, 7), (14, 7), (15, 7), (16, 7), (17, 7), (20, 7), (21, 7), (22, 7), (23, 7), (24, 7), (25, 7), (5, 8), (20, 8), (5, 9), (20, 9), (5, 10), (20, 10), (5, 11), (20, 11), (5, 12), (20, 12), (5, 13), (20, 13), (5, 14), (20, 14), (5, 15), (20, 15), (5, 16), (20, 16), (5, 17), (20, 17), (5, 18), (20, 18), (0, 19), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (6, 19), (7, 19), (8, 19), (9, 19), (10, 19), (11, 19), (14, 19), (15, 19), (16, 19), (17, 19), (18, 19), (19, 19), (20, 19), (21, 19), (22, 19), (23, 19), (24, 19), (25, 19), (0, 20), (5, 20), (11, 20), (14, 20), (20, 20), (25, 20), (0, 21), (5, 21), (11, 21), (14, 21), (20, 21), (25, 21), (1, 22), (2, 22), (5, 22), (6, 22), (7, 22), (8, 22), (9, 22), (10, 22), (11, 22), (13, 22), (14, 22), (15, 22), (16, 22), (17, 22), (18, 22), (19, 22), (20, 22), (23, 22), (24, 22), (2, 23), (5, 23), (8, 23), (17, 23), (20, 23), (23, 23), (2, 24), (5, 24), (8, 24), (17, 24), (20, 24), (23, 24), (0, 25), (1, 25), (2, 25), (3, 25), (4, 25), (5, 25), (8, 25), (9, 25), (10, 25), (11, 25), (14, 25), (15, 25), (16, 25), (17, 25), (20, 25), (21, 25), (22, 25), (23, 25), (24, 25), (25, 25), (0, 26), (11, 26), (14, 26), (25, 26), (0, 27), (11, 27), (14, 27), (25, 27), (0, 28), (1, 28), (2, 28), (3, 28), (4, 28), (5, 28), (6, 28), (7, 28), (8, 28), (9, 28), (10, 28), (11, 28), (12, 28), (13, 28), (14, 28), (15, 28), (16, 28), (17, 28), (18, 28), (19, 28), (20, 28), (21, 28), (22, 28), (23, 28), (24, 28), (25, 28)],
[(0, 3), (25, 3), (0, 22), (25, 22)])

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


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        pygame.sprite.Sprite.__init__(self)
        self.rect = (pos[0], pos[1], size[0], size[1])
        self.image = pygame.Surface(size)
        self.image.fill((0, 0, 0))
        if size[0] > size[1]:
            pygame.draw.line(self.image, (0, 0, 200), (size[1]//2, 0), (size[0]-size[1]//2, 0), 5)
            pygame.draw.line(self.image, (0, 0, 200), (size[1]//2, size[1]-1), (size[0]-size[1]//2, size[1]-1), 5)
            pygame.draw.arc(self.image, (0, 0, 200), (0, 0, size[1], size[1]), 3.142/2, -3.142/2, 3)
            pygame.draw.arc(self.image, (0, 0, 200), (size[0] - size[1], 0, size[1], size[1]), -3.142 / 2, 3.142 / 2, 3)


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
        s = pygame.sprite.Sprite
        s.rect = self.rect.move(dir[0], dir[1])
        return len(pygame.sprite.spritecollide(s, walls, False)) == 0

    def update(self, time):
        self.time += time
        if self.time >= self.time_for_move:
            self.time -= self.time_for_move
            self.move()

    def move(self):
        if self.can_go(self.next_dir):
            self.rect = self.rect.move(self.next_dir[0], self.next_dir[1])
            self.current_dir = self.next_dir
        elif self.can_go(self.current_dir):
            self.rect = self.rect.move(self.current_dir[0], self.current_dir[1])
        pelletList = pygame.sprite.spritecollide(self, pellets, True)
        self.num_pellets += len(pelletList)
        for i in pelletList:
            if i is SuperPellet:
                print("super")


def level_setup():
    for i in pellets.sprites():
        i.kill()
    for pos in pellet_setup[0]:
        pellets.add(Pellet((pos[0]*10, pos[1]*10)))
    for pos in pellet_setup[1]:
        pellets.add(SuperPellet((pos[0]*10, pos[1]*10)))



pacman = Pacman(sprites)
level_setup()
walls.add(Wall((150, 150), (100, 25)))
sprites.add(pellets)
sprites.add(walls)
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
                pacman.next_dir = (0, -10)
            elif event.key == K_DOWN:
                pacman.next_dir = (0, 10)
            elif event.key == K_LEFT:
                pacman.next_dir = (-10, 0)
            elif event.key == K_RIGHT:
                pacman.next_dir = (10, 0)
    sprites.update(Clock.tick())
    win.fill((0, 0, 0))
    sprites.draw(win)
    surf.blit(pygame.transform.scale(win, (surf.get_width() - offset[0]*2, surf.get_height() - offset[1]*2)), (offset[0], offset[1]))
    pygame.display.update()
