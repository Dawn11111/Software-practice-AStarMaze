from random import randint, choice
from enum import Enum


# 迷宫通路、墙、起点和终点
class MAP_ENTRY_TYPE (Enum):
    MAP_EMPTY = 0,
    MAP_BLOCK = 1,
    MAP_START = 2,
    MAP_END = 3,


class WALL_DIRECTION(Enum):
    WALL_LEFT = 0,
    WALL_UP = 1,
    WALL_RIGHT = 2,
    WALL_DOWN = 3,


class Map():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]

    def resetMap(self, value):
        for y in range(self.height):
            for x in range(self.width):
                self.setMap(x, y, value)

    # 地图的设置
    def setMap(self, x, y, value):
        if value == MAP_ENTRY_TYPE.MAP_EMPTY:
            self.map[y][x] = 0
        elif value == MAP_ENTRY_TYPE.MAP_BLOCK:
            self.map[y][x] = 1
        elif value == MAP_ENTRY_TYPE.MAP_START:
            self.map[y][x] = 2
        elif value == MAP_ENTRY_TYPE.MAP_END:
            self.map[y][x] = 3

    # 判断是否已经访问过（访问过则代表不设定为墙
    def isVisited(self, x, y):
        return self.map[y][x] != 1

    # 将生成的地图写入data.txt文件
    def showMap(self):
        # coding=UTF-8
        filename = 'data.txt'
        # 初始化data文件，删除原有内容成为空白文件
        with open(filename, 'w') as file_object:
            file_object.write("")
        for row in self.map:
            s = "    '"
            with open(filename, 'a') as file_object:
                file_object.write("    '")
            for entry in row:
                # 通路
                if entry == 0:
                    s += '.'
                    with open(filename, 'a') as file_object:
                        file_object.write(".")
                # 墙
                elif entry == 1:
                    s += '#'
                    with open(filename, 'a') as file_object:
                        file_object.write("#")
                # 起点
                elif entry == 2:
                    s += 'S'
                    with open(filename, 'a') as file_object:
                        file_object.write("S")
                # 终点
                else:
                    s += 'E'
                    with open(filename, 'a') as file_object:
                        file_object.write("E")
            s += "',"
            with open(filename, 'a') as file_object:
                file_object.write("',\n")
            print(s)


# 找出与当前位置相邻的墙（四个方向
# 然后将其中一个方向的墙随机添加到checklist中，并将其标记为已访问
def checkAdjacentPos(map, x, y, width, height, checklist):
    directions = []
    # 如果当前位置处在边界（即最多只有三个相邻墙位置
    if x > 0:
        if not map.isVisited(2 * (x - 1) + 1, 2 * y + 1):
            directions.append(WALL_DIRECTION.WALL_LEFT)

    if y > 0:
        if not map.isVisited(2 * x + 1, 2 * (y - 1) + 1):
            directions.append(WALL_DIRECTION.WALL_UP)

    if x < width - 1:
        if not map.isVisited(2 * (x + 1) + 1, 2 * y + 1):
            directions.append(WALL_DIRECTION.WALL_RIGHT)

    if y < height - 1:
        if not map.isVisited(2 * x + 1, 2 * (y + 1) + 1):
            directions.append(WALL_DIRECTION.WALL_DOWN)

    # 如果当前位置四周的相邻结点有墙
    if len(directions):
        # 随机选择一个方向的墙
        direction = choice(directions)
        if direction == WALL_DIRECTION.WALL_LEFT:
            map.setMap(2 * (x - 1) + 1, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x - 1, y))
        elif direction == WALL_DIRECTION.WALL_UP:
            map.setMap(2 * x + 1, 2 * (y - 1) + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x + 1, 2 * y, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x, y - 1))
        elif direction == WALL_DIRECTION.WALL_RIGHT:
            map.setMap(2 * (x + 1) + 1, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x + 2, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x + 1, y))
        elif direction == WALL_DIRECTION.WALL_DOWN:
            map.setMap(2 * x + 1, 2 * (y + 1) + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x + 1, 2 * y + 2, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x, y + 1))
        return True
    else:
        # 找不到四周有未经访问的墙（即周边的墙都已经访问过
        return False


# 随机prim算法
def randomPrim(map, width, height):
    # 起始点的设置
    startX, startY = (0, 0)
    map.setMap(2*startX+0, 2*startY+1, MAP_ENTRY_TYPE.MAP_START)
    # 终点的设置
    endX, endY = (width, height)
    map.setMap(2*endX-0, 2*endY-1, MAP_ENTRY_TYPE.MAP_END)

    checklist = []
    checklist.append((startX, startY))
    while len(checklist):
        # 从checklist中选择一个随机方向的墙
        entry = choice(checklist)
        if not checkAdjacentPos(map, entry[0], entry[1], width, height, checklist):
            # 如果四周的墙都已访问过，则把该结点位置从checklist中删除
            checklist.remove(entry)


def doRandomPrim(map):
    # 将地图的所有结点位置都设置为墙
    map.resetMap(MAP_ENTRY_TYPE.MAP_BLOCK)
    randomPrim(map, (map.width - 1) // 2, (map.height - 1) // 2)


def run():
    WIDTH = 41
    HEIGHT = 31
    map = Map(WIDTH, HEIGHT)
    doRandomPrim(map)
    map.showMap()


if __name__ == "__main__":
    run()
