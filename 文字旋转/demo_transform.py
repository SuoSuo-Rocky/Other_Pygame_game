
import sys

# 导入pygame 及常量库
import copy

import pygame
from pygame.locals import *
from pygame import freetype

SIZE = WIDTH, HEIGHT = 640, 396
FPS = 60


class MySprite(pygame.sprite.Sprite):
    """ 自定义精灵类 """

    def __init__(self, img_file, *args, **kwargs):
        """ 精灵初始化 """
        super(MySprite, self).__init__()
        combi = None
        if isinstance(img_file, str):  # 图片文件名
            self.image = pygame.image.load(img_file).convert_alpha()
        elif isinstance(img_file, (list, tuple)):                          # Surface 对象的 大小
            self.image = pygame.Surface(img_file, pygame.SRCALPHA, 32) # 透明图像
            # self.image = pygame.Surface(img_file)
        else:  # Font 对象
            assert isinstance(img_file, freetype.Font)
            assert isinstance(args[0], str) # 必须要有文本
            # 表示前景色
            if len(args) == 2 and isinstance(args[1], (list, tuple, pygame.Color)):
                # 表示背景色
                if len(args) ==  3 and isinstance(args[2], (list, tuple, pygame.Color)):
                    combi = img_file.render(*args, **kwargs)
                else:
                    combi = img_file.render(args[0], args[1], **kwargs)
            else:
                combi = img_file.render(args[0], **kwargs)
        if combi:
            self.image, self.rect = combi
        else:
            self.rect = self.image.get_rect()
        self.orig_image = self.image

    def draw(self, screen):
        """ 绘制精灵 """
        screen.blit(self.image, self.rect)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.orig_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello__施伟")
clock = pygame.time.Clock()
# 创建字体对象
font = freetype.Font("songti.otf", 40, )

mrsoft = MySprite(font, "明日科技外星人", pygame.Color('green'))
mrsoft.rect.center = screen.get_rect().center

angle = 0

running = True
# 主体循环
while running:
    # 1. 清屏
    screen.fill((25, 102, 173))


    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    angle += 2
    mrsoft.rotate(angle)

    if angle == 360:
        angle  = 0
    mrsoft.draw(screen)
    # 3.刷新
    pygame.display.update()
    clock.tick(FPS)
