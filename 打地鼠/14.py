import pygame
import sys
import random
from pygame.locals import *  # 引入鼠标事件类型
import time

"""
https://www.jianshu.com/p/cb2829724e1b
"""

pygame.init()  # 初始化
window = pygame.display.set_mode([640, 396])  # 设定窗口

sur = pygame.Surface([600, 400])  # 绘制背景容器
clr = (0, 0, 255)
posAll = [[100, 150], [300, 150], [500, 150], [200, 300], [400, 300]]  # 六个位置
rad = 50
tick = 0  # 计数器
pos = posAll[0]  # 外面记录圆的位置

# 分数
score = 0  # 分数计数
pygame.font.init()  # 初始化文字
score_font = pygame.font.Font("MicrosoftYaqiHeiLight-2.ttf", 30)  # ！！设定字体和字号
score_sur = score_font.render(str(score), False, (255, 0, 0))  # ！！生成计数表面

# 鼠标
pygame.mouse.set_visible(False)  # !!隐藏鼠标
mpos = [300, 200]  # !!记录鼠标位置

times = 0  # 地鼠跳出的次数
times_max = 10  # 最多次数
tick_max = 30  # 地鼠每次跳多少帧
map = pygame.image.load("dds-map.jpg")  # ！！读取图片
rat1 = pygame.image.load("rat1.png")  # ！！读取地鼠图片
rat2 = pygame.image.load("rat2.png")  # ！！读取被砸地鼠图片
ham1 = pygame.image.load("hammer1.png")  # ！！读取锤子图片
ham2 = pygame.image.load("hammer2.png")  # ！！读取砸下锤子图片

gameover = 0  # ！！结束计时
gameover_max = 100  # ！！结束计时最大值，超过这个值就重新开始

# 音乐和音效
pygame.mixer.music.load("bg.mp3")  # ！！载入背景音乐
pygame.mixer.music.play(-1)  # ！！无限播放背景音乐
hitsound = pygame.mixer.Sound("hit.wav")  # ！！载入击打声音
hurtsound = pygame.mixer.Sound("aiyo2.wav")  # ！！载入地鼠叫声


while 1:
    ham_sur = ham1
    rat_sur = rat1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:  # 如果是鼠标按下事件
            ham_sur = ham2  # 使用下落锤子
            hitsound.play()  # ！！播放击打声音
            mpos = pygame.mouse.get_pos()  # 获取鼠标位置
            dis = pygame.math.Vector2(mpos[0] - pos[0], mpos[1] - pos[1])  # 计算坐标差
            len = pygame.math.Vector2.length(dis)  # 计算距离
            if len < rad:
                tick = 1000  # 立即变换位置
                score = score + 1  # 计分增加
                rat_sur = rat2  # 使用被砸地鼠
                hurtsound.play()  # ！！播放地鼠声音
        elif event.type == MOUSEMOTION:  # 当鼠标移动的时候
            mpos = pygame.mouse.get_pos()  # 更新鼠标位置

    if times >= times_max:
        # 显示结束画面
        sur.fill((0, 0, 0))  # 结束时候仍然用黑色清空画面
        pygame.mouse.set_visible(True)
        end_font = pygame.font.Font("MicrosoftYaqiHeiLight-2.ttf", 48)  # 设定字体和字号
        end_sur = score_font.render(
            "你的分数是:{}/{}！".format(score, times_max), True, (255, 0, 0)
        )  # 生成计数表面
        sur.blit(end_sur, (100, 150))
        cd = int((gameover_max - gameover) / 10)
        cd_sur = score_font.render(
            "重新开始倒计时{}".format(cd), True, (255, 0, 0)
        )  # 生成计数表面
        sur.blit(cd_sur, (100, 200))  # 增加分数表面
        gameover = gameover + 1  # ！！增加结束计时
    else:
        sur.blit(map, (0, 0))  # 添加背景图片
        score_sur = score_font.render(
            "分数:{}/{}！".format(score, times + 1), False, (255, 0, 0)
        )  # 重新生成分数文字表面
        sur.blit(score_sur, (200, 10))  # 增加分数表面
        if tick > tick_max:  # 每50次刷新变换一次
            times = times + 1  # 增加计次
            a = random.randint(0, 4)  # 随机0到4
            pos = posAll[a]  # 更新外部记录的圆的位置
            tick = 0  # 重置计数器
        else:  # 不刷新变换的时候
            tick = tick + 1  # 增加计数器
        if tick > 5:  # 开始几帧不显示地鼠
            sur.blit(rat_sur, (pos[0] - 50, pos[1] - 70))  # 绘制地鼠
        sur.blit(ham_sur, (mpos[0] - 50, mpos[1] - 100))  # 绘制锤头

    # 刷新画面
    window.blit(sur, (0, 0))
    pygame.display.flip()  # 刷新画面
    time.sleep(0.04)  # 保持画面一点时间

    # 重置游戏
    if gameover > gameover_max:
        pygame.mouse.set_visible(False)
        times = 0
        score = 0
        gameover = 0
