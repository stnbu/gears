# Gears! (compare to *Spirograph*&trade;)

## What does it do?

What *doesn't* it do?

## Install? Use?

Sure!

```
pip install https://github.com/stnbu/gears.git
```

```python
    from gears import Gear
    from manim import *
    from sympy import Matrix
    import math

    def ratio_01(origin, angle):
        return math.sqrt(origin[0]**2 + origin[1]**2)

    def arm_01(origin, angle):
        return 10 / math.sqrt(origin[0]**2 + origin[1]**2)

    g0 = Gear()
    g1 = Gear(parent=g0)
    g2 = Gear(ratio=0.5, parent=g1)
    g3 = Gear(ratio=-1.5, arm=arm_01, parent=g2)
    g4 = Gear(ratio=1.1, parent=g3)

    gears = [g0, g1, g2, g3, g4]

    colors = [
        [BLACK, WHITE],
        [PURPLE, ORANGE],
        [YELLOW, ORANGE],
        [WHITE, BLACK],
        [BLUE, GREEN],
    ]
    scene = Scene()
    for gear in gears:
        gear.do()

    cycle_locations = {}
    for i, gear in enumerate(gears):
        cycle_locations[i] = [
            (*value, 0) for (_, value) in sorted(gear.locations.items())
        ][1:]

    cycles = VGroup()
    for locations in cycle_locations.values():
        cycle = VGroup(stroke_width=0.2).set_color(color=colors.pop())
        cycle.set_points_as_corners(locations)
        cycles.add(cycle)

    cycles.scale_to_fit_height(config.frame_height * 0.9)
    scene.add(cycles)
    scene.render()
```

## Why?

Why not?

## Motivating Image?

Yes, but just one:

![Spirochaete](blob/main/wow.jpg?raw=true)
