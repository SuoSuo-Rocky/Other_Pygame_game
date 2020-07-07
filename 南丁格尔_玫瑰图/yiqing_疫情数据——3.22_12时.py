

import csv
import math
import os
import sys

# 导入pygame 及常量库
import pygame
from pygame import gfxdraw
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640, 820
FPS = 60
Dot = (WIDTH // 2, HEIGHT - 130) # 圆心点坐标
SCALE = 1                        # 收缩比例
BG_COLOR = pygame.Color("white") # 窗体背景色

def load_data():
    """ 加载数据 """
    dir =  os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir, "outbreak.csv")
    if not os.path.exists(file_path):
        raise (file_path, "文件不存在， 读取数据失败！")
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        res = list(reader)
    return res

def point(angle, radius, Dot = Dot):
    """ 获取圆上一点坐标 """
    x = math.cos(math.radians(angle)) * radius + Dot[0]
    y = math.sin(math.radians(angle)) * radius + Dot[1]
    return x, y

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("南丁格尔·玫瑰图_施伟")
clock = pygame.time.Clock()
# 创建字体对象
font = pygame.font.Font("songti.otf", 50 * SCALE)
data = load_data()
average_ang = 360 // (len(data) - 1) # 平均角度
font.set_bold(True)                  # 设置粗体
title = font.render("南丁格尔·玫瑰图", True, \
                    (255, 255, 255), (183, 23, 27))
title_rect = title.get_rect()
title_posi = (WIDTH// 2 - title_rect.width // 2, 20)

running = True
# 主体循环
while running:
    # 1. 清屏
    screen.fill(BG_COLOR)
    # 2. 绘制
    # 绘制标题背景框
    pygame.draw.rect(screen, (183, 23, 27, 100), (title_posi[0] - 8, \
                                           title_posi[1] - 8, \
                                           title_rect.width + 16, \
                                           title_rect.height + 16))
    # 绘制标题
    screen.blit(title, title_posi)
    # 绘制——南丁格尔玫瑰图
    for num, li in enumerate(data[1:], 1):
        angle01 = (num - 1) * average_ang - 90
        angle02 = num * average_ang - 90
        left = point(angle01, math.ceil(int(li[1]) * SCALE))
        right = point(angle02, math.ceil(int(li[1]) * SCALE))
        color = pygame.color.Color(li[2])
        pygame.draw.polygon(screen, color, [Dot, left, right])
    # 绘制中心填充区域
    pygame.draw.circle(screen, BG_COLOR, Dot, 25)
    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # 3.刷新
    pygame.display.update()
    clock.tick(FPS)
