import pygame
from pygame.locals import *
pygame.init()


#шрифты
font = pygame.font.SysFont('Arial Black',20)#добавляем шрифт с размерам на экран


#настройки экрана
gamedisplay = pygame.display.set_mode((900,500))
pygame.display.set_caption('catch the chiken 0.0.1 Beta')

#korona
korona = pygame.image.load('korona.png')
korona = pygame.transform.scale(korona,(100,100))
korona_rect=korona.get_rect()
korona_rect.center=(630,135)
#flower
flower = pygame.image.load('flower.jpg')
flower = pygame.transform.scale(flower,(100,100))
#fon
fon = pygame.image.load('468.png')
fon = fon.subsurface((0,0,468,336))
fon_rect=fon.get_rect()
fon_rect.bottom = 500
fon_rect.centerx = 450
#chiken
fon1 = pygame.image.load('kirillach.png')
fon1_rect=fon.get_rect()
fon1_rect.bottom = 500
fon1_rect.centerx = 0
stop=False
text = font.render(' STOOOP!!!!',True,(84, 84, 84))
retext = font.render('nooooooooooo!', True, (84, 84, 84))
regtext = font.render('you Win!', True, (0,50,220))


def run():
    fon1_rect.centerx+=10
    if fon1_rect.left>900:
        fon1_rect.centerx=-100

game = True
while game:
    if not stop:

        run()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            stop=not stop
        if event.type == QUIT:
            game = False




    gamedisplay.fill((255, 255,255))
    gamedisplay.blit(text, (50, 50))
    gamedisplay.blit(fon,fon_rect)
    gamedisplay.blit(fon1,fon1_rect)
    gamedisplay.blit(flower,(300,50))
    if stop:
        rastoanie=abs(450-fon1_rect.centerx)
        print(rastoanie)
        if rastoanie<11:
            gamedisplay.blit(regtext, (100, 200))
            gamedisplay.blit(korona,korona_rect)
        else:
            gamedisplay.blit(retext, (100,100))

    pygame.display.update()
pygame.quit()