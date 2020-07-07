


import math

import pygame
from pygame.locals import *


def draw_txt(text, posi, fgcolor, bgcolor, size):
    """ 绘制文本 """
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, fgcolor, bgcolor)
    screen.blit(img, posi)


def draw_line(dot,color = pygame.Color("gold"), \
              line_width = 9):
    """ 绘制线段 """
    pygame.draw.line(screen, color, dot[0], dot[1], line_width)


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
                pygame.draw.circle(screen, pygame.Color("black"), \
                                   (x, y), 2, 2)
            else:
                pygame.draw.circle(screen, pygame.Color("red"), \
                                   (x, y), 1, 0)
            i += 0.03
        is_border = False
        r -= 1     # 减小心型图的大小
        i = 0      # 下一个心型图从头开始绘制


size = width, height = 640,396
dx, dy = width // 2 - 30, 76   # 心型图位置坐标
r, i = 70, 0                   # 心型图的大小
# 定义四条线段的各个端点坐标
line01 = [(20, 23), (160, 89)]
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

# 初始化及参数设置
pygame.init()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Love ShiWei")
screen.fill(pygame.Color("white"))

# 绘制左上方线段
draw_line(line01)
# 绘制第一个心型图
draw_heart(dx, dy, r)
dx += 100
dy += 30
r, i = 70, 0
is_border = True
# 绘制第二个心型图
draw_heart(dx, dy, r)
# 绘制心语
draw_txt("I love you", (width // 2 - 120, dy), \
          pygame.Color("black"), pygame.Color("red"), 70)
# 绘制右下方箭头
draw_line([line02_first, line02_end])
draw_line(line03)
draw_line(line04)
pygame.display.update()  # 窗口像素刷新

# 使窗口页面卡住
while True:
    for eve in pygame.event.get():
        if eve.type == QUIT:
            exit()
