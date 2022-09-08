from numpy import arange, pi, sin, cos, arccos
n = 50
goldenRatio = (1 + 5**0.5)/2
i = arange(0, n)
theta = 2 *pi * i / goldenRatio
phi = arccos(1 - 2*(i+0.5)/n)
x, y, z = cos(theta) * sin(phi), sin(theta) * sin(phi), cos(phi);


"""
autre option (à comprendre et modifier)
import math


def fibonacci_sphere(samples=1000):

    points = []
    phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians

    for i in (samples / 2, samples):
        y = ((i * offset) - 1) + (offset / 2) # y goes from 1 to -1

        y = 1 - (i / float(samples - 1)) * 2

        radius = math.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        points.append((x, y, z))

    return points
"""