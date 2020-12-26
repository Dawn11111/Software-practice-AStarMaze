#1.创建游戏背景
import turtle as t

import random

# 创建窗口
mz = t.Screen()

# 设置长宽
mz.setup(520,400)
# 设置背景色
mz.bgcolor('#EBEBEB')
# 设置标题
mz.title('MoveMaze')

# 使用照片前先将照片注册
mz.register_shape('images/wall.gif')
mz.register_shape('images/pr.gif')
mz.register_shape('images/la.gif')

# 不用一步一步显示画面，最后一起显示，和mz.update()配合用
mz.tracer(0)


r_map = []
# P：player;
map = [
    '#########################################',
    'S.............#.#...#...................#',
    '#.#.#####.#.###.#.###.###########.#.###.#',
    '#.#.....#.#.....#.....#...#.....#.#...#.#',
    '###.#####.#######.#####.###.###.#######.#',
    '#.......#.................#...#.#...#.#.#',
    '###.#######################.#####.###.#.#',
    '#.........#.#.......................#.#.#',
    '#.#####.#.#.#.#############.#####.###.###',
    '#.#.....#...#.............#.....#.......#',
    '#.#####.#####.#######.###.#.#.###.#.#.#.#',
    '#.#...............#.....#.#.#...#.#.#.#.#',
    '#.#####.#.#.#.#############.###########.#',
    '#.#.....#.#.#.............#.........#.#.#',
    '#.###.#.#########.#.#######.#####.###.###',
    '#...#.#.........#.#.......#.....#.#.....#',
    '###.#.#.#.#.#.###.#.#####.#########.#.###',
    '#...#.#.#.#.#...#.#.....#...........#.#.#',
    '#.#.#.###.###.###.#########.#.#.#.#####.#',
    '#.#.#.#.....#...#.....#...#.#.#.#.......#',
    '#.#.#.#.#####.#.#.#.#.#.#######.#.#.#####',
    '#.#.#.#.....#.#.#.#.#.........#.#.#.....#',
    '#.#.###.#####.###.#.#.#.#####.#.#.###.###',
    '#.#...#.#.......#.#.#.#.....#.#.#...#...#',
    '#.#.#.#.#####.###.#.#.###.#####.#.#.###.#',
    '#.#.#.#.....#...#.#.#.#.#...#...#.#...#.#',
    '###.#.#########.#.#.#.#.###########.#.#.#',
    '#...#.........#.#.#.#.............#.#.#.#',
    '#.#.#.###.#####.###.#.#.###.#.###.#.#####',
    '#.#.#...#...#.....#.#.#...#.#...#.#.....E',
    '#########################################',
]

r_map.append(map)

class Pen(t.Turtle):
    # -----------画笔-------------
    def __init__(self):
        # 继承父类的属性
        super().__init__()
        # 先隐藏起来，隐秘进行运动
        self.ht()
        self.shape('images/wall.gif')
        self.speed(0)
        self.penup()

    # -----------迷宫--------------
    def make_maze(self):
        level = r_map[current - 1]
        for i in range(len(level)):
            # 取出某一行
            row = level[i]
            # 获取到某一元素的坐标
            for j in range(len(row)):
                screen_x = -244 + 12 * j
                screen_y = 185 - 12 * i

                char = row[j]
                #如果元素为X，则画出迷宫
                if char == '#':
                    self.goto(screen_x,screen_y)
                    self.stamp()
                    walls.append((screen_x,screen_y))#元组
                elif char == 'S':
                    player.goto(screen_x,screen_y)
                    player.st()




class Player(t.Turtle):
    #当前位置的移动
    def __init__(self):
        super().__init__()
        # 先隐藏起来，隐秘进行运动
        self.ht()
        self.shape('images/pr.gif')
        self.speed(0)
        self.penup()

    # 右移
    def go_right(self):
        # print('going right')
        self.shape('images/la.gif')
        self.stamp()
        go_x = self.xcor() + 12
        go_y = self.ycor()
        self.shape('images/pr.gif')
        self.move(go_x, go_y)

    # 左移
    def go_left(self):
        # print('going left')
        self.shape('images/la.gif')
        self.stamp()
        go_x = self.xcor() - 12
        go_y = self.ycor()
        self.shape('images/pr.gif')
        self.move(go_x,go_y)

    # 上移
    def go_up(self):
        # print('going up')
        self.shape('images/la.gif')
        self.stamp()
        go_x = self.xcor()
        go_y = self.ycor() + 12
        self.shape('images/pr.gif')
        self.move(go_x, go_y)

    # 下移
    def go_down(self):
        # print('going down')
        self.shape('images/la.gif')
        self.stamp()
        go_x = self.xcor()
        go_y = self.ycor() - 12
        self.shape('images/pr.gif')
        self.move(go_x, go_y)

    # 运动时的共同行为
    def move(self, go_x, go_y):
        if (go_x, go_y) not in walls:
            self.goto(go_x, go_y)
        else:
            print('撞墙了')

current = 1

# 调用画笔类
pen = Pen()

# 调用玩家
player = Player()


# walls数组来存储墙的坐标
walls = []

# 根据不同的关卡绘制迷宫
pen.make_maze()

# 根据键盘移动
mz.listen()
mz.onkey(player.go_right, 'Right')
mz.onkey(player.go_left, 'Left')
mz.onkey(player.go_up, 'Up')
mz.onkey(player.go_down, 'Down')

while True:
    mz.update()

# 提醒窗口不要退出
mz.mainloop()
