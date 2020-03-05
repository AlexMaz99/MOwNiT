from numpy import float32
from matplotlib import pyplot as plt

tab_s = [float32(2), float32(3.6667), float32(5), float32(7.2), float32(10)]
tab_n = [50, 100, 200, 500, 1000]


def relative_error(number, approximation):
    return abs(number - approximation) / number


def dzeta_riemann_forward(s, n, function):
    sum = function(0)
    for k in range(1, n + 1, 1):
        sum += function(1 / (k ** s))
    return sum


def dzeta_riemann_backward(s, n, function):
    backward_sum = function(0)
    for k in range(n, 0, -1):
        backward_sum += function(1 / (k ** s))
    return backward_sum


def eta_dirichlet_forward(s, n, function):
    sum = function(0)
    for k in range(1, n + 1, 1):
        sum += function((-1) ** (k - 1) * 1 / (k ** s))
    return sum


def eta_dirichlet_backward(s, n, function):
    backward_sum = function(0)
    for k in range(n, 0, -1):
        backward_sum += function((-1) ** (k - 1) * 1 / (k ** s))
    return backward_sum


def compare_precision(tab_n, tab_s):
    for s in tab_s:
        for n in tab_n:
            riemann_sum32_f = dzeta_riemann_forward(s, n, float32)
            riemann_sum32_b = dzeta_riemann_backward(s, n, float32)
            riemann_sum64_f = dzeta_riemann_forward(s, n, float)
            riemann_sum64_b = dzeta_riemann_backward(s, n, float)
            dirichlet_sum32_f = eta_dirichlet_forward(s, n, float32)
            dirichlet_sum32_b = eta_dirichlet_backward(s, n, float32)
            dirichlet_sum64_f = eta_dirichlet_forward(s, n, float)
            dirichlet_sum64_b = eta_dirichlet_backward(s, n, float)

            print("s: ", s, "n: ", n)
            print("Riemann dla float32")
            print("Suma normalna: ", riemann_sum32_f)
            print("Suma obliczona wstecz: ", riemann_sum32_b)
            print("Różnica między powyższymi: ", abs(riemann_sum32_b - riemann_sum32_f))
            print("\n")
            print("Riemann dla float64")
            print("Suma normalna: ", riemann_sum64_f)
            print("Suma obliczona wstecz: ", riemann_sum64_b)
            print("Różnica między powyższymi: ", abs(riemann_sum64_b - riemann_sum64_f))
            print("\n")
            print("Dirichlet dla float32")
            print("Suma normalna: ", dirichlet_sum32_f)
            print("Suma obliczona wstecz: ", dirichlet_sum32_b)
            print("Różnica między powyższymi: ", abs(dirichlet_sum32_b - dirichlet_sum32_f))
            print("\n")
            print("Dirichlet dla float64")
            print("Suma normalna: ", dirichlet_sum64_f)
            print("Suma obliczona wstecz: ", dirichlet_sum64_b)
            print("Różnica między powyższymi: ", abs(dirichlet_sum64_b - dirichlet_sum64_f))
            print("\n")
            print("-----------------------------------------")


def riemann_plot(s, n, function):
    sum = function(0)
    tab1 = []
    tab2 = []
    for k in range(1, n + 1):
        sum += function(1 / (k ** s))
        x = 1 / (k ** s)
        y = 1 / ((k + 1) ** s)
        z = 1 / ((k + 2) ** s)
        tab1.append(relative_error(x + y + z, function(function(x + y) + z)))
        tab2.append(relative_error(x + y + z, function(x + function(y + z))))
    plt.plot(tab1)
    plt.show()
    plt.plot(tab2)
    plt.show()


def dirichlet_plot(s, n, function):
    sum = function(0)
    tab1 = []
    tab2 = []
    for k in range(1, n + 1):
        sum += function((-1) ** (k - 1) * 1 / (k ** s))
        x = (-1) ** (k - 1) * 1 / (k ** s)
        y = (-1) ** k * 1 / ((k + 1) ** s)
        z = (-1) ** (k + 1) * 1 / ((k + 2) ** s)
        tab1.append(relative_error(x + y + z, function(function(x + y) + z)))
        tab2.append(relative_error(x + y + z, function(x + function(y + z))))
    plt.plot(tab1)
    plt.show()
    plt.plot(tab2)
    plt.show()


compare_precision(tab_n, tab_s)
riemann_plot(2, 50, float32)
dirichlet_plot(2, 50, float32)
