# Make some function for cleaness of code and future feachures

from hero_funct_2 import create_arr, simple_steps, main_loop
import numpy as np


area = create_arr()      # Get array from function
hero = np.where(area == 1)  #get coordinates of hero
point = np.where(area == 2) #get coordintes of point
wall = np.where(area == 3)
print("\n", area, "\n", sep='')

main_loop(area, hero, point)
