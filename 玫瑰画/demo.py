"""
http://xuxzmail.blog.163.com/blog/static/251319162009739563225/
https://jingyan.baidu.com/article/b87fe19e44cfa55219356869.html ——  MATLAB
"""

from math import sin, cos

import pygame
from pygame.locals import *

o = 0.00
r1 = 300
r2 = 130
r3 = r1 - r2
r4 = 80
k1 = r3 / r1
k2 = r2 / r1
ps = []
pygame.init()
zt3 = zt1 = pygame.font.SysFont('stkaiti', 20)


def prt(font, text, x, y, color=(255, 255, 255)):
    img = font.render(text, True, color)
    scr.blit(img, (x, y))


text = "大圆：" + str(r1) + "小圆:" + str(r3) + "圆孔：" + str(r4)

scr = pygame.display.set_mode((600, 600))
pygame.display.set_caption("繁花曲线")

while True:
    for eve in pygame.event.get():
        if eve.type == QUIT:
            exit()
    scr.fill(pygame.Color("white"))
    pos = (round(300 + r2 * cos(k1 * o) + r4 * cos(k2 * o)), round(300 + r2 * sin(k1 * o) - r4 * sin(k2 * o)))
    ps.append(pos)
    prt(zt3, text, 12, 12, color=(0, 0, 0))
    for i in ps:
        pygame.draw.circle(scr, pygame.Color("blue"), i, 1, 0)
    pygame.display.update()
    o = o + 0.02
    # if o < 0.01:
    #     o = o + 0.03
    # else:
    #     o += 0
