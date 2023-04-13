# Задача 10.
'''
import random
coints = int(input('введите количество монет: ')) 

count = 0
count_1 = 0
count_0 = 0
nominal = 0

for i in range(coints):
    nominal = random.randint(0,1)
    print(nominal, end=" ")
    if nominal > 0:
        count_1 +=1
        count +=1
    else:
        count_0 += 1
        count +=1
    
if count_1 > count_0:
    print(f'\nпереверните {count_0}')
else:
    print(f'\nпереверните {count_1} монет')
'''
# Задача 12.

x = abs(int(input('Введите первое натуральное число X от 1 до 1000 ')))
y = abs(int(input('Введите второе натуральное число Y от 1 до 1000 ')))
if x < 1 or x > 1000 or y < 1 or y > 1000:
    print('Вы ввели число не из заданного диапазона!')
else:
    S = x + y
    P = x * y
    stop = 0
    for i in range(1001):
        if stop != 1:
            for j in range(1001):
                if stop != 1:
                    if i * j == P and i + j == S:
                        print(i, j)
                        stop = 1
            else:
                j = 1001
        else:
            i = 1001


# Задача 14.
n = int(input('Введите число N '))
stop = 0
k = 2
for i in range(n):
    if stop != 1:
        k = k ** i
        if k <= n:
            print(k, end=' ')
            k = 2
        else:
            stop = 1
    else:
        i = n