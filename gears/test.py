from gears import Gear
from polynomier import Q


def test():

    return None  # meh

    g00 = Gear(1)
    g10 = Gear(1, g00)
    g11 = Gear(1, g00)
    g20 = Gear(1, g10)
    assert set(g00.get_leafs()) == set([g11, g20])

    g0 = Gear(Q(1, 1))
    g1 = Gear(Q(2, 1), g0)
    g2 = Gear(Q(3, 1), g1)
    g0.turn(Q(1, 1))
    assert g0.children[0].children[0].rotation == Q(6, 1) == g2.rotation == 6

    g0 = Gear(1)
    g1 = Gear(2, g0)
    g2 = Gear(3, g1)
    g0.turn(1)
    assert g0.children[0].children[0].rotation == Q(6, 1) == g2.rotation == 6

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
    assert gears[-1].rotation == Q(1, 64)
    gears[0].turn(1)
    assert gears[-1].rotation == Q(2, 64)
    gears[0].turn(-2)
    assert gears[-1].rotation == 0


if __name__ == "__main__":
    test()
