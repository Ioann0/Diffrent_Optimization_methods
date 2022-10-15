#coding: utf-8

def fibonacci_search(a, b):
    eps = 10 ** (-3)
    f0, f1 = 1, 1
    f = [f0, f1]
    n = 0
    while ((b - a) / eps) > f[-1]:
        f.append(f[-1]+f[-2])
        n += 1

    x1, x3 = a, b
    x2 = a + ((b - a) * f[-2] + eps * (-1)**n)/f[-1]

    def calc(x):
        a = 13.184763
        b = -0.50678149
        c = -5.9476583
        d = 0.10540214
        e = 0.85730668
        f = -0.0093862876
        g = -0.038289277
        h = 0.00029660947
        z = (a + c * x + e * (x ** 2) + g * (x ** 3))/(1 + (b * x) + d * (x ** 2) + f * (x ** 3) + h * (x ** 4))
        return z

    f2 = calc(x2)
    print(f'Текущий интервал: ({x1, x3})')
    k = 1
    while k > eps:
        x4 = x1 - x2 + x3
        f4 = calc(x4)
        if f4 > f2:
            if x2 < x4:
                x3 = x4
                print(x1, x3)
            else:
                x1 = x4
                print(x1, x3)
        elif x2 < x4:
            x1, x2, f2 = x2, x4, f4
            print(x1, x3)
        else:
            x3, x2, f2 = x2, x4, f4
            print(x1, x3)
        k = x3-x1

    print(f'Конечный интервал ({x1, x3})')
    print(f'Значение функции: {f2}')


if __name__ == '__main__':
    fibonacci_search(float(input('Введите начало интервала: ')), float(input('Введите конец интервала: ')))
