# file just with simple steps functions

import numpy as np

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
