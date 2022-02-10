
from polynomier import Q

class Gear:
    def __init__(self, ratio: Q, parent=None):
        self.ratio = ratio
        self.angle = Q(0, 1)
        self.children = []
        self.is_root = parent is None
        if not self.is_root:
            parent.children.append(self)

    def turn(self, amount: Q):
        my_amount = amount * self.ratio
        new_angle = self.angle + my_amount
        self.angle = new_angle
        for child in self.children:
            child.turn(my_amount)


if __name__ == "__main__":

    g0 = Gear(Q(1, 1))
    g1 = Gear(Q(2, 1), g0)
    g2 = Gear(Q(1, 2), g1)

    g0.turn(Q(1, 1))
    print(g0.children[0].children[0].angle)
