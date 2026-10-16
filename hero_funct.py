# This is functions for hero_way
import numpy as np
from copy import deepcopy

def create_arr():
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    area_list = []

    print("Add rows string-wise (separated values by space)\n")
    for i in range(rows):
        row = list(map(int, input().split()))     # Adding rows
        area_list.append(row)
    area = np.array(area_list)         # Creating array
    return area

def step_up(hero, area):
    area[hero[0] - 1, hero[1]] = 1
    area[hero[0], hero[1]] = 0
    return area

def step_down(hero, area):
    area[hero[1] + 1, hero[1]] = 1
    area[hero[0], hero[1]] = 0
    return area

def step_right(hero, area):
    area[hero[0], hero[1] + 1] = 1
    area[hero[0], hero[1]] = 0
    return area
 
def step_left(hero, area):
    area[hero[0], hero[1] - 1] = 1
    area[hero[0], hero[1]] = 0
    return area


def travers_upper_wall(area, hero, point):
    right = 0
    area_1 = area.copy()
    hero_1 = deepcopy(hero)
    while area_1[hero_1[0]-1, hero_1[1]] == 3:
        hero_1 = np.where(area_1 == 1)
        area_1 = step_right(hero_1, area_1)
        hero_1 = np.where(area_1 == 1)
        right += 1
    left = 0
    area_1 = area.copy()
    hero_1 = deepcopy(hero)
    while area_1[hero_1[0]-1, hero_1[1]] == 3:
        hero_1 = np.where(area_1 == 1)
        area_1 = step_left(hero_1, area_1)
        hero_1 = np.where(area_1 == 1)
        left += 1

    if right <= left:
        while area[hero[0]-1, hero[1]] == 3:
            area = step_right(hero, area)
            print(area, "\n")
            hero = np.where(area == 1)
    elif left < right:
        while area[hero[0]-1, hero[1]] == 3:
            area = step_left(hero, area)
            print(area, "\n")
            hero = np.where(area == 1)
    return area, hero, point


def travers_lower_wall(hero, point, area):
    return None


def simple_steps(area, hero, point):
    while hero[0] != point[0]:  # Main loop
    
        if hero[0] > point[0] and area[hero[0]-1, hero[1]] == 3:
            area, hero, point = travers_upper_wall(area, hero, point)
            
        elif hero[0] > point[0]:
            area = step_up(hero, area)  # step_up
            print(area, "\n")

        elif hero[0] < point[0]:
            area = step_down(hero, area)
            print(area, "\n")
        hero = np.where(area == 1)

    while hero[1] !=  point[1]:

        if hero[1] > point[1]:
            area = step_left(hero, area) # step_left
            print(area, "\n")

        elif hero[1] < point[1]:
            area = step_right(hero, area) #step_right
            print(area, "\n")
        hero = np.where(area == 1)  #get coordinates of hero
    return area, hero, point

