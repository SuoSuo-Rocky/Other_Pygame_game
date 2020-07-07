
import sys

# 导入pygame 及常量库
import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640, 396
FPS = 60

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello__施伟")
clock = pygame.time.Clock()
# 创建字体对象
font = pygame.font.SysFont(None, 60, )
draw_switch = False  # 绘制的开关
dot_li = []   # 曲线的集合
line_width = 3
pos_li = []


running = True
# 主体循环
while running:
    # 1. 清屏
    screen.fill((25, 102, 173))
    pos = pygame.mouse.get_pos()
    mouses = pygame.mouse.get_pressed()
    if mouses == (1, 0, 0):
        if pos not in pos_li:
            pos_li.append(pos)
    # 2. 绘制
    for li in dot_li:
        for dot in range(0, len(li) - 1):
            pygame.draw.line(screen, pygame.Color('red'), li[dot], li[dot + 1], line_width)
    for dot in range(0, len(pos_li) - 1):
        pygame.draw.line(screen, pygame.Color('red'), pos_li[dot], pos_li[dot + 1], line_width)

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                dot_li.append(pos_li)
                pos_li = []
    # 3.刷新
    pygame.display.update()
