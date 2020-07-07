
import sys

import pygame
from pygame.locals import *

# 各个圆形的前景色列表
fore_back = [(0, 0, 255), (0, 0, 0), (255, 0, 0), \
             (255, 255, 0), (0, 255, 0)]
# 各个圆形的圆心坐标列表
point_list = [(215, 190), (340, 190), (465, 190), \
              (277, 240), (402, 240)]
FPS = 60

# 初始化
pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((640, 396))
pygame.display.set_caption("Pygame 奥运五环")
clock = pygame.time.Clock()

# 程序运行主题死循环
while 1:
    screen.fill((0, 163, 150))  # 1. 清屏
    # 2. 绘制： 圆形
    for i in range(5):
        pygame.draw.circle(screen, fore_back[i], point_list[i], 50, 6)

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:  # 判断为程序退出事件
            sys.exit()

    pygame.display.flip()  # 3.刷新
    clock.tick(FPS)



