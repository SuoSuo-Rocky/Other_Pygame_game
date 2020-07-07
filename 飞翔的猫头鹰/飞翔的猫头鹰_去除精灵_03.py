#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import random

import pygame
from pygame.locals import *

__auther__ = "SuoSuo"
__version__ = "master_v1"

# 窗口背景色
BG_COLOR = pygame.Color(0, 163, 150)
# 帧率
FPS = 50
# 屏幕尺寸
SCREEN_WIDTH = 398
SCREEN_HEIGHT = 640
# 猫头鹰尺寸
BIRD_WIDTH = 20
BIRD_HEIGHT = 20
# 地面高度
FLOOR_HEIGHT = 80
# 跳跃时加速度运动的总时长
VARIABLE_LEN_TIME = 6
# 游戏有效高度
BASE_HEIGHT = SCREEN_HEIGHT - FLOOR_HEIGHT
# 挡板移动速度
BAFFLE_SPEED = 1
# 挡板尺寸
BAFFLE_WIDTH = 50
BAFFLE_HEIGHT = 500
# 上下挡板最大间隔
MAX_BAFFLE_INTERVAL = 250
# 水平挡板间隔
VERTICAL_BAFFLE_INTERVAL = 100
# 上下挡板组的数量
BAFFLE_GROUP_NUM = 4
# 猫头鹰的初始位置
BIRD_INIT_POSI = [SCREEN_WIDTH * 0.3, \
        (SCREEN_HEIGHT - BIRD_HEIGHT) / 3]


class Floor():
    """ 地板类 """
    def __init__(self, posi, w, h):
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect(topleft = posi)
        self.image.fill(pygame.Color("green"))
        self.image.set_alpha(255)      # 图像透明度
        # 颜色值透明度
        self.image.set_colorkey(pygame.Color("blue"))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Eagle():
    """ 跳跃的小方块类 """
    def __init__(self, position):
        self.image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
        self.rect = self.image.get_rect(center = position)
        self.up_speed = 1.5        # 跳跃初速度
        self.down_speed = 1.5      # 下坠初速度
        self.variable_time = 0     # 匀加速运动持续时间
        self.acc_up = 0.5          # 跳跃加速度
        self.acc_down = 0.4        # 下坠加速度
        self.is_jumping = False    # 猫头鹰跳跃状态开关
        self.high_offset = 0       # 猫头鹰上下偏移量
        self.is_horizontal = False # 猫头鹰水平移动开关
        self.direction = 0         # 猫头鹰移动方向

    def draw(self, screen):
        """ 绘制猫头鹰 """
        screen.blit(self.image, self.rect)
        self.image.fill(pygame.Color("white"))


class Baffle():
    """ 挡板类 """
    def __init__(self, w, h, **kwargs):
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect(**kwargs)

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color("blue"), self.rect, 1)



def draw_game_over(screen, text):
    """
    绘制 Press Enter To Start!
    """
    font_size = 50
    font = pygame.font.SysFont('arial', font_size)
    font_sur = font.render(text, True, (0, 255, 0))
    font_rec = font_sur.get_rect(center = screen.get_rect().center)
    screen.blit(font_sur, font_rec)

pygame.init()
# 游戏窗口电脑屏幕居中
# 注意：此系统变量的设置不可在 Pygame 窗口创建之后， 否则无效
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Eagle')
pygame.key.set_repeat(FPS)   # 打开重复按键
clock = pygame.time.Clock()  # 时钟管理对象
is_game_running = True       # 运行开关
fps_interval = 6             # 挡板帧率间隔


while True:

    screen.fill(BG_COLOR)  # 填充背景

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()           # 更新画布
    clock.tick(FPS)
