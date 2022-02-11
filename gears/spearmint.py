
from manim import VGroup, Scene, config
from sympy import Matrix
from math import sin, cos, tau as circle

CURRENT = 0

def rotate_unit_line(origin, theta):
    global CURRENT
    angle = theta + CURRENT




    origin_x, origin_y = origin
    r = Matrix(
        [
            [cos(angle), -sin(angle), 0],
            [sin(angle),  cos(angle), 0],
            [0,0,1],
        ]
    )
    x, y, _ = r * Matrix([origin_x, origin_y + 1, 1])
    CURRENT = angle
    return x, y

num_sticks = 2
locations = [(0, num_sticks)]
angles = [(circle/1000)*n for n in range(1, 25)]
for angle in angles:
    location = 0, 0
    for _ in range(0, num_sticks):
        location = rotate_unit_line(location, angle)
    locations.append(location)

#import ipdb; ipdb.set_trace()
config.quality = "low_quality"
scene = Scene()
cycle = VGroup()
cycle.set_points_as_corners([(x, y, 0) for (x,y) in locations])
scene.add(cycle)
scene.render()
