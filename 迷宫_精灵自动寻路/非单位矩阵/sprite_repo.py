


from settings import *


class Sprite_Fact(pygame.sprite.Sprite):
    """ 精灵图_精灵类 """

    def __init__(self):
        super(Sprite_Fact, self).__init__()
        self.area = 1                # 帧号
        self.master_image = None     # 精灵总图
        self.area_width = 1          # 帧图宽
        self.area_height = 1         # 帧图高
        self.first_area = 0          # 起始帧号
        self.last_area = 0           # 终止帧号
        self.old_area = -1           # 前一帧的帧号
        self.columns = 1             # 精灵图中每行帧列图中的帧数
        self.last_time = 0           # 前一帧号图绘制时间
        self.vel = pygame.Vector2(0, 0)     # 移动速度 (x, y) , velocity
        self.acc = pygame.Vector2(0, 0)     # 移动加速度 (x, y) , acceleration
        self.is_move = False         # 移动开关
        self.old_dir = self.direction
        self.direction = 0           # 移动方向， 代表精灵总图的第几行
        self.auto_move_switch = False # 自动移动开关
        self.routes = []              # 移动路径
        self.matrix_cell_size = matrix_cell_size # 地图中的矩阵方格的尺寸
        self.move_size = move_size            # 移动一次所走的像素长度
        assert self.matrix_cell_size % self.move_size == 0
        # 移动一次矩阵方格所需移动的次数
        self.ness_move_num = self.matrix_cell_size // self.move_size


    def _get_x(self):
        return self.rect.x
    def _set_x(self, x):
        self.rect.x = x
    X = property(_get_x, _set_x)

    def _get_y(self):
        return self.rect.y
    def _set_y(self, y):
        self.rect.y = y
    Y = property(_get_y, _set_y)

    # 更新动画绘制位置
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos
    position = property(_getpos,_setpos)

    def _get_dir(self):
        return (self.first_area, self.last_area)
    def _set_dir(self, direction):
        if direction == self.old_dir:
            return
        self.first_area = direction * self.columns
        self.last_area = self.first_area + self.columns - 1
    direction = property(_get_dir, _set_dir)

    def load(self, image, width, height, columns):
        """ 加载精灵图与初始化 """
        self.master_image = pygame.image.load(image)
        self.area_width = width
        self.area_height = height
        self.rect = pygame.Rect(0, 0, width, height)
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_area = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate = 30):
        """ 更新动画帧图， 确定 self.image """

        # 移动控制
        if not self.is_move:
            self.area = self.last_area = self.first_area
        # 控制动画的绘制速率
        elif current_time > self.last_time + rate:
            self.area += 1
            # 帧区间边界判断
            if self.area > self.last_area:
                self.area = self.first_area
            if self.area < self.first_area:
                self.area = self.first_area
            # 记录当前时间
            self.last_time = current_time
        # 只有当帧号发生更改时才更新 self.image ************
        if self.area != self.old_area:
            area_x = (self.area % self.columns) * self.area_width
            area_y = (self.area // self.columns) * self.area_height
            rect = pygame.Rect(area_x, area_y, self.area_width, self.area_height)
            # 子表面 Surface
            try:
                self.image = self.master_image.subsurface(rect)
                self.image.set_colorkey((201, 202, 203, 255))
            except Exception as e:
                print(e + " \n图片剪裁超出范围........")
            self.old_area = self.area

    def move(self,):
        """ 移动精灵 """
        # if self.is_move:
        self.rect.move_ip(self.vel)

    def draw(self, screen):
        """ 绘制精灵 """
        screen.blit(self.image, self.rect)

    def go_one_step(self, x, y):
        """
        :param x: 目标坐标
        :param y: 目标坐标
        """
        self.next_x = x
        self.next_y = y

        # 设置人物面向
        if self.next_x > self.rect.centerx:
            self.direction, self.vel.x, self.vel.y = Move_Dir_Dict[pygame.K_RIGHT]
        elif self.next_x < self.rect.centerx:
            self.direction, self.vel.x, self.vel.y  = Move_Dir_Dict[pygame.K_LEFT]
        if self.next_y > self.rect.bottom:
            self.direction, self.vel.x, self.vel.y  = Move_Dir_Dict[pygame.K_DOWN]
        elif self.next_y < self.rect.bottom:
            self.direction, self.vel.x, self.vel.y  = Move_Dir_Dict[pygame.K_UP]
        self.move()
        self.auto_move_switch = True


    def charge_dir(self, sour_pos, dest_pos):
        """ 判断将要移动的方向 """

        assert isinstance(sour_pos, (list, tuple, pygame.Vector2)) and len(sour_pos) == 2
        assert isinstance(dest_pos, (list, tuple, pygame.Vector2)) and len(dest_pos) == 2

        offset_x = dest_pos[0] - sour_pos[0]
        offset_y = dest_pos[1] - sour_pos[1]

        if offset_x == 0 and offset_y < 0:
            return pygame.K_UP
        elif offset_x == 0 and offset_y > 0:
            return pygame.K_DOWN
        elif offset_x < 0 and offset_y == 0:
            return pygame.K_LEFT
        elif offset_x > 0 and offset_y == 0:
            return pygame.K_RIGHT
        else:
            return None

    # def auto_move(self, routes):
    #     """ 自动移动逻辑 """

