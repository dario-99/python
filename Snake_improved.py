import pygame
import random
pygame.init()


class Snake:
    # costruttore
    def __init__(self, name = 'Snake', x=2, y=2, color=(255, 255, 255)):
        self.name = name
        self.size = 1
        self.height = 20
        self.width = 20
        self.position = [[(x+1)*20-10, (y+1)*20-10, self.width, self.height]]
        self.color = color
        self.L = False
        self.R = False
        self.U = False
        self.D = False
        self.points = 0
    # incrementa la dimensione del serpente
    def incrementSize(self):
        self.size += 1
        self.position.append(self.position[self.size-2])

    #disegna il serpente
    def draw(self, win):
        for i in range(0, self.size):
            pygame.draw.rect(win, self.color, self.position[i])
            

    #fa l' update delle posizioni
    def update(self):
        for i in range(0, self.size):
            self.position[self.size-i-1] = self.position[self.size-i-2]
            print ('quadrato '+str(self.size-i-1)+' '+str(self.position[self.size-i-1]))
        print('#######################################################')
            
    #aumenta di una casella la testa del serpente
    def move(self):
        if self.L:
            self.position [0][0] -= self.width
        if self.R:
            self.position [0][0] += self.width
        if self.U:
            self.position [0][1] -= self.height
        if self.D:
            self.position [0][1] += self.height
        
            
    #stoppa il serpente
    def stop(self):
        self.L = False
        self.R = False
        self.U = False
        self.D = False

    #cambia direzione del serpente
    def changeDirection(self, direction):
        if direction == 'L' and self.R != True :
            self.stop()
            self.L = True
        elif direction == 'R' and self.L != True:
            self.stop()
            self.R = True
        elif direction == 'U' and self.D != True:
            self.stop()
            self.U = True
        elif direction == 'D' and self.D != True:
            self.stop()
            self.D = True
        

    #check se  la testa colpisce l'oggetto nella posizione (x,y)
    def checkCollision(self, x, y):
        if self.position[0][0] == x and self.position[0][1] == y:
            return True
        else :
            return False
    #check se colpisci i boundaries
    def checkBoundaries(self):
        if self.position[0][0] < 10 or self.position[0][0] >= 480 or self.position[0][1] < 10 or self.position[0][1] >= 480:
            return True
        else:
            return False
    #check se il serpente e presente nella posizione (x,y)
    def checkInPosition(self,x,y): 
        for i in range(0,self.size):
            if self.position[i][0] == x and self.position[i][1] == y:
                return True
        return False
        

    #aumento punteggio di n points
    def scorePoint(self,points):
        self.points += points

class Apple:
    #costruttore
    def __init__(self, x, y, color = (255,0,0)):
        self.x = x
        self.y = y
        self.height = 20
        self.width = 20
        self.color = color
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.height, self.width))
    def changePosition(self, x, y):
        self.x = x
        self.y = y
    
#Logic function
def logic(win, snake, apple, done):
    snake.update()
    #check collision with apple
    if snake.checkCollision(apple.x, apple.y):
        snake.scorePoint(5)
        snake.incrementSize()
        x = (random.randint(0,23) + 1)* 20 - 10
        y = (random.randint(0,23) + 1)* 20 - 10
        while snake.checkInPosition(x, y):#check se spawna la mela gia nel serpente se capita crea un altra mela fin quando non trova una pos libera
            x = (random.randint(0,23) + 1)* 20 - 10
            y = (random.randint(0,23) + 1)* 20 - 10
        apple.changePosition(x,y)
    
    #check for keyboard presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake.changeDirection('L')
        elif keys[pygame.K_RIGHT]:
            snake.changeDirection('R')
        elif keys[pygame.K_UP]:
            snake.changeDirection('U')
        elif keys[pygame.K_DOWN]:
           snake.changeDirection('D')
        if keys[pygame.K_SPACE]:
            snake.stop()
    #muove il serpente
    snake.move()

    #check if the snake passes the boundaries
    if snake.checkBoundaries():
        done = True
    draw(win, apple, snake)
    return done
#draw function
def draw(win, apple, snake):
    win.fill((0, 0, 0))
    apple.draw(win)
    snake.draw(win)
    pygame.display.update()
# main loop
def main():
    # window setup
    winHeight = 500
    winWidth = 500
    win = pygame.display.set_mode((winWidth, winHeight))
    clock = pygame.time.Clock()
    fps = 10
    done = False

    # color setup
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (255, 255, 255)

    #create snake
    snake = Snake()
    x = (random.randint(0,23) + 1)* 20 - 10
    y = (random.randint(0,23) + 1)* 20 - 10
    apple = Apple(x,y)
    # while loop
    while not done:
        clock.tick(fps)
        done = logic(win, snake, apple, done)


main()
pygame.quit()
