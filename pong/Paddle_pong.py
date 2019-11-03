import pygame
class Paddle:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rectangle = (x, y, w, h)
        self.color = color
        self.vel = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rectangle)

    def update(self, wH):
        self.rectangle = (self.x, self.y, self.w, self.h)
        self.y += self.vel
        if self.y < 0:
            self.y = 0
        elif self.y > wH - self.h:
            self.y = wH - self.h

    def move (self, vel):
        self.vel = vel
    
    def reset (self, x, y):
        self.x = x
        self.y = y

    
