

import sys

# 导入pygame 及常量库
import pygame
from pygame import freetype
from pygame.locals import *

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
        elif isinstance(img_file, (list, tuple)):     # Surface 对象的 大小
            self.image = pygame.Surface(img_file, pygame.SRCALPHA, 32) # 透明图像
            if len(args) ==  1 and isinstance(args[0], (list, tuple, pygame.Color)): # 前景色
                self.image.fill(args[0])
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

    def draw(self, screen):
        """ 绘制精灵 """
        screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello__施伟")
clock = pygame.time.Clock()
# 创建字体对象
font = freetype.Font("songti.otf", 40)
# 该下拉菜单 所有元素的 参考坐标 , 头部点击框的左上顶点坐标
master_pos = (WIDTH // 2 - 90, 60)
master_size = (180, 60)
left_click_switch = False
right_click_switch = False
# 子菜单上部分面板 中子菜单的数量
sub_menu_num = 3
# 子菜单上部分面板 尺寸
sub_panel_size =  (2 * master_size[0] - 30, sub_menu_num * (master_size[1] - 10) + 20)
# 子菜单上部分面板 中子菜单精灵组
sub_menu_group = pygame.sprite.Group()
txt_li = ["panda", 'lion is Big', 'Monkey is cute']


# 头部点击框
master_menu = MySprite(master_size, pygame.Color(51, 122, 183))
master_menu.rect.topleft = master_pos
# 下三角图标
sanjiao = MySprite("sanjiao.png")
sanjiao.rect.topleft = (master_pos[0] + master_size[0] - 44, \
                        (master_pos[1] + master_size[1] // 2)- sanjiao.rect.h // 2 )
# 头部框的文本
master_txt = MySprite(font, "Primary", pygame.Color('white'), size = 33)
master_txt.rect.center = ((master_menu.rect.w - sanjiao.rect.w) // 2 + master_pos[0], \
                          master_menu.rect.centery)

# 子菜单上部分面板
sub_top_panel = MySprite(sub_panel_size, pygame.Color('green'))
sub_top_panel.rect.topleft  = (master_menu.rect.bottomleft[0], \
                               master_menu.rect.bottomleft[1] + 4)
# 子菜单面板中的子菜单
# sub_01 = MySprite((sub_top_panel.image.get_width(), master_menu.rect.h - 10), pygame.Color(220, 220, 220))
# 动态创建子菜单变量
local_varible = locals()
for index in range(1, sub_menu_num + 1):
    local_varible["sub_0" + str(index)] = MySprite((sub_top_panel.image.get_width(), master_menu.rect.h - 10))
    local_varible["sub_0" + str(index)].rect.topleft = sub_top_panel.rect.left, \
                                                       sub_top_panel.rect.top + 10 + (index - 1) * (master_size[1] - 10)
    # local_varible["sub_0" + str(index)].rect
    sub_menu_group.add(local_varible["sub_0" + str(index)])
print(f"local = {list(locals())}")
# 动态创建 子菜单文本 精灵对象
for i in range(1, sub_menu_num + 1):
    local_varible["sub_txt_0" + str(i)] = MySprite(font, txt_li[i - 1])
    local_varible["sub_txt_0" + str(i)].rect.midleft =  local_varible["sub_0" + str(i)].rect.left + 16, \
                                                        local_varible["sub_0" + str(i)].rect.centery
    sub_menu_group.add(local_varible["sub_txt_0" + str(i)])


running = True
# 主体循环
while running:
    # 1. 清屏
    screen.fill((255, 255, 255))
    pos = pygame.mouse.get_pos()
    # 2. 绘制
    master_menu.draw(screen)
    sanjiao.draw(screen)
    master_txt.draw(screen)


    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                # 鼠标左键单击头部框的左半部分
                if master_menu.rect.collidepoint(event.pos):
                    left_click_switch = bool(1 - left_click_switch)
                elif not sub_top_panel.rect.collidepoint(event.pos):
                    left_click_switch = False
    # 子菜单面板中 子菜单 与 鼠标坐标的 边界检测
        if event.type == MOUSEMOTION:
            for i in range(1, sub_menu_num + 1):
                obj = local_varible["sub_0" + str(i)]
                if obj.rect.collidepoint(event.pos):
                    obj.image.fill(pygame.Color('white'))
                else:
                    obj.image.fill(pygame.Color(220, 220, 220 ))



    # 切换 头部框点击时的背景色
    if left_click_switch:
        master_menu.image.fill(pygame.Color(40, 96, 144))
        # 绘制一个黑色的边框
        pygame.draw.rect(screen, pygame.Color('black'), master_menu.rect, 3)
        # 绘制子菜单面板
        sub_top_panel.draw(screen)
        # 绘制子菜单面板边框
        pygame.draw.rect(screen, pygame.Color(220, 220, 220), sub_top_panel.rect, 2)
        # 绘制子菜单面板中的子菜单
        sub_menu_group.draw(screen)
    else:
        master_menu.image.fill(pygame.Color(51, 122, 183))

    # 3.刷新
    pygame.display.update()
    clock.tick(FPS)
