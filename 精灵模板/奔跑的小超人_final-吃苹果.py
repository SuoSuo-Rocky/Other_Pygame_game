



import random

import pygame
from pygame.locals import *
from pygame.math import Vector2

SIZE = WIDTH, HEIGHT = 640, 396
FPS = 30

class MySprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.master_image = None # 精灵序列图(主图)
        self.image = None        # 帧图 Surface 对象
        self.rect = None         # 帧图 Rect 对象
        self.topleft = 0, 0      # 帧图左上顶点坐标
        self.area = 0            # 精灵序列号
        self.area_width = 1      # 帧图宽
        self.area_height = 1     # 帧图高
        self.first_area = 0      # 动画帧图起始序列号
        self.last_area = 0       # 动画帧图终止序列号
        self.columns = 1         # 精灵序列图列数（每个动画的帧数）
        self.old_area = -1       # 绘制的前一帧图序列号
        self.last_time = 0       # 前一帧图绘制的时间
        self.is_move = False     # 移动开关
        self.vel = Vector2(0, 0) # 移动速度

    def _get_dir(self):
        return (self.first_area, self.last_area)
    def _set_dir(self, direction):
        self.first_area = direction * self.columns
        self.last_area = self.first_area + self.columns - 1
    # 通过移动方向 控制帧图区间
    direction = property(_get_dir, _set_dir)

    def load_img(self, filename, width, height, columns):
        """加载序列（精灵）图"""
        self.master_image = pygame.image.load(filename).convert_alpha()
        # 帧图宽度
        self.area_width = width
        # 帧图高度
        self.area_height = height
        self.rect = pygame.Rect(0, 0, width, height)
        # 序列图中的帧图列数
        self.columns = columns
        rect = self.master_image.get_rect()
        # 序列图中的终止帧图序号(从0开始)
        self.last_area = (rect.width // width) - 1

        self.mask = pygame.mask.from_surface(self.master_image)

    def update(self, current_time, rate=20):
        """更新帧图"""
        # 移动控制
        if not self.is_move:
            self.area = self.first_area = self.last_area
            self.vel = (0, 0)
        # 控制动画的绘制速率
        if current_time > self.last_time + rate:
            self.area += 1
            # 帧区间边界判断
            if self.area > self.last_area:
                self.area = self.first_area
            if self.area < self.first_area:
                self.area = self.first_area
            # 记录当前时间
            self.last_time = current_time
        # 只有当帧号发生更改时才更新 self.image
        if self.area != self.old_area:
            area_x = (self.area % self.columns) * self.area_width
            area_y = (self.area // self.columns) * self.area_height
            rect = pygame.Rect(area_x, area_y, self.area_width, self.area_height)
            # 子表面 Surface
            try:
                self.image = self.master_image.subsurface(rect)

                self.mask = pygame.mask.from_surface(self.image)
            except Exception as e:
                print(e + " \n图片剪裁超出范围........")
            self.old_area = self.area

    def draw(self, screen):
        """绘制帧图"""
        screen.blit(self.image, self.rect)

    def move(self):
        """ 移动 """
        self.rect.move_ip(self.vel)

def create_apple():
    """ 创建众多苹果精灵 """
    global apple_group
    apple_li = []
    for i in range(36):
        obj = MySprite()
        obj.load_img("apple.png", 35, 35, 1)
        while 1:
            x = random.randrange(WIDTH - obj.rect.w)
            y = random.randrange(HEIGHT - obj.rect.h)
            rect = pygame.Rect((x, y), obj.rect.size)
            # 判断重叠，单个 与 列表中的所有
            if not rect.collidelistall(apple_li):
                apple_li.append(rect)
                obj.rect = rect
                apple_group.add(obj)
                break

def draw_text(font, text, color=(255,255,255)):
    """ 绘制文本类 """
    sur = font.render(text, True, color)
    rec = sur.get_rect()
    screen = pygame.display.get_surface()
    rec.center = screen.get_rect().center
    screen.blit(sur, rec)

pygame.init()
screen = pygame.display.set_mode((640, 396), 0, 32)
pygame.display.set_caption("小超人吃苹果_SuoSuo")
pygame.key.set_repeat(26)         # 重复响应按键
clock = pygame.time.Clock()
super_man = MySprite()
super_man.load_img("super_man.png", 150, 150, 4)
font = pygame.font.Font(None, 60)

apple_group = pygame.sprite.Group()  # 苹果精灵组
create_apple()                       # 创建苹果
apple_group.update(100, 0) # 初始化所有苹果精灵的self.image

while True:
    screen.fill((0, 163, 150))
    ticks = pygame.time.get_ticks()
    if pygame.event.wait().type in [QUIT]: exit()
    keys = pygame.key.get_pressed()   # 键盘轮询
    if keys[pygame.K_ESCAPE]: exit()
    dir = [keys[K_DOWN], keys[K_LEFT], keys[K_RIGHT], \
           keys[K_UP], (0, 4), (-4, 0), (4, 0), (0, -4)]
    for k, v in enumerate(dir[0:4]):  # 判断移动方向
        if v:
            super_man.direction = k
            super_man.vel = dir[k + 4]
            super_man.is_move = v
            break
    else:                             # 无移动
        super_man.is_move = False

    # 碰撞检测 返回第一个(使用遮罩检测)
    collide = pygame.sprite.spritecollideany(super_man, \
            apple_group, pygame.sprite.collide_mask)
    if collide != None:
        # 按比例缩小要圆形检测
        if pygame.sprite.collide_circle_ratio(0.66)(super_man, collide):
            apple_group.remove(collide) # 删除吃掉的苹果精灵
    if not apple_group.sprites():
        while 1:
            draw_text(font, "G A M E   O V E R")
            if pygame.event.wait().type in [QUIT, KEYDOWN]: exit()
            pygame.display.update()
    apple_group.draw(screen)       # 绘制苹果
    super_man.update(ticks, 90)    # 更新
    super_man.draw(screen)         # 绘制小超人
    super_man.move()               # 移动
    pygame.display.update()
    clock.tick(FPS)

