"""
Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: a
A(n) = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15

"""

a1 = int(input('Первое число: '))
d = int(input('Разность: '))
n = int(input('Кол-во элементов: '))

lst = []
k = a1

for i in range(n):
    lst.append(k)
    k = k + d

print(lst)
