from manim import VGroup, Scene, config
from sympy import Matrix
from math import sin, cos, tau as circle


def rotate_unit_line(origin, angle):
    origin_x, origin_y = origin
    r = Matrix(
        [
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1],
        ]
    )
    x, y, _ = r * Matrix([origin_x, origin_y + 1, 1])
    return x, y


def get_stick_tower_points(num_sticks, sample_angle):
    # (0, num_sticks)]
    angles = [sample_angle * n for n in range(1, 3000)]
    for angle in angles:
        location = 0, 0
        for height in range(0, num_sticks):
            location = rotate_unit_line(location, angle * (height + 1))
        yield location


locations = get_stick_tower_points(2, circle / 1000)

config.quality = "low_quality"
scene = Scene()
cycle = VGroup()
cycle.set_points_as_corners([(x, y, 0) for (x, y) in locations])
scene.add(cycle)
scene.render()
