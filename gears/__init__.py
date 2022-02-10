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
