
import sys

# 导入pygame 及常量库
import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640, 420
FPS = 60












pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello__施伟")
clock = pygame.time.Clock()
# 创建字体对象
font = pygame.font.SysFont(None, 60, )

running = True
# 主体循环
while running:
    # 1. 清屏
    screen.fill((25, 102, 173))
    # 2. 绘制

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # 3.刷新
    pygame.display.update()
    clock.tick(FPS)
