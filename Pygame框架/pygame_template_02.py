
import sys

# 导入pygame 及常量库
import pygame
from pygame.locals import *

# 游戏中的一些常量定义
SIZE = WIDTH, HEIGHT = 640, 396
FPS = 60
TITLE = "Hello__施伟"

# 颜色常量定义
BG_COLOR = 25, 102, 173

# 初始化
pygame.init()
pygame.mixer.init()

# 创建游戏窗口
screen = pygame.display.set_mode(SIZE)
# 设置窗口标题
pygame.display.set_caption(TITLE)
# 创建时间管理对象
clock = pygame.time.Clock()
# 创建字体对象
font = pygame.font.SysFont(None, 60, )

running = True
# 程序运行主体循环
while running:
    # 1. 清屏(窗口纯背景色画纸的绘制)
    screen.fill(BG_COLOR)  # 先准备一块画布
    # 2. 绘制

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:  # 判断点击窗口右上角“X”
            pygame.quit()       # 退出游戏，还原设备
            sys.exit()          # 程序退出

    # 3.刷新
    pygame.display.update()
    # 设置帧数
    clock.tick(FPS)

# 循环结束后，退出游戏
pygame.quit()