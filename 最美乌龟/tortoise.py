

import os

import pygame
from pygame.locals import *

# 初始化
pygame.init()
# 游戏窗口居中
os.environ['SDL_VIDEO_CENTERED'] = '1'
# 创建游戏窗口
screen = pygame.display.set_mode((640, 396))
pygame.display.set_caption("levely Tortoise_SuoSuo")
# 背景颜色
bg_rgb = (0, 164, 150)
# 王八主体色
tor_rgb = (0, 100, 0)
# 王八的坐标位置
x, y = 260, 20

# 壳背多边形顶点列表
point_list = [(x+34, y+130), (x+86, y+160), (x+86, y+220), \
              (x+34, y+250), (x-18, y+220), (x-18, y+160)]


# 程序运行主逻辑循环
while 1:
    screen.fill(bg_rgb)  # 1. 清屏
    # 2.绘制
    # 画脑袋
    pygame.draw.ellipse(screen, tor_rgb, (x, y, 70, 100), 0)
    # 画眼睛
    pygame.draw.ellipse(screen, (0, 0, 0), (x+10, y+30, 10, 10), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x+50, y+30, 10, 10), 0)
    # 画尾巴
    pygame.draw.ellipse(screen, tor_rgb, (x, y+290, 60, 80), 0)
    pygame.draw.ellipse(screen, bg_rgb, (x+20, y+300, 60, 80), 0)
    # 画四条腿
    pygame.draw.circle(screen, tor_rgb, (x-50, y+115), 35, 0)  # 左上
    pygame.draw.circle(screen, tor_rgb, (x+115, y+115), 35, 0) # 右上
    pygame.draw.circle(screen, tor_rgb, (x-50, y+270), 35, 0)  # 左下
    pygame.draw.circle(screen, tor_rgb, (x+115, y+270), 35, 0) # 右下
    # 画壳子
    pygame.draw.ellipse(screen, (0, 50, 0), (x-66, y+70, 200, 240), 0)
    # 画壳贝多边形
    pygame.draw.polygon(screen, (255, 255, 0), point_list, 1)
    # 画线段
    pygame.draw.line(screen, (255, 255, 0), point_list[0], (point_list[0][0], point_list[0][1]-60), 1)
    pygame.draw.line(screen, (255, 255, 0), point_list[1], (point_list[1][0]+37, point_list[1][1]-20), 1)
    pygame.draw.line(screen, (255, 255, 0), point_list[2], (point_list[2][0]+37, point_list[2][1]+20), 1)
    pygame.draw.line(screen, (255, 255, 0), point_list[3], (point_list[3][0], point_list[3][1]+60), 1)
    pygame.draw.line(screen, (255, 255, 0), point_list[4], (point_list[4][0]-37, point_list[4][1]+20), 1)
    pygame.draw.line(screen, (255, 255, 0), point_list[5], (point_list[5][0]-37, point_list[5][1]-20), 1)

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:  # 判断为程序退出事件
            exit()


    # 轮询键盘事件
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        x -= 1
    if keys[K_UP]:
        y -= 1
    if keys[K_RIGHT]:
        x += 1
    if keys[K_DOWN]:
        y += 1
    # 重置壳背多边形顶点列表
    point_list = [(x + 34, y + 130), (x + 86, y + 160), (x + 86, y + 220), \
                  (x + 34, y + 250), (x - 18, y + 220), (x - 18, y + 160)]

    pygame.display.update()  # 3.刷新



