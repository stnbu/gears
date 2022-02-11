
from manim import VGroup, Scene, config
from sympy import Matrix
from math import sin, cos, tau as circle

CURRENT = 0

def rotate_unit_line(origin, theta):
    global CURRENT
    angle = theta + CURRENT




    about_x, about_y = origin
    r = Matrix(
        [
            [cos(angle), -sin(angle)],
            [sin(angle),  cos(angle)],
        ]
    )
    rotated_about_x, rotated_about_y = r * Matrix([about_x, about_y])
    dx, dy = rotated_about_x - about_x, rotated_about_y - about_y
    def worker(point):
        x, y = r * Matrix(point)
        return x - dx, y - dy

    point = worker([about_x, about_y + 1])
    CURRENT = angle
    return point

num_sticks = 2
locations = [(0, num_sticks)]
angles = [(circle/8)*n for n in range(1, 2)]
for angle in angles:
    location = 0, 0
    for _ in range(0, num_sticks):
        location = rotate_unit_line(location, angle)
    locations.append(location)

config.quality = "low_quality"
scene = Scene()
cycle = VGroup()
cycle.set_points_as_corners([(x, y, 0) for (x,y) in locations])
scene.add(cycle)
scene.render()
