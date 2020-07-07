
import pygame

class MySprite(pygame.sprite.Sprite):
    """ 自定义精灵类 """

    def __init__(self, img_file):
        """ 精灵初始化 """
        super(MySprite, self).__init__()
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        
    def draw(self, screen):
        """ 绘制精灵 """
        screen.blit(self.image, self.rect)
