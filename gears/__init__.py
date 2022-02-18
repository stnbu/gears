from math import sin, cos, tau as circle
from sympy import Matrix


class FloatDict(dict):
    def __in__(self, key):
        for real_key in self.__dict__:
            if abs(real_key - key) <= 0.00000001:
                return real_key
        return key in self.__dict__


class Gear:
    def __init__(self, ratio=1, arm=1, parent=None):
        self.ratio = ratio
        self.arm = arm
        self.parent = parent
        self.locations = FloatDict()

    def get_nib(self, angle):
        input_angle = angle
        lineage = self.get_lineage()
        origin = 0, 0
        total_angle = 0
        gamma = 1
        for gear in lineage:
            total_angle += angle
            origin, angle = gear.rotate(origin, total_angle)
            gamma = 1 if angle == 0 else input_angle / abs(angle)
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
        sample_angle = circle / 300
        angle = 0
        while angle <= circle * 10:
            if angle in self.locations:
                angle += sample_angle * gamma
                continue
            location, gamma = self.get_nib(angle)
            angle += sample_angle * gamma
            self.locations[angle] = location


if __name__ == "__main__":
    from manim import *
    from sympy import Matrix

    g0 = Gear()
    g1 = Gear(parent=g0)
    g2 = Gear(ratio=0.5, parent=g1)
    g3 = Gear(ratio=-1.5, parent=g2)
    g4 = Gear(ratio=1.1, parent=g3)

    colors = [
        [GREEN, RED],
        [PURPLE, ORANGE],
        [YELLOW, BLUE],
        [RED, WHITE],
        [BLUE, GREEN],
    ]
    scene = Scene()
    for gear in reversed([g4, g3, g2, g1]):
        gear.do()

    cycles = VGroup()
    for gear in reversed([g4, g3, g2, g1]):
        cycle = VGroup(stroke_width=0.2).set_color(color=colors.pop())
        locations = [(*value, 0) for (_, value) in sorted(gear.locations.items())]
        cycle.set_points_as_corners(locations)
        cycles.add(cycle)

    cycles.scale_to_fit_height(config.frame_height)
    scene.add(cycles)
    scene.render()
