
import copy

from core.stack import Stack
from core.settings import *
from core.handler import Ele_Sprite

# 关卡
class Level:
    """ 关卡管理类 """


    # 矩阵元素
    CHAN, WALL, BOX, PERSON, GOAL, HOME, REPO = 0,1,2,3,4,5,6
    # 键盘方向键
    UP, RIGHT, BOTTOM, LEFT = 1, 2, 3, 4

    def __init__(self, screen):
        self.game_level = 4            # 当前关卡等级
        self.frame = copy.deepcopy(Grade_Data[self.game_level])   # 当前游戏数据  *********
        self.screen = screen           # 窗口Surface对象
        self.hero_dir = 2              # 玩家移动的方向索引
        self.undo_stack = Stack(5)     # 撤销栈类实例
        self.step = 0                  # 玩家移动步数
        self.old_frame = copy.deepcopy(self.frame) # 在移动之前记录关卡矩阵

    @property
    def level(self):
        return self.game_level

    @level.setter
    def level(self, lev):
        self.game_level = lev
        self.frame = copy.deepcopy(Grade_Data[self.game_level])

    # 获取玩家位置
    @property
    def person_posi(self):
        """ 获取玩家位置 """
        for row, li in enumerate(self.frame):   #  *****  good
            for col, val in enumerate(li):
                if val in [3, 5]:
                    return (row, col)


    # 记录玩家移动前的矩阵
    def record_frame(self):
        """ 记录玩家移动前的矩阵 """
        if self.is_move():
            self.undo_stack.push(copy.deepcopy(self.old_frame))
            self.stack_push_switch = False
