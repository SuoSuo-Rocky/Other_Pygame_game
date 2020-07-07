


import pygame
pygame.init()
# sprite_01 = pygame.sprite.Sprite()
# group_01 = pygame.sprite.Group(sprite_01)
# sprite_02 = pygame.sprite.Sprite(group_01)
group_02 = pygame.sprite.Group()
# group_02.add([sprite_01, sprite_02])
# print(group_02.sprites())

small_sur = pygame.Surface((100, 100))
img_sur = pygame.image.load("super_06_deal.png")
res = img_sur.blit(small_sur, (200, 200), (50, 50, 50, 50))
print(f"res = {res}")

