import pygame
import random
pygame.init()
#window constants
wH=500
wW=1000
size = (wW, wH)
screen = pygame.display.set_mode(size)
#pygame clock
clock = pygame.time.Clock()

finished = False
#setup
v = []
for i in range (wW):
    v.append(random.randint(0,wH))
i = 0

def quickSort(Vet, Sin, Des):
    if Sin >= Des:
        return
    I, J = Sin, Des
    Pivot = Vet[(Sin+Des)//2]
    Primo = True
    while( Primo or I<=J ):
        Primo = False
        while( Vet[I]<Pivot ):  I+=1
        while( Vet[J]>Pivot ):  J-=1
        if( I<=J ):
            Vet[I], Vet[J] = Vet[J], Vet[I]
            I+=1
            J-=1
        clock.tick(120)
        screen.fill((0,0,0))
        k = 0
        for k in range (wW):
            pygame.draw.line(screen,(255,255,255),(k,wH), (k,Vet[k]), 1)
        pygame.display.update()
    quickSort(Vet, Sin, J)
    quickSort(Vet, I, Des)

quickSort(v,0,len(v)-1)
## """   
##for i in range (wW):
##    j=0
##    while j<wW-i-1:
##        if v[j] < v[j+1]:
##            v[j], v[j+1] = v[j+1], v[j]
##        j+=1    
##        clock.tick(1000)
##        screen.fill((0,0,0))
##        k = 0
##        for k in range (wW):
##            pygame.draw.line(screen,(255,255,255),(k,wH), (k,v[k]), 1)
##        pygame.display.update()
####while not finished:
##    
##    
####    if i<wW:
####        j=0
####        while j<wW-i-1:
####            if():
####                temp = v[j]
####                v[j] = v[j+1]
####                v[j+1] = v[j]
####            
####    i+=1
pygame.quit()


 
