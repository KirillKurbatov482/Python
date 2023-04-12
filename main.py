# print('Введите первую строку')
# a = input ()
# print (a)

# i = int(input ())
# j = int(input ())
# if i==j:
#     print('не хватает данных')
# else:
#     print(j+i-1)

a = input('Введите трехзначное число: ')
a = int(a)
b = a % 10
a = a // 10
c = a % 10
a = a // 10
print('Сумма цифр: ', a+b+c)

