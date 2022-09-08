import math
import matplotlib.pyplot as plt


def fibonacci_sphere(samples=1000):

    xs = []
    ys = []
    zs = []
    phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians

    for i in range(samples):

        y = 1 - (i / float(samples - 1)) # y goes from 1 to 0

        radius = math.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        xs.append(x)
        ys.append(y)
        zs.append(z)

    return xs,ys,zs

xs,ys,zs = fibonacci_sphere()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

xs.append(0)
ys.append(-1)
zs.append(0)

ax.scatter(xs, ys, zs)

plt.show()