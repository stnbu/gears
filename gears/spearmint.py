
from sympy import Matrix
from math import pi, sin, cos

CURRENT = 0.0

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

location = 0.0, 0.0
for _ in range(0, 2):
    location = rotate_unit_line(location, pi/4)

print(location)
