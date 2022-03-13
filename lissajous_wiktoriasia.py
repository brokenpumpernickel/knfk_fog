from turtle import color
import numpy as np
from numpy import sin, pi, linspace
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

a = 3
b = 5
d = 7

delta = pi/d

t = linspace(-pi,pi,1000)

x = sin(a * t + delta)
y = sin(b * t)


fig, ax = plt.subplots()
fig.suptitle('Krzywa Lissajous twoich marzeń', fontsize=12)

line = plt.plot(x, y, color='pink')


plt.subplots_adjust( bottom=0.43)


axfreq = plt.axes([0.18, 0.3, 0.65, 0.03])
a_slider = Slider(
    ax=axfreq,
    label='wartość a',
    valmin=1,
    valmax=20,
    valinit=a,
    valstep=1.0
)

bxfreq = plt.axes([0.18, 0.2, 0.65, 0.03])
b_slider = Slider(
    ax=bxfreq,
    label='wartość b',
    valmin=1,
    valmax=10,
    valinit=b,
    valstep=1.0
)

dxfreq = plt.axes([0.18, 0.1, 0.65, 0.03])
d_slider = Slider(
    ax=dxfreq,
    label='wartość d',
    valmin=1,
    valmax=20,
    valinit=d,
    valstep=1.0
)


def update(val):
    delta = pi/d_slider.val

    line[0].set_xdata(sin(a_slider.val * t + delta))
    line[0].set_ydata(sin(b_slider.val * t))

    fig.canvas.draw_idle()


a_slider.on_changed(update)
b_slider.on_changed(update)
d_slider.on_changed(update)


plt.show()
