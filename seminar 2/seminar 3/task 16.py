#  Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число Xfrom random import randrange

from random import randrange

N = int(input())
A = [
    randrange(10) for i in range(N)
    ]
X = int(input())
print(A)
print(A.count(X))