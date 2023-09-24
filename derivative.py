import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x):
    return x**2

def dfdx(x, h):
    return (f(x+h) - f(x))/h

h = 0.1
x_start = -3
x_end = 3
num_frames = 50

fig, ax = plt.subplots()

x = np.linspace(x_start, x_end, 100)
ax.plot(x, f(x), label='f(x)')

tangent_x = np.linspace(x_start, x_end, 3)
tangent_y = f(tangent_x)
tangent_line, = ax.plot(tangent_x, tangent_y, 'r--', label='Recta tangente')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Derivada de x^2')
ax.legend()

def update(frame):
    x0 = x_start + frame*(x_end - x_start)/num_frames
    tangent_x = np.linspace(x0-h, x0+h, 3)
    tangent_y = f(x0) + dfdx(x0, h)*(tangent_x - x0)
    tangent_line.set_data(tangent_x, tangent_y)
    return tangent_line,

ani = FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

plt.show()
