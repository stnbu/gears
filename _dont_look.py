

import svgwrite
from gears import Gear

g0 = Gear()
g1 = Gear(parent=g0, arm=1.3)
g2 = Gear(ratio=0.5, parent=g1)
g3 = Gear(ratio=-1.5, parent=g2)
g4 = Gear(ratio=1.1, parent=g3)

gears = [g0, g1, g2, g3, g4]
for gear in gears:
    gear.do()


def get_bounds(*lines):
    max_x = float('-inf')
    min_x = float('inf')
    max_y = float('-inf')
    min_y = float('inf')
    for points in lines:
        max_x = max(max([x for (x, _) in points]), max_x)
        min_x = min(min([x for (x, _) in points]), min_x)
        max_y = max(max([y for (_, y) in points]), max_y)
        min_y = min(min([y for (_, y) in points]), min_y)
    return max_x, min_x, max_y, min_y


style = "position: absolute; width: 100%; height: 100%;"
frame = svgwrite.Drawing("foo.svg", style=style, debug=False)

max_x, min_x, max_y, min_y = get_bounds(g4.locations.values())

line = [(point[0] - min_x, point[1] - min_y) for (_, point) in sorted(g4.locations.items())]

#import ipdb; ipdb.set_trace()
frame.viewbox(0, 0, max_x - min_x, max_y - min_y)

poly = frame.polyline(line, fill="none", stroke="black", stroke_width="0.1%")
frame.add(poly)

frame.save()
