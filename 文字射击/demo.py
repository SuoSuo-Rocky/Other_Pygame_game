import random
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
        elif isinstance(img_file, (list, tuple)):                          # Surface 对象的 大小
            self.image = pygame.Surface(img_file, pygame.SRCALPHA, 32) # 透明图像
            # self.image = pygame.Surface(img_file)
        else:  # Font 对象
            assert isinstance(img_file, freetype.Font)
            assert isinstance(args[0], str) # 必须要有文本
            # 表示前景色
            if len(args) >= 2 and isinstance(args[1], (list, tuple, pygame.Color)):
                # 表示背景色
                if len(args) >=  3 and isinstance(args[2], (list, tuple, pygame.Color)):
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
        self.is_move = True


    def init_unit(self, *args, **kwargs):

        if kwargs.get('source', None):
            self.source = pygame.Vector2(*kwargs['source'])
            self.rect.center = (self.source.x, self.source.y)

        # 计算所需移动的单位向量
        if kwargs.get("dest", None):   # 目的地 的 中心位置
            self.collide_rec = pygame.Rect(10, 10, 10, 10)
            self.dest = kwargs['dest']
            # 计算总 向量
            distance_vec = pygame.Vector2(*self.dest) - pygame.Vector2(*source_loc)
            self.collide_rec.size = abs(distance_vec.x), abs(distance_vec.y)  # 赋值 尺寸
            # 四种情况，确定 所圈定的具体位置
            if distance_vec.x > 0 and distance_vec.y > 0:  # 右下角
                self.collide_rec.topleft = source_loc
                print("右下角")
                print(f"collide_rec = {self.collide_rec}")
            elif distance_vec.x < 0 and distance_vec.y > 0:  # 左下角
                self.collide_rec.topright = source_loc
                print("左下角")
                print(f"collide_rec = {self.collide_rec}")
            elif distance_vec.x > 0 and distance_vec.y < 0:  # 右上角
                self.collide_rec.bottomleft = source_loc
                print("右上角")
                print(f"collide_rec = {self.collide_rec}")
            elif distance_vec.x < 0 and distance_vec.y < 0:  # 左上角
                print(f"collide_rec = {self.collide_rec} ----01")
                print(f'source_loc = {source_loc}')
                self.collide_rec.bottomright = source_loc
                print("左上角")
                print(f"collide_rec = {self.collide_rec} --- 02")
            self.unit = distance_vec.normalize()  # 计算单位向量
            self.offset = list((i for i in self.unit)) # 计算偏移量
            # print(f"offset = {self.offset}")

    def draw(self, screen):
        """ 绘制精灵 """
        screen.blit(self.image, self.rect)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.orig_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        """ 移动精灵 """
        while self.is_move:
            print(f'++++++++++++++++++   new  while ')
            print(f"offset = { self.offset}")
            self.source += self.unit
            self.rect.center = int(self.source.x), int(self.source.y)
            print(f'source = {self.source}')
            print(f"collide_rec = {self.collide_rec}---source_loc = {source_loc} --  matrix_fir_loc = {matrix_fir_loc}")
            # pygame.draw.rect(screen, pygame.Color('red'), self.collide_rec, 1)
            pygame.draw.circle(screen, pygame.Color('green'), self.dest, 2, )
            pygame.draw.circle(screen, pygame.Color('blue'), (int(self.source.x), int(self.source.y)), 2, )
            # 移动超出范围
            if self.collide_rec.collidepoint(*self.rect.center):

                print('______________________________________')
                self.is_move = False
                break
            pygame.time.wait(20)
            pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello__施伟")
clock = pygame.time.Clock()
# 创建字体对象
font = freetype.Font("songti.otf", 30, )
scr_rec = screen.get_rect()
txt = r'长春市宽城区\明日科技有限责任公司\跟着我学数学'
source_loc = (scr_rec.centerx, scr_rec.bottom - 66)

matrix_fir_loc = (scr_rec.centerx - 100, scr_rec.top + 66)
txt_sprite_group = pygame.sprite.Group()
row, col = 0, 0
init_loc = list(matrix_fir_loc)
for k, ele in enumerate(list(txt)):
    ran = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    obj =  MySprite(font, ele, pygame.Color('green'), ran)
    obj.init_unit(source = source_loc, dest = init_loc)
    # print(f'ele = {ele}, width = {obj.rect.w}, height = {obj.rect.h}')
    # print(f"obj.dest = {obj.dest}")

    if ele == "\\":
        init_loc[1] += (obj.rect.h + 12)
        init_loc[0] = matrix_fir_loc[0]
        continue
    else:
        init_loc[0] += (obj.rect.w + 3)
    txt_sprite_group.add(obj)
# obj = MySprite(font, txt, pygame.Color('green'))
# txt_sprite_group.add(obj)

running = True
# 主体循环
while running:
    # 1. 清屏
    screen.fill((25, 102, 173))
    # 2. 绘制
    # txt_sprite_group.draw(screen)
    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.event.clear()
    for obj in txt_sprite_group.sprites():
        obj.draw(screen)
        obj.remove()
        print(f'__________________new ')
    # 3.刷新
    pygame.display.flip()
    clock.tick(FPS)
