import math
from penrose import PenroseP3, BtileL, psi


scale = 1000
tiling = PenroseP3(scale, ngen=3)

theta = 4*math.pi / 5
rot = math.cos(theta) + 1j*math.sin(theta)
A = -scale/6 + 0j
B = scale/6 * rot
C = scale/6 / psi + 0j
tiling.set_initial_tiles([BtileL(A, B, C)])
tiling.make_tiling()

tiling.write_svg('example1.svg')