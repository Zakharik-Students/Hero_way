import numpy as np
from copy import deepcopy

def create_arr():
    rows = int(input("Rows: "))
    area_list = []   # list for input
    print("Add rows string-wise (separate value by space)", "\n")
    for i in range(rows):
        row = list(map(int, input().split()))
        area_list.append(row)
    area = np.array(area_list)    # Creating array
    return area

def step_up(hero, area):
    area[hero[0]-1, hero[1]] = 1
    area[hero[0], hero[1]] = 0
    return area

def step_down(hero, area):
    area[hero[0]+1, hero[1]] = 1
    area[hero[0], hero[1]] = 0
    return area

def step_left(hero, area):
    area[hero[0], hero[1]-1] = 1
    area[hero[0], hero[1]] = 0
    return area

def step_right(hero, area):
    area[hero[0], hero[1]+1] = 1
    area[hero[0], hero[1]] = 0
    return area

def horisontal_wall_length(area, hero, side_of_wall):
    right, left = 0, 0
    area_1 = area.copy()
    hero_1 = deepcopy(hero)
    while area_1[hero_1[0]-side_of_wall, hero_1[1]] == 3:
        area_1 = step_right(hero_1, area_1)
        hero_1 = np.where(area_1 == 1)
        right += 1
    area_1 = area.copy()
    hero_1 = deepcopy(hero)
    while area_1[hero_1[0]-side_of_wall, hero_1[1]] == 3:
        area_1 = step_left(hero_1, area_1)
        hero_1 = np.where(area_1 == 1)
        left += 1
    return ("right", right) if right <= left else ("left", left)

def horisontal_wall_travers(area, hero, point, side_of_wall):
    side_and_length = horisontal_wall_length(area, hero, side_of_wall)
    side, length = side_and_length[0], side_and_length[1]
    if side  == "right":
        for i in range(length):
            area = step_right(hero, area)
            print(area, "\n")
            hero = np.where(area == 1)
    else:
        for i in range(length):
            area = step_left(hero, area)
            print(area, "\n")
            hero = np.where(area == 1)
    return area, hero

def vertical_wall_length(area, hero, side_of_wall):
    up, down = 0, 0
    area_1 = area.copy()
    hero_1 = deepcopy(hero)
    while area_1[hero_1[0], hero_1[1]-side_of_wall] == 3:
        area_1 = step_up(hero_1, area_1)
        hero_1 = np.where(area_1 == 1)
        up += 1
    area_1 = area.copy()
    hero_1 = deepcopy(hero)
    while area_1[hero_1[0], hero_1[1]-side_of_wall] == 3:
        area_1 = step_down(hero_1, area_1)
        hero_1 = np.where(area_1 == 1)
        down += 1
    return ("up", up) if up <= down else ("down", down)

def vertical_wall_travers(area, hero, point, side_of_wall):
    side_and_length = vertical_wall_length(area, hero, side_of_wall)
    side, length = side_and_length[0], side_and_length[1]
    if side  == "up":
        for i in range(length):
            area = step_up(hero, area)
            print(area, "\n")
            hero = np.where(area == 1)
    else:
        for i in range(length):
            area = step_down(hero, area)
            print(area, "\n")
            hero = np.where(area == 1)
    return area, hero


def simple_steps(area, hero, point):
    while hero[0] != point[0]:
        if hero[0] > point[0] and area[hero[0]-1, hero[1]] == 3:
            area, hero = horisontal_wall_travers(area, hero, point, 1)
        elif hero[0] > point[0]:
            area = step_up(hero, area)
            print(area, "\n")
        if hero[0] < point[0] and area[hero[0]+1, hero[1]] == 3:
            area, hero = horisontal_wall_travers(area, hero, point, -1) 
        elif hero[0] < point[0]:
            area = step_down(hero, area)
            print(area, "\n")
        hero = np.where(area == 1)

    while hero[1] != point[1]:
        if hero[1] > point[1] and area[hero[0], hero[1]-1] == 3:
            area, hero = vertical_wall_travers(area, hero, point, 1)
        elif hero[1] > point[1]:
            area = step_left(hero, area)
            print(area, "\n")
        if hero[1] < point[1] and area[hero[0], hero[1]+1] == 3:
            area, hero = vertical_wall_travers(area, hero, point, -1)
        elif hero[1] < point[1]:
            area = step_right(hero, area)
            print(area, "\n")
        hero = np.where(area == 1)
    return area, hero
        
def main_loop(area, hero, point):
    while True:
        area, hero = simple_steps(area, hero, point)
        if hero[0] == point[0] and hero[1] == point[1]:
            break
