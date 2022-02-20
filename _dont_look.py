from gears import Gear
from manim import *
from sympy import Matrix
import math

def ratio_01(origin, angle):
    return math.sqrt(origin[0] ** 2 + origin[1] ** 2)

def arm_01(origin, angle):
    return 10 / math.sqrt(origin[0] ** 2 + origin[1] ** 2)

def arm_02(origin, angle):
    return angle / 2

g0 = Gear()
g1 = Gear(parent=g0, arm=arm_02)
g2 = Gear(ratio=0.5, parent=g1)
g3 = Gear(ratio=-1.5, arm=arm_01, parent=g2)
g4 = Gear(ratio=ratio_01, parent=g3)

gears = [g0, g1, g2, g3, g4]

colors = [
    [BLACK, WHITE],
    [PURPLE, ORANGE],
    [YELLOW, ORANGE],
    [WHITE, BLACK],
    [BLUE, GREEN],
]

for gear in gears:
    gear.do()
    
cycle_locations = {}
for i, gear in enumerate(gears):
    cycle_locations[i] = [
        (*value, 0) for (_, value) in sorted(gear.locations.items())
    ][1:]
