n = 5

#print(type(n))
# print(dklj)
'''
print(1)

print(16437)
print(iuhjy)
'''

print(9.8)
print(9)

a = 5
b = 6.90
c = 'hello'
print(a, b, c)
print(a, '-', b, '-', c)
print(f"{a} - {b} - {c}")
print("{} - {} - {}".format(a, b, c))

#ввод даанных
'''
print('enter number')
a = input()

b = input('enter second number') #это сообщение никуда не сохраняется
print(a, '+', b, '=', a + b)
'''
'''
c = 5.89
print(c)
#n = int(c)
c = int(c)
print(c) 
print(type(c))
'''
'''
print('enter number')
a = int(input())

b = int(input('enter second number')) #введенное число будет целочисленным числом
print(a, '+', b, '=', a + b)
'''
a = 5.9857
b = 6.96574
print(round(a*b, 3))
# округление

#сокращенное присваивание
iter = 2
iter += 3 #  iter =  iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5 число с остатком
iter //= 5 # iter = iter // 5 целочисленное деление
iter %= 5 # iter = iter % 5 остаток от деления
iter **= 5 # iter = iter ** 5 степень 5 
'''
#циклы
username = input('Enter your name:')
if username == 'Маша':
    print('Ура, это Маша!!!')
elif username == 'Марина':
    print('Я так тебя ждал, Марина!')
elif username == 'Аня':
    print('Аня - супер - пупер - топчик!!!')
else:
    print('Тебя сюда никто не звал, КЫШ,', username, '!!!')
'''
#метод флажка
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: #если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числане может превышать введенное число, деленое на 2
        print(n)
        flag = False
    i += 1