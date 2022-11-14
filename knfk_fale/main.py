import math
import matplotlib.pyplot as plt
import numpy as np
import time

n: int = 80
c = 1
X = 10  # size of the membrane
delta_x = float(X) / 10
delta_t = delta_x / 1.5

matrix_previous = np.zeros([n, n])
matrix_current = np.zeros([n, n])
matrix_next = np.zeros([n, n])


# initial conditions
def f(x, y):  # u(0,x,y)
    if 0.1 < x < 0.2:
        return 1
    else:
        return 0
        # return math.sin(math.pi * x) * math.sin(math.pi * y)
    # return 0


# def g(x, y):  # du/dt(0, x, y)
#    return 0


def fill_initial_conditions():
    global matrix_next, matrix_current, matrix_previous
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            matrix_current[i, j] = f(i * delta_x, j * delta_x)
            matrix_previous[i, j] = f(i * delta_x, j * delta_x)


def calculate_next_matrix():
    global matrix_next, matrix_current, matrix_previous
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            matrix_next[i, j] = 2 * matrix_current[i, j] - matrix_previous[i, j] + c ** 2 * (
                    delta_t ** 2 / (delta_x ** 2)) * (
                                        matrix_current[i - 1, j] + matrix_current[i, j - 1] + matrix_current[
                                    i + 1, j] + matrix_current[i, j + 1] - 4 * matrix_current[i, j])
    return matrix_next


def main():
    global matrix_previous
    global matrix_next
    global matrix_current
    # fill_initial_conditions()
    # calculate_next_matrix()
    plt.ion()
    fig = plt.figure()
    img = plt.matshow(matrix_next, fignum=0, vmax=10, vmin=-10, cmap='PiYG')  # plasma tez fajna rozowiutka
    plt.show(block=False)

    for i in range(0, 10000000):
        t = i * delta_t
        matrix_current[40, 50] = 15 * math.cos(t)
        matrix_current[40, 25] = 15 * math.sin(t)
        calculate_next_matrix()
        img.set(data=matrix_current)
        matrix_previous = matrix_current
        matrix_current = matrix_next
        matrix_next = np.zeros([n, n])
        plt.pause(0.01)
        time.sleep(0.5)

#szczeliny ustawic komorki we wszystkich krokach na 0
main()
plt.imshow(matrix_current)
plt.show()