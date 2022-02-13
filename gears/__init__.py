from math import tau, sin, cos
from sympy import Matrix


class Gear:
    def __init__(self, ratio=1, arm=1, parent=None):
        self.ratio = ratio
        self.arm = arm
        self.parent = parent

    def iter_nib(self, angle):
        lineage = self.get_lineage()
        origin = 0, 0
        total_angle = 0
        for gear in lineage:
            total_angle += angle
            origin, angle = gear.rotate(origin, total_angle)
        return origin

    def get_lineage(self):
        ancestry = [self]
        while ancestry[-1].parent is not None:
            ancestry.append(ancestry[-1].parent)
        return list(reversed(ancestry))

    def rotate(self, origin, angle):
        origin_x, origin_y = origin
        output = self.ratio * angle
        r = Matrix(
            [
                [cos(output), -sin(output), 0],
                [sin(output), cos(output), 0],
                [0, 0, 1],
            ]
        )
        x, y, _ = r * Matrix([origin_x, origin_y + self.arm, 1])
        return (x, y), output

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, id(self))


if __name__ == "__main__":
    g0 = Gear()
    g1 = Gear(parent=g0)
    print(g1.iter_nib(tau / 8))
