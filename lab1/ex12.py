from numpy import float32
from matplotlib import pyplot as plt
import time

val = float32(0.53125)
numbers = [val] * 10 ** 7


def absolute_error(number, approximation):
    return abs(number - approximation)


def relative_error(number, approximation):
    return abs(number - approximation) / number


def iterative_sum(tab):
    sum = float32(0)
    for i in tab:
        sum += i
    return sum


def recursive_sum(xs):
    length = len(xs)
    if length == 0:
        return 0
    if length == 1:
        return xs[0]
    else:
        return recursive_sum(xs[:length//2]) + recursive_sum(xs[length//2:])


def relative_error_plot(numbers):
    sum = float32(0)
    sum2 = 0
    x = 0
    tab = []
    for i in numbers:
        sum += i
        sum2 += i
        if x % 25000 == 0:
            tab.append(relative_error(sum2, sum) * 100)
        x += 1
    plt.plot(tab)
    plt.show()


def compare_time_iterative_recursive():
    start = time.time() * 1000
    iterative_sum(numbers)
    end = time.time() * 1000
    time_sum1 = (end - start).__round__(2)
    print(f"Czas dla sumy obliczonej iteracyjnie: {time_sum1} milisekund")
    start = time.time() * 1000
    recursive_sum(numbers)
    end = time.time() * 1000
    time_recursive_sum = (end - start).__round__(2)
    print(f"Czas dla sumy obliczonej rekurencyjnie: {time_recursive_sum} milisekund")


def not_zero_error():
    x = float32(0.0001)
    y = float32(10000)
    numbers2 = []
    sum64 = float(0)
    for i in range(10 ** 7 + 1):
        if i % 2 == 0:
            numbers2.append(x)
            sum64 += x
        else:
            numbers2.append(y)
            sum64 += y
    sum3 = recursive_sum(numbers2)
    return relative_error(sum64, sum3) * 100


def Kahan_sum (tab, function):
    sum = function(0.0)
    err = function(0.0)
    for i in tab:
        y = function(i - err)
        tmp = function(sum + y)
        err = function((tmp - sum) - y)
        sum = tmp
    return sum
# (tmp - sum) odzyskuje wyższe bity y; odjęcie y odzyskuje niższe bity y; zatem err zawiera utracone niskie bity


def compare_time_kahan_recursive():
    start = time.time() * 1000
    Kahan_sum(numbers, float32)
    end = time.time() * 1000
    time_sum1 = (end - start).__round__(2)
    print(f"Czas dla sumy obliczonej algorytmem Kahana: {time_sum1} milisekund")
    start = time.time() * 1000
    recursive_sum(numbers)
    end = time.time() * 1000
    time_recursive_sum = (end - start).__round__(2)
    print(f"Czas dla sumy obliczonej rekurencyjnie: {time_recursive_sum} milisekund")


sum32 = iterative_sum(numbers)
original_sum = val * 10 ** 7

print('Wartość dla 32 bitów:', sum32)
print('Wartość dla 64 bitów: ', original_sum)

print('Błąd bezwzględny:', absolute_error(original_sum, sum32))
print('Błąd względny:', relative_error(original_sum, sum32) * 100, '%')
# Błąd względny jest spowodowany dodawaniem bardzo małej liczby do coraz większej sumy.


sum3 = recursive_sum(numbers)
print('Suma obliczona rekurencyjnie: ', sum3)
print('Błąd bezwzględny: ', absolute_error(original_sum, sum3))
print('Błąd względny: ', relative_error(original_sum, sum3) * 100, '%')
#Błąd względny jest równy 0, ponieważ rekurencyjnie dodajemy do siebie bardzo podobne liczby.
#Bity mantysy nie są tracone.

relative_error_plot(numbers)
compare_time_iterative_recursive()
print('Niezerowy błąd: ', not_zero_error(), '%')
#Jeżeli w tablicy będą obok siebie liczby bardzo duże i bardzo małe to błąd wzrośnie.

kahan_sum = Kahan_sum(numbers, float32)
original_sum = val * 10 ** 7
print('Błąd bezwzględny: ', absolute_error(original_sum, kahan_sum))
print('Błąd względny: ', relative_error(original_sum, kahan_sum) * 100, '%')

compare_time_kahan_recursive()
