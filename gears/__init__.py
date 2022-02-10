from polynomier import Q


class Gear:
    def __init__(self, ratio, parent=None, name=None):
        if not isinstance(ratio, Q):
            ratio = Q(ratio, 1)
        self.ratio = ratio
        self.name = name
        self.angle = Q(0, 1)
        self.parent = parent
        self.children = []
        if not self.is_root():
            parent.children.append(self)

    def turn(self, amount):
        if not isinstance(amount, Q):
            amount = Q(amount, 1)
        my_amount = amount * self.ratio
        new_angle = self.angle + my_amount
        self.angle = new_angle
        for child in self.children:
            child.turn(my_amount)

    def is_root(self):
        return self.parent is None

    def get_root(self):
        current = self
        while not current.is_root():
            current = current.parent
        return current

    def degree(self):
        return len(self.children) + 1

    def get_leafs(self):
        leafs = []
        # if self.degree() == 1:
        #     leafs.append(self)
        for child in self.children:
            leafs.extend(child.get_leafs())
            if child.degree() == 1:
                leafs.append(child)
        return leafs

    def __repr__(self):
        if self.name is not None:
            return self.name
        return "<%s %s>" % (self.__class__.__name__, id(self))


if __name__ == "__main__":

    g00 = Gear(1)
    g10 = Gear(1, g00)
    g11 = Gear(1, g00)
    g20 = Gear(1, g10)
    assert set(g00.get_leafs()) == set([g11, g20])

    g0 = Gear(Q(1, 1))
    g1 = Gear(Q(2, 1), g0)
    g2 = Gear(Q(3, 1), g1)
    g0.turn(Q(1, 1))
    assert g0.children[0].children[0].angle == Q(6, 1) == g2.angle == 6

    g0 = Gear(1)
    g1 = Gear(2, g0)
    g2 = Gear(3, g1)
    g0.turn(1)
    assert g0.children[0].children[0].angle == Q(6, 1) == g2.angle == 6

    ratio_sequence = [
        Q(1, 1),
        Q(1, 2),
        Q(1, 2),
        Q(1, 2),
        Q(1, 2),
        Q(1, 2),
        Q(1, 2),
    ]
    gears = []
    parent = None
    for ratio in ratio_sequence:
        g = Gear(ratio, parent)
        gears.append(g)
        parent = g
    assert len(set([g.get_root() for g in gears])) == 1
    gears[0].turn(1)
    print(gears[-1].angle)
