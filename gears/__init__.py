from math import sin, cos, tau as circle
from sympy import Matrix


class Gear:
    def __init__(self, ratio=1, arm=1, parent=None):
        self.ratio = ratio
        self.arm = arm
        self.parent = parent
        self.results = {}

    def get_nib(self, angle):
        input_angle = angle
        lineage = self.get_lineage()
        origin = 0, 0
        total_angle = 0
        gamma = 1
        for gear in lineage:
            total_angle += angle
            origin, angle = gear.rotate(origin, total_angle)
            _gamma = 1 if angle == 0 else input_angle / abs(angle)
            if gamma > _gamma:
                gamma = _gamma
        return origin, gamma

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

    def do(self):
        locations = []
        sample_angle = circle / 100
        angle = 0
        while angle <= circle:
            location, gamma = self.get_nib(angle)
            angle += sample_angle * gamma
            locations.append(location)
        return locations


if __name__ == "__main__":
    from manim import VGroup, Scene

    g0 = Gear()
    g1 = Gear(parent=g0)
    g2 = Gear(ratio=0.5, parent=g1)
    g3 = Gear(ratio=-1.5, parent=g2)
    g4 = Gear(ratio=1.1, parent=g3)
    locations = g3.do()

    scene = Scene()
    cycle = VGroup()
    cycle.set_points_as_corners([(x, y, 0) for (x, y) in locations])
    scene.add(cycle)
    scene.render()
