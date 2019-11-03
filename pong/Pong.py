import pygame
from Ball_pong import Ball
from Paddle_pong import Paddle
import os.path

pygame.init()

# colors
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)

# windows setup
wH = 500
wW = 500
size = (wW, wH)
win = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")
clock = pygame.time.Clock()

#setup
paddleW = wW // 20
paddleH = wH // 7
leftPad = Paddle(10, wH//2 - paddleH // 2, paddleW, paddleH, white)
rightPad = Paddle(wW - paddleW - 10, wH//2 - paddleH // 2, paddleW, paddleH, white)
ball = Ball(white, wW//2, wH//2, 10, 4)
gameOver = False
p1 = 0
p2 = 0
p1dir = 0
p2dir = 0

#scores text setup
font = pygame.font.Font('freesansbold.ttf', 32)

#score SOUND setup
C = os.path.abspath(os.path.dirname(__file__))
scoreSound = pygame.mixer.music.load(C + '/sounds/score.mp3')

#while not gameOver
while not gameOver:
    clock.tick(100)
    #keyboard presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            p1dir = -5
        elif keys[pygame.K_s]:
            p1dir = 5
        else:
            p1dir = 0
        if keys[pygame.K_UP]:
            p2dir = -5
        elif keys[pygame.K_DOWN]:
            p2dir = 5
        else:
            p2dir = 0
    leftPad.move(p1dir)
    rightPad.move(p2dir)

    #update logic
    leftPad.update(wH)
    rightPad.update(wH)
    ball.update()
    res = ball.hitWall(wW, wH)
    if res == 1:
        p1 += 1
        pygame.mixer.music.play()
    elif res == 2:
        p2 += 1
        pygame.mixer.music.play()
    if res != 0:
        ball.reset(wW//2, wH//2)
        leftPad.reset(10, wH//2 - paddleH // 2)
        rightPad.reset(wW - paddleW - 10, wH//2 - paddleH // 2)
    ball.hitPaddle(leftPad, 'left')
    ball.hitPaddle(rightPad, 'right')

    #draw
    win.fill((0,0,0))
    leftPad.draw(win)
    rightPad.draw(win)
    ball.draw(win)
    
    #draw Scores
    text = font.render(str(p1), True, white)
    textRect = text.get_rect()
    textRect.center = (50, 50)
    
    win.blit(text, textRect)

    text = font.render(str(p2), True, white)
    textRect = text.get_rect()
    textRect.center = (wW - 50, 50)
    
    win.blit(text, textRect)

    pygame.display.update()
scoreSound.unload()
pygame.quit()