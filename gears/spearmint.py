
from manim import VGroup, Scene, config
from sympy import Matrix
from math import sin, cos, tau as circle

CURRENT = 0

def rotate_unit_line(origin, theta):
    global CURRENT
    my_theta = theta + CURRENT
    x, y = origin
    y += 1  # vertical unit stick
    r = Matrix(
        [
            [cos(my_theta), -sin(my_theta)],
            [sin(my_theta),  cos(my_theta)],
        ]
    )
    CURRENT = my_theta
    x, y = r * Matrix([x, y])
    return x, y

num_sticks = 2
locations = [(0, num_sticks)]
angles = [(circle/8)*n for n in range(1, 2)]
for angle in angles:
    location = 0, 0
    for _ in range(0, num_sticks):
        location = rotate_unit_line(location, angle)
        import ipdb; ipdb.set_trace()
    locations.append(location)

config.quality = "low_quality"
scene = Scene()
cycle = VGroup()
cycle.set_points_as_corners([(x, y, 0) for (x,y) in locations])
scene.add(cycle)
scene.render()

if False:
    origin_x, origin_y = origin
    nib_x, nib_y = origin_x, origin_y + 1
    r = Matrix(
        [
            [cos(my_theta), -sin(my_theta)],
            [sin(my_theta),  cos(my_theta)],
        ]
    )
    new_origin_x, new_origin_y = r * Matrix([nib_x, nib_y])
    dx, dy = new_origin_x - origin_x, new_origin_y - origin_y