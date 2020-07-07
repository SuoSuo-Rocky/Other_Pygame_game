import copy
import pickle
import sys

# 导入pygame 及常量库
import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640, 396
FPS = 60
exit_switch = False

pygame.init()
screen = pygame.display.set_mode(SIZE, RESIZABLE)
pygame.display.set_caption("Hello__施伟")
clock = pygame.time.Clock()
# 创建字体对象
font = pygame.font.Font("songti.otf", 40)


def font_switch_img(map):

    pygame.image.save(map.image, "misoft.png")
    pygame.quit()
    exit()


class MySprite(pygame.sprite.Sprite):
    """ 自定义精灵类 """

    def __init__(self, img_file):
        """ 精灵初始化 """
        super(MySprite, self).__init__()
        if isinstance(img_file, str):
            self.image = pygame.image.load(img_file).convert_alpha()
        else:
            assert isinstance(img_file, (list, tuple))
            self.image = pygame.Surface(img_file, pygame.SRCALPHA, 32)
            # self.image = pygame.Surface(img_file)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        """ 绘制精灵 """
        screen.blit(self.image, self.rect)

map = MySprite(screen.get_rect().size)
font_sur = font.render("明日科技外星人", True, pygame.Color('green'))
font_rec = font_sur.get_rect()
font_rec.center = map.rect.center

running = True
# 主体循环
while running:
    # 1. 清屏
    screen.fill((25, 102, 173))
    # map.image.fill(pygame.Color("white"))

    # 2. 绘制
    map.image.blit(font_sur, font_rec)

    map.draw(screen)
    # 3.刷新
    pygame.display.flip()

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type in [KEYDOWN, MOUSEBUTTONDOWN]:
            exit_switch = True

    if exit_switch:
        font_switch_img(map)

    clock.tick(FPS)
