from numpy import float32
from matplotlib import pyplot as plt

val = float32(0.53125)
sum = float32(0)
numbers = [val] * 10 ** 7
sum2 = 0
tab = []
x = 0

for i in numbers:
    sum += i
    sum2 += i
    if x % 25000 == 0:
        tab.append(abs((sum2 - sum) / sum2) * 100)
    x += 1
print('Wartość dla 32 bitów:', sum)
print('Wartość dla 64 bitów: ', sum2)

print('Błąd bezwzględny:', abs(sum2 - sum))
print('Błąd względny:', (abs(sum2 - sum) / sum2) * 100, '%')

plt.plot(tab)
plt.show()


def recursive_sum(xs):
    length = len(xs)
    if length == 0:
        return 0
    if length == 1:
        return xs[0]
    else:
        return recursive_sum(xs[:length//2]) + recursive_sum(xs[length//2:])


sum3 = recursive_sum(numbers)
print('Suma obliczona rekurencyjnie: ', sum3)
print('Błąd bezwzględny: ', abs(sum3 - sum2))
print('Błąd względny: ', (abs(sum3 - sum2) / sum2) * 100, '%')

#Czas wykonania pierwszego algorytmu: 1.527
#Czas wykonania drugiego algorytmu (rekurencyjnego):17.678
