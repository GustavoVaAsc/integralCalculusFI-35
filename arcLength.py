import math
import matplotlib.pyplot as plt

def f(t):
    return t**(3/2)

def secant_length(a, b):
    delta_t = b - a
    delta_y = f(b) - f(a)
    return math.sqrt(delta_t**2 + delta_y**2)

t_start = float(input("Enter the starting value of t: "))
t_end = float(input("Enter the ending value of t: "))
num_sect = int(input("Enter the number of secant lines to use: "))

delta_t = (t_end - t_start) / num_sect

arc_length = 0
prev_t = t_start

t_values = []
y_values = []

for i in range(num_sect):
    t = t_start + i * delta_t
    y = f(t)
    t_values.append(t)
    y_values.append(y)
    arc_length += secant_length(prev_t, t)
    prev_t = t

plt.text(0.1, 0.9, "La aproximacion de la longitud de arco es: {:.2f}".format(arc_length), transform=plt.gca().transAxes)

secant_x = []
secant_y = []
for i in range(num_sect):
    t1 = t_start + i * delta_t
    y1 = f(t1)
    t2 = t_start + (i+1) * delta_t
    y2 = f(t2)
    secant_len = secant_length(t1, t2)
    secant_x.extend([t1, t2, None])  
    secant_y.extend([y1, y2, None])

t_plot = list(map(lambda t: t_start + t*(t_end-t_start)/1000, range(1001)))
y_plot = list(map(f, t_plot))

plt.plot(secant_x, secant_y, label='Rectas secantes', color='red')
plt.plot(t_plot, y_plot, label='x^3/2')
plt.title('Longitud de arco (Aproximada)')    
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
