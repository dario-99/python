import pygame
pygame.init()
#windows setup
wH = 1000
wW = 1000
size = (wW, wH) 
win = pygame.display.set_mode (size)
pygame.display.set_caption("TIC TAC TOE")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)

#colors
black = (0,0,0)
blue = (0,0,255)
white = (255,255,255)
red = (255,0,0)

#game setup
gameOver = False
array = [   [0,0,0], 
            [0,0,0],
            [0,0,0]
]
turn = 1
end = 'NULL'

#function check who win and returns the winnin player(0 NO WIN, 1 FIRST PLAYER, 2 SECOND PLAYER WIN, 3 DRAW)
def checkWin(grid):
    winner = 0
    draw = True
    if grid[0] == [1,1,1] or grid[1] == [1,1,1] or grid[2] == [1,1,1] or [grid[0][0],grid[1][1],grid[2][2]] == [1,1,1] or [grid[0][2],grid[1][1],grid[2][0]] == [1,1,1] or [grid[0][0],grid[1][0],grid[2][0]] == [1,1,1] or [grid[0][1],grid[1][1],grid[2][1]] == [1,1,1] or [grid[0][2],grid[1][2],grid[2][2]] == [1,1,1]:
        winner = 1
    elif grid[0] == [2,2,2] or grid[1] == [2,2,2] or grid[2] == [2,2,2] or [grid[0][0],grid[1][1],grid[2][2]] == [2,2,2] or [grid[0][2],grid[1][1],grid[2][0]] == [2,2,2] or [grid[0][0],grid[1][0],grid[2][0]] == [2,2,2] or [grid[0][1],grid[1][1],grid[2][1]] == [2,2,2] or [grid[0][2],grid[1][2],grid[2][2]] == [2,2,2]:
        winner = 2
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                draw = False
    if draw:
        return 3
    else:
        return winner
#main loop
while not gameOver:
    clock.tick(20)
    #draw grid
    win.fill(black)
    if end == 'NULL':
        for i in range(3):
            for j in range (3):
                if array[i][j] == 1:
                    pygame.draw.circle(win, red, ((2*j+1) * wW // 6,(2*i+1) * wH // 6), wW // 6 - 20, 10)
                if array[i][j] == 2: 
                    pygame.draw.line(win, blue, (j*wW // 3, i*wH // 3), ((j+1)*wW // 3, (i+1)*wH // 3), 10)  
                    pygame.draw.line(win, blue, ((j+1)*wW // 3, i*wH // 3), (j*wW // 3, (i+1)*wH // 3), 10)
        pygame.draw.line(win, white, (0,wH//3), (wW,wH//3), 20)
        pygame.draw.line(win, white, (0,2*wH//3), (wW,2*wH//3), 20)
        pygame.draw.line(win, white, (wW//3,0), (wW//3,wH), 20)
        pygame.draw.line(win, white, (2*wW//3,0), (2*wW//3,wH), 20)
        pygame.display.update()
        #Game logic
        a = checkWin(array)
        if a == 1:
            print('player 1 WON')
            end = 'PLAYER 1 WON'
        elif a == 2:
            print('player 2 WON')
            end = 'PLAYER 2 WON'
        if a == 3:
            print('DRAW!')
            end = 'DRAW!'
        else:#continue playing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                if pygame.mouse.get_pressed() == (1,0,0):
                        x,y = pygame.mouse.get_pos()
                        mx = 0
                        my = 0
                        for i in range(3):
                            if x>(i*wW // 3) and x <((i+1)*wW//3):
                                my = i
                        for j in range(3):
                            if y>(j*wH // 3) and y <((j+1)*wH//3):
                                mx = j

                        if array[mx][my] == 0:
                            array[mx][my] = turn
                            if turn == 1:
                                turn = 2
                            else: 
                                turn = 1
    else:
        win.fill(red)
        text = font.render(end, True, blue, red)
        textRect = text.get_rect()
        textRect.center = (wH // 2, wW // 2)                   
        win.blit(text, textRect)
        pygame.display.update()  
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True 
                if pygame.mouse.get_pressed() == (1,0,0):
                    array = [   [0,0,0], 
                                [0,0,0],
                                [0,0,0]
                    ]
                    turn = 1
                    end = 'NULL'
pygame.quit()