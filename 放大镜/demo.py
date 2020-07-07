



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
        self.rect = self.image.get_rect()

    def draw(self, screen):
        """ 绘制精灵 """
        screen.blit(self.image, self.rect)

# 创建游戏窗口
screen = pygame.display.set_mode(SIZE)
# 设置窗口标题
pygame.display.set_caption(TITLE)
# 创建时间管理对象
clock = pygame.time.Clock()
# 创建字体对象
font = pygame.font.SysFont(None, 60, )
clip_size = (40, 40)

obj = MySprite("one.jpg")
obj.rect.center = screen.get_rect().center

sub_obj = MySprite(clip_size)

running = True
# 程序运行主体循环
while running:
    # 1. 清屏(窗口纯背景色画纸的绘制)
    screen.fill(BG_COLOR)  # 先准备一块画布
    pos = pygame.mouse.get_pos()
    top_left = (int(pos[0] - sub_obj.rect.w // 2),
                int(pos[1] - sub_obj.rect.h // 2))
    sub_obj.rect.topleft = top_left
    try:
        sub_obj.image = pygame.Surface.subsurface(obj.image, sub_obj.rect)
    except Exception as e:
        pass

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:  # 判断点击窗口右上角“X”
            pygame.quit()       # 退出游戏，还原设备
            sys.exit()          # 程序退出
    # 2. 绘制
    sub_obj.draw(screen)

    # 3.刷新
    pygame.display.update()
    # 设置帧数
    clock.tick(FPS)

