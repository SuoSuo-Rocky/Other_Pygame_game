

# 转换回去

import pygame

pygame.init()

size = width, height = 640, 396

screen = pygame.display.set_mode(size)
img = pygame.image.load("img/6t.png").convert_alpha()

# img_rect = img.get_rect()
# img_rect.center = width // 2, height // 2
# screen.blit(img, img_rect)

with pygame.PixelArray(img) as pixel:
    pixel.replace((255, 255, 255, 255), (255, 255, 255, 0))
    # pixel = pixel.transpose()
    # for row, li in enumerate(pixel):
    #     for col, ele in enumerate(li):
    #         if ele == (255, 255, 255, 255):
    #             pixel[row][col] = (255, 255, 255, 0)

    pygame.image.save(pixel.make_surface(), "img/66.png")

pygame.quit()
exit()



