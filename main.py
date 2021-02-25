import pygame, sys, random, math
from pygame.locals import *
pygame.init()
surf = pygame.display.set_mode((725//2, 800//2), RESIZABLE)
Clock = pygame.time.Clock()
win = pygame.Surface((725, 800))
offset = [0, 0]
tile_width = 10
pellets = pygame.sprite.Group()
sprites = pygame.sprite.Group()
ghosts = pygame.sprite.Group()
walls = pygame.sprite.Group()
level = -1
level_vars = [150, 125, 100]
# pellet_setup = ["11111111111100111111111111",
#                 "10000100000100100000100001",
#                 "10000100000100100000100001",
#                 "20000100000100100000100002",
#                 "11111111111111111111111111",
#                 "10000100100000000100100001",
#                 "10000100100000000100100001",
#                 "11111100111100111100111111",
#                 "00000100000100100000100000",
#                 "00000100000100100000100000",
#                 "00000100111111111100100000",
#                 "00000100100000000100100000",
#                 "00000100100000000100100000",
#                 "00000111100000000111100000",
#                 "00000100100000000100100000",
#                 "00000100100000000100100000",
#                 "00000100111111111100100000",
#                 "00000100100000000100100000",
#                 "00000100100000000100100000",
#                 "11111111111100111111111111",
#                 "10000100000100100000100001",
#                 "10000100000100100000100001",
#                 "21100111111111111111100112",
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

pellet_setup = ([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0), (21, 0), (22, 0), (23, 0), (24, 0), (25, 0), (0, 1), (5, 1), (11, 1), (14, 1), (20, 1), (25, 1), (0, 2), (5, 2), (11, 2), (14, 2), (20, 2), (25, 2), (5, 3), (11, 3), (14, 3), (20, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (14, 4), (15, 4), (16, 4), (17, 4), (18, 4), (19, 4), (20, 4), (21, 4), (22, 4), (23, 4), (24, 4), (25, 4), (0, 5), (5, 5), (8, 5), (17, 5), (20, 5), (25, 5), (0, 6), (5, 6), (8, 6), (17, 6), (20, 6), (25, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (8, 7), (9, 7), (10, 7), (11, 7), (14, 7), (15, 7), (16, 7), (17, 7), (20, 7), (21, 7), (22, 7), (23, 7), (24, 7), (25, 7), (5, 8), (11, 8), (14, 8), (20, 8), (5, 9), (11, 9), (14, 9), (20, 9), (5, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10), (16, 10), (17, 10), (20, 10), (5, 11), (8, 11), (17, 11), (20, 11), (5, 12), (8, 12), (17, 12), (20, 12), (5, 13), (6, 13), (7, 13), (8, 13), (17, 13), (18, 13), (19, 13), (20, 13), (5, 14), (8, 14), (17, 14), (20, 14), (5, 15), (8, 15), (17, 15), (20, 15), (5, 16), (8, 16), (9, 16), (10, 16), (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16), (17, 16), (20, 16), (5, 17), (8, 17), (17, 17), (20, 17), (5, 18), (8, 18), (17, 18), (20, 18), (0, 19), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (6, 19), (7, 19), (8, 19), (9, 19), (10, 19), (11, 19), (14, 19), (15, 19), (16, 19), (17, 19), (18, 19), (19, 19), (20, 19), (21, 19), (22, 19), (23, 19), (24, 19), (25, 19), (0, 20), (5, 20), (11, 20), (14, 20), (20, 20), (25, 20), (0, 21), (5, 21), (11, 21), (14, 21), (20, 21), (25, 21), (1, 22), (2, 22), (5, 22), (6, 22), (7, 22), (8, 22), (9, 22), (10, 22), (11, 22), (12, 22), (13, 22), (14, 22), (15, 22), (16, 22), (17, 22), (18, 22), (19, 22), (20, 22), (23, 22), (24, 22), (2, 23), (5, 23), (8, 23), (17, 23), (20, 23), (23, 23), (2, 24), (5, 24), (8, 24), (17, 24), (20, 24), (23, 24), (0, 25), (1, 25), (2, 25), (3, 25), (4, 25), (5, 25), (8, 25), (9, 25), (10, 25), (11, 25), (14, 25), (15, 25), (16, 25), (17, 25), (20, 25), (21, 25), (22, 25), (23, 25), (24, 25), (25, 25), (0, 26), (11, 26), (14, 26), (25, 26), (0, 27), (11, 27), (14, 27), (25, 27), (0, 28), (1, 28), (2, 28), (3, 28), (4, 28), (5, 28), (6, 28), (7, 28), (8, 28), (9, 28), (10, 28), (11, 28), (12, 28), (13, 28), (14, 28), (15, 28), (16, 28), (17, 28), (18, 28), (19, 28), (20, 28), (21, 28), (22, 28), (23, 28), (24, 28), (25, 28)],
[(0, 3), (25, 3), (0, 22), (25, 22)])

wall_setup = [(0, 0, 725, 25), (0, 0, 25, 350), (0, 775, 725, 25), (700, 0, 25, 350), (0, 400, 25, 400), (700, 400, 25, 400),
              (75, 75, 75, 50), (200, 75, 100, 50), (350, 25, 25, 100), (425, 75, 100, 50), (575, 75, 75, 50),
              (75, 175, 75, 25), (200, 175, 25, 175), (275, 175, 175, 25), (500, 175, 25, 175), (575, 175, 75, 25),
              (25, 250, 125, 100), (225, 250, 75, 25), (350, 200, 25, 75), (425, 250, 75, 25), (575, 250, 125, 100),
              (25, 400, 125, 100), (200, 400, 25, 100), (500, 400, 25, 100), (575, 400, 125, 100), (275, 475, 175, 25),
              (75, 550, 75, 25), (200, 550, 100, 25), (350, 500, 25, 75), (425, 550, 100, 25), (575, 550, 75, 25),
              (25, 625, 50, 25), (125, 575, 25, 75), (200, 625, 25, 75), (275, 625, 175, 25), (500, 625, 25, 75), (575, 575, 25, 75), (650, 625, 50, 25),
              (75, 700, 225, 25), (350, 650, 25, 75), (425, 700, 225, 25), (275, 325, 175, 100),
              (-25, 325, 25, 25), (725, 325, 25, 25), (-25, 400, 25, 25), (725, 400, 25, 25)]


class Pellet(pygame.sprite.Sprite):
    def __init__(self, pos, size=12):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, (255, 255, 255), (size//2, size//2), size//2-1)

        self.rect = self.image.get_rect()
        self.rect.center = pos


class SuperPellet(Pellet):
    def __init__(self, pos):
        Pellet.__init__(self, pos, 18)


class Wall(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
        self.image = pygame.Surface((rect[2], rect[3]))
        self.image.fill((0, 0, 0))
        pygame.draw.arc(self.image, (0, 0, 200), (0, 0, 20, 20), 3.142 / 2, 3.142, 3)
        pygame.draw.arc(self.image, (0, 0, 200), (rect[2] - 20, 0, 20, 20), 0, 3.142 / 2, 3)
        pygame.draw.arc(self.image, (0, 0, 200), (0, rect[3] - 20, 20, 20), 3.142, -3.142 / 2, 3)
        pygame.draw.arc(self.image, (0, 0, 200), (rect[2] - 20, rect[3] - 20, 20, 20), -3.142 / 2, 0, 3)
        pygame.draw.line(self.image, (0, 0, 200), (10, 0), (rect[2]-10, 0), 5)
        pygame.draw.line(self.image, (0, 0, 200), (10, rect[3]-1), (rect[2]-10, rect[3]-1), 5)
        pygame.draw.line(self.image, (0, 0, 200), (0, 10), (0, rect[3]-10), 5)
        pygame.draw.line(self.image, (0, 0, 200), (rect[2]-1, 10), (rect[2]-1, rect[3]-10), 5)


class Movable(pygame.sprite.Sprite):
    def __init__(self, pos, time_for_move=level_vars[level]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.current_dir = (0, 0)
        self.next_dir = (0, 0)
        self.time = 0
        self.time_for_move = time_for_move

    def move(self):
        if self.can_go(self.next_dir):
            self.rect = self.rect.move(self.next_dir[0], self.next_dir[1])
            self.current_dir = self.next_dir
        elif self.can_go(self.current_dir):
            self.rect = self.rect.move(self.current_dir[0], self.current_dir[1])
        if self.rect.center[0] <= -25:
            self.rect.center = (750, self.rect.center[1])
        elif self.rect.center[0] >= 750:
            self.rect.center = (-25, self.rect.center[1])

    def can_go(self, dir):
        s = pygame.sprite.Sprite
        s.rect = self.rect.move(dir[0], dir[1])
        return len(pygame.sprite.spritecollide(s, walls, False)) == 0


class Ghost(Movable):
    def __init__(self, color=(225, 125, 125), pos=(50, 50)):
        Movable.__init__(self, pos, 200)
        self.color = color
        self.update_image()

    def update_image(self):
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, self.color, (25, 20), 20, 0)
        pygame.draw.rect(self.image, self.color, (5, 20, 40, 17), 0)
        pygame.draw.circle(self.image, self.color, (12, 37), 7, 0)
        pygame.draw.circle(self.image, self.color, (25, 37), 7, 0)
        pygame.draw.circle(self.image, self.color, (38, 37), 7, 0)
        pygame.draw.ellipse(self.image, (255, 255, 255), (11, 12, 12, 16), 0)
        pygame.draw.ellipse(self.image, (255, 255, 255), (27, 12, 12, 16), 0)
        pygame.draw.ellipse(self.image, (0, 0, 0),
                            (14 + 3*self.current_dir[0]//25, 16 + 3*self.current_dir[1]//25, 6, 8))
        pygame.draw.ellipse(self.image, (0, 0, 0),
                            (30 + 3 * self.current_dir[0] // 25, 16 + 3 * self.current_dir[1] // 25, 6, 8))

    def update(self, time):
        self.time += time
        if self.time >= self.time_for_move:
            self.time -= self.time_for_move
            self.get_next_dir()
            self.move()
            self.update_image()

    def get_next_dir(self):
        options = []
        for i in [(25, 0), (-25, 0), (0, 25), (0, -25)]:
            if not (i[0] == -1*self.current_dir[0] and i[1] == -1*self.current_dir[1]):
                if self.can_go(i):
                    options.append(i)
        if len(options) > 0:
            self.next_dir = options[random.randint(0, len(options)-1)]
        else:
            self.next_dir = (-1*self.current_dir[0], -1*self.current_dir[1])


class Pacman(Movable):
    def __init__(self, pos=(350, 600)):
        Movable.__init__(self, pos)
        self.num_pellets = 0
        self.angle = 3.1416/3
        self.update_image()

    def update(self, time):
        self.time += time
        if self.time >= self.time_for_move:
            self.time -= self.time_for_move
            self.move()
            self.check_pellet_collide()
            self.update_image()

    def update_image(self):
        self.angle += 3.1416/12
        if self.angle >= 3.1416/4:
            self.angle = -3.1416/4
        self.image.fill((0, 0, 0))
        if self.current_dir[1] > 0:
            facing = 3.1416 / 2
        elif self.current_dir[1] < 0:
            facing = -3.1416 / 2
        elif self.current_dir[0] < 0:
            facing = 3.1416
        else:
            facing = 0
        pygame.draw.polygon(self.image, (255, 255, 0), self.get_arc_points(facing), 0)

    def get_arc_points(self, facing):
        points = []
        for i in range(int(20*(facing + abs(self.angle))), int(20*(facing - abs(self.angle) + 2*3.1416))):
            points.append((int(25 + 25*math.cos(i/20)), int(25+25*math.sin(i/20))))
        points.append((25, 25))
        return points

    def check_pellet_collide(self):
        pelletList = pygame.sprite.spritecollide(self, pellets, True, collided=pellet_collide)
        self.num_pellets += len(pelletList)
        for i in pelletList:
            if isinstance(i, SuperPellet):
                print("super")
        if len(pellets.sprites()) <= 0:
            next_level()
        if len(pygame.sprite.spritecollide(self, ghosts, False, collided=pellet_collide)):
            print("you lose, score " + str(self.num_pellets))


def pellet_collide(sprite1, sprite2):
    return -20 < sprite1.rect.center[0] - sprite2.rect.center[0] < 20 and -20 < sprite1.rect.center[1] - sprite2.rect.center[1]  < 20


def setup_pellets():
    for i in pellets.sprites():
        i.kill()
    for pos in pellet_setup[0]:
        pellets.add(Pellet((pos[0]*25 + 50, pos[1]*25 +50)))
    for pos in pellet_setup[1]:
        pellets.add(SuperPellet((pos[0]*25+50, pos[1]*25 +50)))


def setup_walls():
    for rect in wall_setup:
        walls.add(Wall(rect))


def next_level():
    global pacman, level
    level += 1
    pacman.kill()
    pacman = Pacman()
    sprites.add(pacman)
    setup_pellets()


pacman = pygame.sprite.Sprite()
ghosts.add(Ghost((255, 100, 100)), Ghost((0, 255, 255)), Ghost((0, 255, 0)), Ghost((255, 0, 0)))
sprites.add(ghosts)
next_level()
setup_walls()
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
                pacman.next_dir = (0, -25)
            elif event.key == K_DOWN:
                pacman.next_dir = (0, 25)
            elif event.key == K_LEFT:
                pacman.next_dir = (-25, 0)
            elif event.key == K_RIGHT:
                pacman.next_dir = (25, 0)
    sprites.update(Clock.tick())
    win.fill((0, 0, 0))
    pellets.draw(win)
    walls.draw(win)
    sprites.draw(win)
    surf.blit(pygame.transform.scale(win, (surf.get_width() - offset[0]*2, surf.get_height() - offset[1]*2)), (offset[0], offset[1]))
    pygame.display.update()
