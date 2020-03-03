from numpy import float32

val = float32(0.53125)
sum = float32(0)
numbers = [val] * 10 ** 7
sum2 = 0


def Kahan_sum (tab, sum, err):
    for i in tab:
        y = i - err
        tmp = sum + y
        err = (tmp - sum) - y
        sum = tmp
    return sum


print(Kahan_sum(numbers, float32(0.0), float32(0.0)))
