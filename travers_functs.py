# funct for check any length of wall and travers it

import numpy as np
from copy import deepcopy
from step_functs import step_up, step_down, step_right, step_left

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
 
