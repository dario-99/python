import pygame
import random
import math
# pygame setup
pygame.init()
wW = 600
wH = 600
size = (wW, wH)
win = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("MINESWEEPER")
font = pygame.font.Font('freesansbold.ttf', wW//25)
# color setup
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# game setup
# 10*10 grid
gameOver = False
rows = 10
cols = 10
w = wW // rows
h = wW // cols
bombs = rows + cols
map = []
for i in range(rows):
    v = []
    for j in range(cols):
        cell = {
            "nBombs": 0,
            "show": False,
            "flag": False
        }
        v.append(cell)
    map.append(v)
# put bombs
while bombs > 0:
    randX = random.randint(0, rows-1)
    randY = random.randint(0, cols-1)
    if map[randX][randY]["nBombs"] != 10:
        map[randX][randY]["nBombs"] = 10
        bombs -= 1
    else:
        pass
# distance function


def distance(x, y, j, k):
    dis = math.sqrt(pow(x-j, 2) + pow(y-k, 2))
    return dis
# check how many bombs nearby


def checkNearBombs(x, y):
    counter = 0
    for i in range(rows):
        for j in range(cols):
            if map[i][j]["nBombs"] == 10:
                if distance(i, j, x, y) <= 1.5:
                    counter += 1
    return counter


# fill with numbers
for i in range(rows):
    for j in range(cols):
        if map[i][j]["nBombs"] != 10:
            nearBombs = checkNearBombs(i, j)
            map[i][j]["nBombs"] = nearBombs
while not gameOver:
    clock.tick(10)
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if pygame.mouse.get_pressed() == (1, 0, 0):
            x, y = pygame.mouse.get_pos()
            mx = 0
            my = 0
            for i in range(rows):
                if x > (i*w) and x < ((i+1)*w):
                    my = i
            for j in range(cols):
                if y > (j*h) and y < ((j+1)*h):
                    mx = j
            if map[mx][my]["show"] == False:
                map[mx][my]["show"] = True
            if map[mx][my]["nBombs"] == 10:
                gameOver = True
        if pygame.mouse.get_pressed() == (0, 0, 1):
            x, y = pygame.mouse.get_pos()
            mx = 0
            my = 0
            for i in range(rows):
                if x > (i*w) and x < ((i+1)*w):
                    my = i
            for j in range(cols):
                if y > (j*h) and y < ((j+1)*h):
                    mx = j
            if map[mx][my]["flag"] == False:
                map[mx][my]["flag"] = True
            else:
                map[mx][my]["flag"] = False
    # draw the map
    win.fill((0, 0, 0))
    for i in range(rows):
        for j in range(cols):
            if map[i][j]["show"] == False and map[i][j]["flag"] == False:
                pos = (j*w, i*h, h-1, w-1)
                pygame.draw.rect(win, white, pos)
            elif map[i][j]["show"] == True:
                val = map[i][j]["nBombs"]
                pos = (j*w, i*h, h-1, w-1)
                if val != 10:
                    text = font.render(str(val), True, (0, 0, 0), (0, 255, 0))
                    pygame.draw.rect(win, (0, 255, 0), pos)
                else:
                    text = font.render('#', True, (0, 0, 0), (255, 0, 0))
                    pygame.draw.rect(win, (255, 0, 0), pos)
                textRect = text.get_rect()
                textRect.center = (j*w + w//2, i*h + w//2)
                win.blit(text, textRect)
            else:
                pos = (j*w, i*h, h-1, w-1)
                text = font.render('?', True, (0, 0, 0), white)
                pygame.draw.rect(win, white, pos)
                textRect = text.get_rect()
                textRect.center = (j*w + w//2, i*h + w//2)
                win.blit(text, textRect)
        pygame.draw.line(win, (0, 0, 0), (i*w, (j+1)*h), ((i+1)*w, (j+1)*h), 2)
        pygame.draw.line(win, (0, 0, 0), ((i+1)*w, j*h), ((i+1)*w, (j+1)*h), 2)

    pygame.display.update()
pygame.quit()
