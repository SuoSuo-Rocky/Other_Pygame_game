



import sys

# 导入pygame 及常量库
import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640, 396
FPS = 60

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("打地鼠__施伟")
clock = pygame.time.Clock()
# 创建字体对象
font = pygame.font.SysFont(None, 60, )

HEAD_EVENT = pygame.USEREVENT
is_running = True

pygame.time.set_timer(HEAD_EVENT, 1000)


# 主体循环
while True:
    # 1. 清屏
    screen.fill((25, 102, 173))
    # 2. 绘制

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == HEAD_EVENT:
            print("is =" , HEAD_EVENT)


    # 3.刷新
    pygame.display.update()
    clock.tick(FPS)
