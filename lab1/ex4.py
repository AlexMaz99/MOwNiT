from numpy import float32
from numpy import float64
from numpy import arange
from matplotlib import pyplot as plt

N = 1000


def x_N(x_0, r, function):
    tab = [function(x_0)]
    r = function(r)
    for i in range(0, N):
        tab.append(function(r * tab[i] * (1 - tab[i])))
    return tab


def a(how_many):

    for x_0 in arange(0.1, 1, 0.1):
        for r in arange(1, 4, 0.01):
            tab = x_N(x_0, r, float32)
            for i in (N - how_many, N):
                plt.plot(r, tab[i], '.', markersize=2)

    plt.show()


def b():
    R = []
    for r in arange(3.75, 3.8, 0.0001):
        R.append(r)
    for x_0 in arange(0.1, 1, 0.1):
        xN32 = []
        xN64 = []
        for r in R:
            xN32.append(x_N(x_0, r, float32)[N - 1])
            xN64.append(x_N(x_0, r, float64)[N - 1])
        plt.subplot(1, 2, 1)
        plt.plot(R, xN32, '.', markersize=2)
        plt.subplot(1, 2, 2)
        plt.plot(R, xN64, '.', markersize=2)
    plt.show()


def c():
    r = float32(4)
    eps = 1e-4

    iterations = []
    for x_0 in arange(0.01, 1, 0.01):
        tab = [float32(x_0)]
        i = 0
        while tab[i] > eps and i < N:
            tab.append(r * tab[i] * (1 - tab[i]))
            i = i + 1
        iterations.append(i)
    plt.plot(arange(0.01, 1, 0.01), iterations, '.', markersize=2)
    plt.show()


# a(5)
# b()
c()
