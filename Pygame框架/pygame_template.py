
import sys

import pygame
from pygame.locals import *

# 初始化
pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((640, 396))
# 创建字体对象
font = pygame.font.SysFont(None, 60,)
# 创建文本图像
mingri = font.render("Hello Pygame World", True, (0, 0, 0))

# 程序运行主题死循环
while 1:
    screen.fill((80, 133, 188))     # 1. 清屏
    screen.blit(mingri, (150, 160))  # 2. 绘制

    for event in pygame.event.get(): # 事件索取
        if event.type == QUIT:       # 判断为程序退出事件
            sys.exit()

    pygame.display.update()         # 3.刷新


    
