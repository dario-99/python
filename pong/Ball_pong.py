import random
import math 
import pygame

class Ball:
    def __init__ (self, color, x, y, radius, vel):
        self.color = color
        self.x = x
        self.y = y
        if random.random() <= 0.5:
            self.angle = random.uniform(math.pi - math.pi/4, math.pi + math.pi/4)
        else:
            self.angle = random.uniform(-math.pi/4, math.pi/4)
        self.vel = vel
        self.radius = radius
        self.counter = 0
    def update (self):
        if not (self.counter < 105):
            self.velX = self.vel * math.cos(self.angle)
            self.velY = self.vel * math.sin(self.angle)
            self.x += self.velX
            self.y += self.velY
        self.counter += 1
    def draw(self, win):
        pygame.draw.circle(win, (255,255,255), (int(self.x),int(self.y)), self.radius)
    def hitWall(self, wW, wH):
        if self.x >= wW:
            return 1
        elif self.x <= 0:
            return 2
        elif self.y <= 0 or self.y >= wH:
            self.angle *= -1
        return 0
    def reset(self, x, y):
        if random.random() <= 0.5:
            self.angle = random.uniform(math.pi - math.pi/4, math.pi + math.pi/4)
        else:
            self.angle = random.uniform(-math.pi/4, math.pi/4)
        self.x = x
        self.y = y
        self.counter = 0
    def hitPaddle(self, paddle, l):
        if l == 'left':
            if self.x <= paddle.x + paddle.w and self.x >= paddle.x and paddle.y - self.y <= 0 and paddle.y - self.y >= -paddle.h :
                self.angle = -(math.pi/4) - (math.pi/(2*paddle.h))*(paddle.y - self.y)
                self.x = paddle.x + paddle.w + self.radius

        elif l == 'right':
            if self.x >= paddle.x and self.x <= paddle.x + paddle.w and paddle.y - self.y <= 0 and paddle.y - self.y >= -paddle.h:
                self.angle = -(3/4)*math.pi + (math.pi/(2*paddle.h))*(paddle.y - self.y)
                self.x = paddle.x - self.radius