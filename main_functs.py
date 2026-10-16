import numpy as np
from step_functs import step_up, step_down, step_left, step_right
from travers_functs import horisontal_wall_travers, vertical_wall_travers

def create_arr():
    rows = int(input("Rows: "))
    area_list = []   # list for input
    print("Add rows string-wise (separate value by space)", "\n")
    for i in range(rows):
        row = list(map(int, input().split()))
        area_list.append(row)
    area = np.array(area_list)    # Creating array
    return area

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
