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


    # 更新猫头鹰的位置
    def update(self):
        """ 更新位置 """
        """匀变速运动位移公式： S = V0 * t + a * t ** 2 / 2 
            V0: 初速度
            t: 运动时间
            a： 加速度
            S: 位移
        """
        if self.is_jumping:  # 向上跳
            # 计算位移:
            self.high_offset = int(self.up_speed * self.variable_time + \
                                self.acc_up * self.variable_time ** 2 / 2)
            # 移动位置
            self.rect.move_ip(0, self.high_offset * -1)
            # 跳跃时防止跳出窗体外了
            if not screen.get_rect().contains(self.rect) and \
                    self.rect.top < 0:
                self.rect.top = 0
                self.is_jumping = False
                self.variable_time  = 0
            self.high_offset = 0
            self.variable_time -= 1
            if self.variable_time <= 0: # 一次跳跃的时间到顶端了
                self.is_jumping = False
        else:  # 向下落
            self.high_offset = int(self.down_speed * self.variable_time + \
                                self.acc_down * self.variable_time ** 2 / 2)
            # 移动位置
            self.rect.move_ip(0, self.high_offset)
            # 与地板有重叠
            if self.rect.colliderect(floor.rect):
                self.rect.bottom = floor.rect.top + 1
            # 防止下落到窗体外
            if not screen.get_rect().contains(self.rect) and \
                    self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = floor.rect.top
            self.high_offset = 0
            # 匀加速运动时间超时
            if self.variable_time <= VARIABLE_LEN_TIME - 3:
                self.variable_time += 1
        # 左右移动
        if self.is_horizontal:
            if self.direction == pygame.K_LEFT:
                self.rect.move_ip(-8, 0)
            if self.direction == pygame.K_RIGHT:
                self.rect.move_ip(8, 0)
            if not screen.get_rect().contains(self.rect):
                if self.rect.left < 0:
                    self.rect.left = 0
                    return
                if self.rect.right > SCREEN_WIDTH:
                    self.rect.right = SCREEN_WIDTH - 1
                    return
            self.is_horizontal = False


class Baffle():
    """ 挡板类 """
    def __init__(self, w, h, **kwargs):
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect(**kwargs)

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color("blue"), self.rect, 1)


    @staticmethod
    def create_baffle_group():
        """ 创建挡板组 """
        # baffle_group = pygame.sprite.Group()
        baffle_group = []
        x = SCREEN_WIDTH + 100
        for i in range(BAFFLE_GROUP_NUM):
            bottomleft = (x, random.randint(100, 400))
            vertical_interval = random.randrange(100, \
                                    MAX_BAFFLE_INTERVAL + 1)
            topleft = (x, bottomleft[1] + vertical_interval)
            up_obj = Baffle(BAFFLE_WIDTH, BAFFLE_HEIGHT, \
                            bottomleft = bottomleft)
            down_obj = Baffle(BAFFLE_WIDTH, BAFFLE_HEIGHT, \
                              topleft = topleft)
            baffle_group.append(up_obj)
            baffle_group.append(down_obj)
            x += (BAFFLE_WIDTH + VERTICAL_BAFFLE_INTERVAL)
        return baffle_group


    def update(self, *args):
        if is_game_running:
            for k, obj in enumerate(baffle_group):
                obj.move(k)


    def move(self, index):
        """ 挡板移动 """
        self.rect.move_ip(BAFFLE_SPEED * -1, 0)
        if index in [0, 2, 4, 6]:
            front = index % (BAFFLE_GROUP_NUM * 2) - 2
            if front == -2:
                front = 6
            # 挡板与 窗口 无重叠部分
            if not self.rect.colliderect(screen.get_rect()) and \
                    self.rect.left < 0:
                print("过界 ", index)
                self.rect.left = baffle_group[front].rect.right + \
                                 VERTICAL_BAFFLE_INTERVAL
                baffle_group[index + 1].rect.left =  \
                    baffle_group[front].rect.right + \
                    VERTICAL_BAFFLE_INTERVAL


def init_sprite():
    """
    初始化游戏元素类
    """
    eagle = Eagle(BIRD_INIT_POSI)
    floor = Floor((-1, SCREEN_HEIGHT - FLOOR_HEIGHT), \
                  SCREEN_WIDTH + 2, FLOOR_HEIGHT)
    # 创建挡板组
    baffle_group = Baffle(BAFFLE_WIDTH, BAFFLE_HEIGHT).create_baffle_group()
    return eagle, floor, baffle_group


def draw_game_over(screen, text):
    """
    绘制 Press Enter To Start!
    """
    font_size = 50
    font = pygame.font.SysFont('arial', font_size)
    font_sur = font.render(text, True, (0, 255, 0))
    font_rec = font_sur.get_rect(center = screen.get_rect().center)
    screen.blit(font_sur, font_rec)


def listen_event(is_game_running, eagle):
    """
    游戏事件监听
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击关闭按钮退出
            pygame.quit()
            sys.exit()
            input()
        elif event.type == pygame.KEYDOWN:
            # 空格键 或者 up 键猫头鹰上升
            if event.key == pygame.K_SPACE or \
                    event.key == pygame.K_UP:
                if is_game_running:
                    eagle.is_jumping = True
                    eagle.variable_time = VARIABLE_LEN_TIME
            # 猫头鹰左右移动
            if event.key == pygame.K_LEFT:
                eagle.is_horizontal = True
                eagle.direction = pygame.K_LEFT
            if event.key == pygame.K_RIGHT:
                eagle.is_horizontal = True
                eagle.direction = pygame.K_RIGHT
            # 游戏结束时回车键继续
            elif event.key == pygame.K_RETURN and not is_game_running:
                return True


def collision_test():
    """
    重叠检测
    """
    # 猫头鹰和挡板
    for obj in baffle_group:
        if eagle.rect.colliderect(obj.rect):
            return True
    # 猫头鹰和地板
    if eagle.rect.colliderect(floor.rect):
        return True
    return False

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
eagle, floor, baffle_group = init_sprite() # 初始化游戏元素类


# 游戏主逻辑循环
while True:

    screen.fill(BG_COLOR)  # 填充背景

    # 事件监听
    restart = listen_event(is_game_running, eagle)


    is_collision = collision_test()  # 重叠检测
    if is_collision:                 # 游戏结束
        is_game_running = False

    # 绘制
    eagle.draw(screen)                # 画鸟
    for obj in baffle_group:          # 画挡板
        obj.draw(screen)
    floor.draw(screen)                # 画地板


    # 位置更新
    if is_game_running:
        eagle.update()                # 猫头鹰位移更新
        fps_interval -= 1
        if fps_interval == 0:         # 移动挡板
            for obj in baffle_group:
                obj.update()
            fps_interval = 3
    else:                             # 游戏结束
        draw_game_over(screen, 'Press Enter To Start!')


    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()           # 更新画布
    clock.tick(FPS)
