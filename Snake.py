import pygame
import random
import math
pygame.init()
clock = pygame.time.Clock()
# setup
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

windowHeight = 500
windowWidth = 500
win = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("SNAKE")
points = 0
fps = 20
pause = True
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('PAUSE', True, green, (0, 0, 0))
punteggio = font.render('POINTS: '+str(points), True, white, (0, 0, 0))
textRect = text.get_rect()
textRect.center = (windowHeight // 2, windowWidth // 2)

# setup snake
x = 250
y = 250
w = 20
h = 20
v = 10
gameOver = False
L = False
R = False
U = False
D = False
position = [(x, y, h, w)]

# apple setup
Apple_w = 10
Apple_h = 10
Apple_x = random.randint(0, windowWidth/10)*10
if Apple_x <= 20:
    Apple_x = 30
Apple_y = random.randint(0, windowHeight/10)*10
if Apple_y <= 20:
    Apple_y = 30

# funzione calcola distanza


def dis(x1, y1, x2, y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

# give another random position at the apple


def randApple():
    global Apple_x
    global Apple_y
    Apple_x = random.randint(0, windowWidth/10)*10
    if Apple_x <= 20:
        Apple_x = 30
    elif Apple_x >= windowWidth-20:
        Apple_x = windowWidth-30
    Apple_y = random.randint(0, windowHeight/10)*10
    if Apple_y <= 20:
        Apple_y = 30
    elif Apple_y >= windowHeight-20:
        Apple_y = windowHeight-30

# draw function


def drawGameWindow():
    global pause
    global position
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (Apple_x, Apple_y, Apple_w, Apple_h))
    for i in range(0, len(position)):
        if i == 0:
            pygame.draw.rect(win, (0, 0, 255), position[len(position)-i-1])
        pygame.draw.rect(win, (255, 255, 255), position[len(position)-i-1])
    if pause:
        win.blit(text, textRect)
    punteggio = font.render('POINTS: '+str(points), True, white, (0, 0, 0))
    win.blit(punteggio, (0, 0))
    pygame.display.update()


# reset the value of L R U D
def resetMovement():
    global L
    global U
    global R
    global D
    L = False
    R = False
    U = False
    D = False


# logic function, checks for collision and handles the movement
def logic():
    global L
    global U
    global R
    global D
    global x
    global y
    global w
    global h
    global v
    global gameOver
    global points
    global pause
    # check for collision with the apple
    if math.ceil(dis(x, y, Apple_x, Apple_y)) <= 15:
        points += 5
        randApple()
        position.append(position[0])
    # check for keyboard presses event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and R != True:
            resetMovement()
            L = True
            pause = False
        elif keys[pygame.K_RIGHT] and L != True:
            resetMovement()
            R = True
            pause = False
        elif keys[pygame.K_UP] and D != True:
            resetMovement()
            U = True
            pause = False
        elif keys[pygame.K_DOWN] and U != True:
            resetMovement()
            D = True
            pause = False
        if keys[pygame.K_SPACE]:
            resetMovement()
            pause = True
    # movement logic
    if L == True:
        x -= v
        position[0] = (x, y, h, w)
    elif R == True:
        x += v
        position[0] = (x, y, h, w)
    elif U == True:
        y -= v
        position[0] = (x, y, h, w)
    elif D == True:
        y += v
        position[0] = (x, y, h, w)
    for i in range(0, len(position)):
        position[len(position)-i-1] = position[len(position)-i-2]
    # Game over condition \ collision detection
    if x >= windowWidth-w or x <= 0 or y <= 0 or y >= windowHeight-h:
        gameOver = True

# main loop


def main():
    while gameOver == False:
        clock.tick(fps)
        logic()
        drawGameWindow()


main()
# closes the game

pygame.quit()
