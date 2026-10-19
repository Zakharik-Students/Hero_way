# Make some function for cleaness of code and future feachures

from main_functs import create_arr, simple_steps, main_loop
import numpy as np
from const import HERO, POINT, WALL

area = create_arr()      # Get array from function
hero = np.where(area == HERO)  #get coordinates of hero
point = np.where(area == POINT) #get coordintes of point
wall = np.where(area == WALL)
print("\n", area, "\n", sep='')

main_loop(area, hero, point)
