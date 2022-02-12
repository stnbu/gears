from manim import VGroup, Scene, config
from sympy import Matrix
from math import sin, cos, tau as circle


def rotate_unit_line(origin, angle):
    origin_x, origin_y = origin
    if angle == 0:
        return origin_x, origin_y + 1
    r = Matrix(
        [
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1],
        ]
    )
    x, y, _ = r * Matrix([origin_x, origin_y + 1, 1])
    return x, y


def iter_stick_tower_points(num_sticks, sample_angle):
    angle = 0
    while angle <= circle:
        location = 0, 0
        for height in range(0, num_sticks):
            location = rotate_unit_line(location, angle * (height + 1))
        angle += sample_angle
        yield location


if __name__ == "__main__":
    scene = Scene()
    cycle = VGroup()
    locations = iter_stick_tower_points(2, circle / 1000)
    cycle.set_points_as_corners([(x, y, 0) for (x, y) in locations])
    scene.add(cycle)
    scene.render()
