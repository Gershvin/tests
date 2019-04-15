import unittest
import numpy as np

def func_1(a):
    z = []
    pows = []
    for i in range(len(a)):
        z.append(tuple(a[i].split()))
    print('Ваш кортеж из кортежей до преобразования выглядит так', z)
    for i in range(len(z)):
        for j in range(len(z[i])):
            e = (int(z[i][j]), pow(int(z[i][j]), int(z[i][j])))
            pows.append(e)
    return pows

def func_2(a):
    del_repeat = [a[0][1]]
    for i in range(1, len(a)):
        if a[i][1] != a[i-1][1]:
            del_repeat.append(a[i][1])
    return del_repeat

answer_1= func_1(tuple(i for i in input('Введите данные. Кортежи отделяйте запятыми, а элементы кортежей - пробелами ').split(',')))
answer_2 = func_2(answer_1)
print('Результат функции func_1:', answer_1)
print('Результат функции func_2:', answer_2)

