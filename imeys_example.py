# first attempt at making black and white penrose
import math
from penrose import PenroseP3, BtileL, psi

scale = 100
config = {'tile-opacity': 1, 'stroke-colour': '#000', 'Ltile-colour': '#FFF',
          'Stile-colour': '#FFF', 'base-stroke-width': 0.1}

tiling = PenroseP3(scale, ngen=10, config= config)

#ngen set to 4, scale set to 200


theta = 2*math.pi / 5

rot = math.cos(theta) + 1j*math.sin(theta)
A = -scale/2 + 0j
B = scale/2 * rot
C = scale/2 / psi + 0j

tiling.set_initial_tiles([BtileL(A, B, C)])
tiling.make_tiling()

tiling.write_svg('imey1.svg')
