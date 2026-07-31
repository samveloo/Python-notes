""" while условие:
    блок кода """

i = 0
while i < 10:
    print('Привет')
    i += 1

num = int(input())
while num != -1:
    print('Квадрат вашего числа равен:', num * num)
    num = int(input())

# используем for
for i in range(101):
    print(i)

# используем while
i = 0
while i < 101:
    print(i)
    i += 1

# используем for
for i in range(0, 100, 3):
    print(i)

# используем while
i = 0
while i < 100:
    print(i)
    i += 3

text = input()
total = 0
while text != 'stop':
    total += int(text)
    text = input()

print('Сумма чисел равна', total)

i = -1
while i > 0:
    print('Hello world!')

name = input()
while name != 'Валера' and name != 'Артур':
    print('Доступ запрещен')
    name = input()

counter = 0
str = input()
while str not in ('стоп', 'хватит', 'достаточно'):
    counter += 1
    str = input()
print(counter)

str = input()
while str != 'КОНЕЦ' and str != 'конец':
    print(str)
    str = input()

n = int(input())
while not n % 7:
    print(n)
    n = int(input())

