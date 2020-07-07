


import math

import pygame
from pygame.locals import *



def draw_txt(text, posi, fgcolor, bgcolor, size):
    """ 绘制文本 """
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, fgcolor, bgcolor)
    screen.blit(img, posi)

def draw_heart(dx, dy, r, is_border = True):
    """ 绘制心型图
        心型线的极坐标方程： ρ = a (1 + cos(θ))
    """
    i = 0  # 点的密度
    while r >= 1:
        while i <= 190:
            m = i
            n = -r * (((math.sin(i) * math.sqrt(abs(math.cos(i)))) / \
                        (math.sin(i) + 1.46)) - 2 * math.sin(i) + 1.83)
            x = round(n * math.cos(m) + dx)
            y = round(n * math.sin(m) + dy)
            # 绘制心型图案边框为黑色
            if is_border:
                pixel[x][y] = pygame.Color("black")
            else:
                pixel[x][y] = pygame.Color("red")
            i += 0.03
        is_border = False
        r -= 1
        i = 0

def draw_line(dot,color = pygame.Color("gold"), \
              line_width = 9):
    """ 绘制线段 """
    pygame.draw.line(screen, color, dot[0], dot[1], line_width)

size = width, height = 640,396
pygame.init()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Love ShiWei")
pixel = pygame.PixelArray(screen)   # **********************

screen.fill(pygame.Color("white"))
dx, dy = width // 2 - 30, 76   # 位置坐标
r, i = 70, 0
# 定义线段的端点坐标
line01 = [(20, 23), (153, 81)]
slope =  (line01[1][1] - line01[0][1]) / \
         (line01[1][0] - line01[0][0])    # 斜率
line02_first = (410, 182)
line02_end = [586, \
             (586 - line02_first[0]) * slope + \
              line02_first[1]]
line03 = [line02_end, (line02_end[0] - 18, \
                       line02_end[1] - 35)]
line04 = [line02_end, (line02_end[0] - 43, \
                       line02_end[1] + 15)]
screen.fill(pygame.Color("white"))

# 绘制第一个心型图
draw_heart(dx, dy, r)
dx += 100
dy += 30
r, i = 70, 0
is_border = True
# 绘制第二个心型图
draw_heart(dx, dy, r)
# 绘制心语
del pixel     #************************************
draw_txt("I love you", (width // 2 - 120, dy), \
          pygame.Color("black"), pygame.Color("red"), 70)
pygame.display.update()
# 绘制箭头
draw_line(line01)
draw_line([line02_first, line02_end])
draw_line(line03)
draw_line(line04)

while True:
    for eve in pygame.event.get():
        if eve.type == QUIT:
            exit()