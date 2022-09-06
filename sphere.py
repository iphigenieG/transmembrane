from numpy import arange, pi, sin, cos, arccos
n = 50
goldenRatio = (1 + 5**0.5)/2
i = arange(0, n)
theta = 2 *pi * i / goldenRatio
phi = arccos(1 - 2*(i+0.5)/n)
x, y, z = cos(theta) * sin(phi), sin(theta) * sin(phi), cos(phi);