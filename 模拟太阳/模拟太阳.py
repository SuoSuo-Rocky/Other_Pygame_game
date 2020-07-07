

#  https://zhuanlan.zhihu.com/p/116941490

# 导出模块
import pygame
import math
from pygame.locals import *


# 游戏初始化
pygame.init()

# 定义窗口大小、标题名称、字体设置、创建时钟
size = width, height = 1200, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption("太阳-地球-月亮-金星等示意图")
myfont=pygame.font.Font(None,60)
# 如果是中文，字体hwfs=华文仿宋字体，放在根目录下
# myfont=pygame.font.Font('hwfs.ttf',60)
# 创建时钟对象 (可以控制游戏循环频率)
clock = pygame.time.Clock()

FPS = 60

# 初始化相关定义---具体到各个游戏的定义
# 定义三个空列表
'''  
pos_v=[]  
pos_e = []  
pos_mm = []  
'''

#与上面的作用相同
pos_v = pos_e = pos_mm = []
#金星、地球和月球等其他行星的公转过的角度
roll_v = roll_e = roll_m = 0
roll_3 = roll_4 = roll_5 = roll_6 = roll_7 = roll_8 = 0
textImage = myfont.render("Sun=yellow,Earth=blue,Moon=green,Venas=red", True, pygame.Color("green"))
# 太阳的位置, 中心坐标， 固定
position = width//2, height//2
# 8.第6步：

# ---第6步---游戏循环---
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.fill(pygame.Color("black"))
    # 绘制说明文字
    screen.blit(textImage,(100,100))
    # 画太阳
    pygame.draw.circle(screen, pygame.Color("yellow"), position, 60, 0)

    # 画地球
    pos_e_x = int(width//2 + height//6 * math.sin(roll_e))
    pos_e_y = int(height//2 + height//6 * math.cos(roll_e))
    pygame.draw.circle(screen, pygame.Color("blue"), (pos_e_x, pos_e_y), 15, 0)
    roll_e += 0.01       # 地球公转角度， 每帧

    # 画地球的轨迹线
    pos_e.append((pos_e_x, pos_e_y))
    if len(pos_e) > 255:
        pos_e.pop(0) # 弹出栈底的元素
    for i in range(len(pos_e)):
        # 画像素点（半径为 1 的圆）
        pygame.draw.circle(screen, pygame.Color("green"), pos_e[i], 1, 0)

    # 画月球
    pos_m_x = int(pos_e_x + height//20 * math.sin(roll_m))
    pos_m_y = int(pos_e_y + height//20 * math.cos(roll_m))
    pygame.draw.circle(screen, pygame.Color("green"), (pos_m_x, pos_m_y), 5, 0)
    roll_m += 0.1  # 月球的公转角度， 每帧

    # 画月球的轨迹线
    pos_mm.append((pos_m_x, pos_m_y))
    if len(pos_mm) > 255:
        pos_mm.pop(0)  # 弹出栈底的元素
    for i in range(len(pos_mm)):
        pygame.draw.circle(screen, pygame.Color("green") ,pos_mm[i], 1, 0)

    # 画金星(Venus), 也是绕着太阳转， 但比地球的半径大
    pos_v_x = int(width//2 + height//3 * math.sin(roll_v))
    pos_v_y = int(height//2 + height//3 * math.cos(roll_v))
    pygame.draw.circle(screen, pygame.Color("red"), (pos_v_x, pos_v_y), 20, 0)
    roll_v += 0.015 # 金星的公转角度， 每帧

    # 画金星的轨迹线
    pos_v.append((pos_v_x, pos_v_y))
    if len(pos_v) > 255:
        pos_v.pop(0)
    for i in range(len(pos_v)):
        pygame.draw.circle(screen, pygame.Color("green"), pos_v[i], 1, 0)

    #---6-6---其他几个行星---缺点不是椭圆形轨道---
    # 3
    roll_3 += 0.03# 假设金星每帧公转0.03pi
    pos_3_x = int(width//2 + height//3.5*math.sin(roll_3))
    pos_3_y = int(height//2 + height//3.5*math.cos(roll_3))
    pygame.draw.circle(screen, pygame.Color("white"),(pos_3_x, pos_3_y), 20, 0)

    # 4
    roll_4 += 0.04# 假设金星每帧公转0.04pi
    pos_4_x = int(width//2 + height//4*math.sin(roll_4))
    pos_4_y = int(height//2 + height//4*math.cos(roll_4))
    pygame.draw.circle(screen, pygame.Color("white"),(pos_4_x, pos_4_y), 20, 0)

    # 5
    roll_5 += 0.05# 假设金星每帧公转0.05pi
    pos_5_x = int(width//2 + height//5*math.sin(roll_5))
    pos_5_y = int(height//2 + height//5*math.cos(roll_5))
    pygame.draw.circle(screen, pygame.Color("white"), (pos_5_x, pos_5_y), 20, 0)
    # 6
    roll_6 += 0.06# 假设金星每帧公转0.06pi
    pos_6_x = int(width//2 + height//2.5*math.sin(roll_6))
    pos_6_y = int(height//2 + height//2.5*math.cos(roll_6))
    pygame.draw.circle(screen, pygame.Color("white"),(pos_6_x, pos_6_y), 20, 0)

    # 7
    roll_7 += 0.07# 假设金星每帧公转0.07pi
    pos_7_x = int(width//2 + height//4.5*math.sin(roll_7))
    pos_7_y = int(height//2 + height//4.5*math.cos(roll_7))
    pygame.draw.circle(screen, pygame.Color("white"), (pos_7_x, pos_7_y), 20, 0)

    # 8
    roll_8 += 0.08# 假设金星每帧公转0.08pi
    pos_8_x = int(width//2 + height//5.5*math.sin(roll_8))
    pos_8_y = int(height//2 + height//5.5*math.cos(roll_8))
    pygame.draw.circle(screen, pygame.Color("white"), (pos_8_x, pos_8_y), 20, 0)

    #刷新
    pygame.display.flip()
    #数值越大刷新越快，小球运动越快
    clock.tick(FPS)