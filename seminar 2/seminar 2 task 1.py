# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


n = int(input("Введите кол-во монет: "))
k = 0
for i in range(n):
    v = int(input("Введите 1 - для монет лежащих гербом вверх, 0 - для монет лежащих решкой вверх "))
    if v == 1:
        k += 1
print(k if k<n/2 else n-k)

