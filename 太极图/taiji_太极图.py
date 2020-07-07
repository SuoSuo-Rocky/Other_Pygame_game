


import math
import sys
from functools import lru_cache

# 导入pygame 及常量库
import pygame
from pygame.locals import *


SIZE = WIDTH, HEIGHT = 640, 396
FPS = 60
BG_COLOR = pygame.Color("white")
BlACK = pygame.Color("black")
WHITE = pygame.Color("white")
FONT_BG_COLOR = (183, 23, 27, 100)

@lru_cache(maxsize=360 * 6)
def cul_posi(angle, posi, radius):
    """ 计算圆心坐标 """
    dot_x = round(math.cos(math.radians(angle)) * radius + posi[0])
    dot_y = round(math.sin(math.radians(angle)) * radius + posi[1])
    return (dot_x, dot_y)


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("太极图__施伟")
clock = pygame.time.Clock()
# 创建字体对象
font = pygame.font.Font("songti.otf", 60, )
# 太极图半径
radius = 160
# 起始角度
angle = 30
# 太极图中心坐标
posi = (WIDTH // 2 - 60, HEIGHT // 2)
font.set_bold(True)
font_01 = font.render("阴", True, WHITE, FONT_BG_COLOR)
font_02 = font.render("阳", True, WHITE, FONT_BG_COLOR)
font_03 = font.render("图", True, WHITE, FONT_BG_COLOR)
font_rect = font_01.get_rect()
font_linesize = font.get_linesize()
print("font_rect = ", font_rect)  # 68, 61
print("font_linesize = ", font_linesize)  # 120
title_posi = (500, 40)

# 主体循环
while True:
    # 1. 清屏
    screen.fill(BG_COLOR)
    # 2. 绘制
    # 绘制实心黑色圆
    pygame.draw.circle(screen, BlACK, posi, radius)
    # 计算长方形四个点的坐标
    dot_x1, dot_y1 = cul_posi(angle, posi, radius)
    dot_x4, dot_y4 = cul_posi(angle + 180, posi, radius)
    dot_x2, dot_y2 = cul_posi(angle + 90, (dot_x1, dot_y1), radius)
    dot_x3, dot_y3 = cul_posi(angle + 90, (dot_x4, dot_y4), radius)
    # 绘制填充(与窗体背景色相同)四边形(长方形)
    pygame.draw.polygon(screen, BG_COLOR, [(dot_x1, dot_y1), \
                                            (dot_x2, dot_y2), \
                                            (dot_x3, dot_y3), \
                                            (dot_x4, dot_y4),])
    # 绘制大的实心黑圆边框， 用以显示被填充矩形覆盖掉的大圆边框
    pygame.draw.circle(screen, BlACK, posi, radius, 1)
    # 计算两个小圆的圆心坐标
    posi_x1, posi_y1 = cul_posi(angle, posi, radius / 2)
    posi_x2, posi_y2 = cul_posi(angle, (dot_x4, dot_y4), radius / 2)
    # 绘制两个填充小圆
    pygame.draw.circle(screen, BlACK, (posi_x1, posi_y1), radius // 2)
    pygame.draw.circle(screen, BG_COLOR, (posi_x2, posi_y2), radius // 2)
    # 绘制阴阳各自的填充小圆心
    pygame.draw.circle(screen, BlACK, (posi_x2, posi_y2), 16)
    pygame.draw.circle(screen, BG_COLOR, (posi_x1, posi_y1), 16)
    # 阴阳转换
    angle += 1
    if angle == 361:
        angle = 0
    # 绘制标题背景框
    pygame.draw.rect(screen, FONT_BG_COLOR, (title_posi[0] - 8, \
                                           title_posi[1] - 18, \
                                           font_rect.width + 16, \
                                           16 + 100 * 3))
    # 绘制字体
    screen.blit(font_01, title_posi)
    screen.blit(font_02, (title_posi[0], title_posi[1] + 100))
    screen.blit(font_03, (title_posi[0], title_posi[1] + 100 * 2))

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    fps = clock.get_fps()
    print(f"fps = {fps}")

    # 3.刷新
    pygame.display.update()
    clock.tick(FPS)

