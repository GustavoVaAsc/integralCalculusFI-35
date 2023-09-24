# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    return x**2

a = 0
b = 2

n_rectangles = 50
#int(input("Teclea el número de aproximaciones: "))

dx = (b - a) / n_rectangles

x = np.linspace(a, b, n_rectangles)
y = f(x)

fig, ax = plt.subplots()
ax.set_xlim([a, b])
ax.set_ylim([0, f(b)])
rects = ax.bar(x, y, dx, alpha=0.5)
curve, = ax.plot([], [], 'r-', linewidth=2)

def update(frame):
    for rect, yi in zip(rects, y):
        rect.set_height(yi * frame / n_rectangles)
    curve.set_data(x[:frame], y[:frame])
    return rects, curve

ani = animation.FuncAnimation(fig, update, frames=n_rectangles, interval=100, repeat=False)

plt.show()
