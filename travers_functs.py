# funct for check any length of wall and travers it

import numpy as np
from copy import deepcopy
from step_functs import step_up, step_down, step_right, step_left
from const import HERO, POINT, WALL

def condition_1(area_1, hero_1, side_of_wall) -> bool:
    if hero_1[1] <= np.size(area_1, axis=1)-2:
        if area_1[hero_1[0], hero_1[1]] != 3:
            return True
        else:
            return False
    else:
            return False

def condition_2(area_1, hero_1, side_of_wall) -> bool:
    if hero_1[1] == 0:
        return False
    else:
        return True

def condition_3(area_1, hero_1, side_of_wall) -> bool:
    if hero_1[0] <= np.size(area_1, axis=0)-2:
        if area_1[hero_1[0], hero_1[1]] != 3:
            return True
        else:
            return False
    else:
            return False

def condition_4(area_1, hero_1, side_of_wall) -> bool:
    if hero_1[0] == 0:
        return False
    else:
        return True


def _wall_length(area, hero, side_of_wall):
    up, down, right, left = 0, 0, 0, 0
    area_1 = area.copy()
    hero_1 = deepcopy(hero)
    while area_1[hero_1[0]-side_of_wall[0], hero_1[1]-side_of_wall[1]] == WALL:
        if side_of_wall[0]:        
            if condition_1(area_1, hero_1, side_of_wall): 
                area_1 = step_right(hero_1, area_1)
                hero_1 = np.where(area_1 == HERO)
                right += 1
            else:
                right = 1000
                break
        else:
            if condition_3(area_1, hero_1, side_of_wall):
                area_1 = step_down(hero_1, area_1)
                hero_1 = np.where(area_1 == HERO)
                down += 1
            else:
                down = 1000
                break
    area_1 = area.copy()
    hero_1 = deepcopy(hero)
    while area_1[hero_1[0]-side_of_wall[0], hero_1[1]-side_of_wall[1]] == WALL:
        if side_of_wall[0]:
            if condition_2(area_1, hero_1, side_of_wall):
                area_1 = step_left(hero_1, area_1)
                hero_1 = np.where(area_1 == HERO)
                left += 1
            else:
                left = 1000
                break
        else:
            if condition_4(area_1, hero_1, side_of_wall):
                area_1 = step_up(hero_1, area_1)
                hero_1 = np.where(area_1 == HERO) 
                up += 1
            else:
                up = 1000
                break
    if side_of_wall[0]:
        return ("right", right) if right <= left else ("left", left)
    else:
        return ("down", down) if down <= up else("up", up)

def wall_travers(area, hero, point, side_of_wall):
    side_and_length = _wall_length(area, hero, side_of_wall)
    side, length = side_and_length[0], side_and_length[1]
    if side  == "up":
        for i in range(length):
            area = step_up(hero, area)
            print(area, "\n")
            hero = np.where(area == HERO)
    elif side == "down":
        for i in range(length):
            area = step_down(hero, area)
            print(area, "\n")
            hero = np.where(area == HERO)
    elif side  == "right":
        for i in range(length):
            area = step_right(hero, area)
            print(area, "\n")
            hero = np.where(area == HERO)
    elif side == "left":
        for i in range(length):
            area = step_left(hero, area)
            print(area, "\n")
            hero = np.where(area == HERO)

    return area, hero
 
