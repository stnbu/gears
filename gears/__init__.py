from math import tau, sin, cos
from polynomier import Q
from sympy import Matrix

# FIXME s/angle/rotations/g
# MAYBE import tau as circle

class Gear:
    def __init__(self, ratio, parent=None, name=None):
        if not isinstance(ratio, Q):
            ratio = Q(ratio, 1)
        self.ratio = ratio
        self.name = name
        #self.rotation = Q(0, 1)
        self.parent = parent
        self.children = []
        if not self.is_root():
            parent.children.append(self)

    # def turn(self, amount):
    #     if not isinstance(amount, Q):
    #         amount = Q(amount, 1)
    #     my_amount = amount * self.ratio
    #     new_rotation = self.rotation + my_amount
    #     self.rotation = new_rotation
    #     for child in self.children:
    #         child.turn(my_amount)

    def is_root(self):
        return self.parent is None

    def get_root(self):
        current = self
        while not current.is_root():
            current = current.parent
        return current

    def degree(self):
        return len(self.children) + 1

    def get_output_rotation(self, input_rotation):
        rotation = input_rotation
        for gear in self.get_lineage():
            rotation = gear.ratio * rotation
        return rotation

    def get_lineage(self):
        ancestry = [self]
        while ancestry[-1].parent is not None:
            ancestry.append(ancestry[-1].parent)
        return reversed(ancestry)

    def get_leafs(self):
        leafs = []
        for child in self.children:
            leafs.extend(child.get_leafs())
            if child.degree() == 1:
                leafs.append(child)
        return leafs

    def __repr__(self):
        if self.name is not None:
            return self.name
        return "<%s %s>" % (self.__class__.__name__, id(self))


class DrawingGear(Gear):

    def __init__(self, *args, arm=None, nib=None, **kwargs):
        super().__init__(*args, *kwargs)
        self.arm = Q(1, 1) if arm is None else arm
        self.nib = nib

    def get_nib(self, input_rotation):
        x, y = 0.0, 0.0
        #net_rotation = Q(0, 1)
        for gear in self.get_lineage():
            (x, y), input_rotation = gear.react((x, y), input_rotation)
        return x, y

    def react(self, origin, input_rotation):
        import ipdb; ipdb.set_trace()
        dx, dy = origin
        x, y = dx, float(self.arm) + dy
        n, d = self.get_output_rotation(input_rotation)
        angle = tau * (n / d)
        r = Matrix(
            [
                [cos(angle), -sin(angle)],
                [sin(angle),  cos(angle)],
            ]
        )
        x, y = r * Matrix([x, y])
        #import ipdb; ipdb.set_trace()
        return (x, y), input_rotation


if __name__ == "__main__":
    dgg = DrawingGear(1)
    dhh = DrawingGear(1, dgg)
    input_rotation = Q(1, 8)
    x, y = dhh.get_nib(input_rotation)
    print(new_frame)

    dhh = DrawingGear(1, None)
    import ipdb; ipdb.set_trace()
    new_frame = dhh.get_nib_frame(*new_frame)
    
    #
    #dgg.turn(Q(1, 8))
    #input_rotation = Q(1, 8)
    #print(dhh.get_nib_xy(input_rotation))

