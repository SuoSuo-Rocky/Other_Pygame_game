



import sys
import pygame
from pygame.locals import *


class MyPlane(pygame.sprite.Sprite):
    """我的战机类"""

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("static/img/hero1.png").convert_alpha()
        self.image2 = pygame.image.load("static/img/hero2.png").convert_alpha()
        self.destroy_images = []
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.speed = 10
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width


class Element(pygame.sprite.Sprite):
    """背景图片类"""

    # 背景图片地址
    bg_image = "static/img/background.png"

    def __init__(self, image, posi):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = posi

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def remove(self, speed):
        self.rect = self.rect.move(*speed)

def bg_replace(screen, pos_y):
    """ 绘制背景图片"""
    bg = Element(Element.bg_image, (0, pos_y - 850))
    bg02 = Element(Element.bg_image, (0, pos_y - 850 * 2))
    bg.draw(screen)
    bg02.draw(screen)


def main():

    screen_size = (478, 850)
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("喷气战机")
    screen = pygame.display.set_mode(screen_size)
    pygame.key.set_repeat(10)       # 开启重复产生键盘事件 功能

    bg_pos_y = 850  # 背景图片的 高
    # 我的 飞机
    airplane = MyPlane(screen_size)
    # 我飞机的 切换开关
    switch_image = False
    # 用于延迟
    delay = 100

    while 1:
        # 绘制背景图片
        bg_replace(screen, bg_pos_y)
        # 滚动背景图片
        bg_pos_y += 20
        if bg_pos_y >=  850 * 2:
            bg_pos_y = 850
        # 绘制我的战机
        if switch_image:
            screen.blit(airplane.image1, airplane.rect)
        else:
               screen.blit(airplane.image2, airplane.rect)
        # 事件检索
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 键盘轮询
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE] or keys[K_q]:
            sys.exit()
        # 飞机事件监听
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            airplane.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            airplane.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            airplane.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            airplane.moveRight()

        # 切换图片开关
        if not (delay % 5):
            switch_image = not switch_image
        delay -= 1
        if not delay:
            delay = 100
        # 刷新绘制
        pygame.display.update()
        # 设置帧率
        clock.tick(60)


if __name__ == '__main__':
   main()
