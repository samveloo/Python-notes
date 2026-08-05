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

count = 0
while (num := int(input())) >= 1 and num <= 5:
    count += 1 if num == 5 else 0
print(count)

while '_' in (nickname := input()):
    pass
print(nickname)

count = 0
while (person := input()) != 'Александра':
    pass
while (person := input()) != 'Левон':
    count += 1
print(count)

count = 0
n = int(input())
while n >= 25:
    n -= 25
    count += 1
while n >= 10:
    n -= 10
    count += 1 
while n >= 5:
    n -= 5
    count += 1
while n >= 1:
    n -= 1
    count += 1  
print(count)

num = 1576
has_seven = False                                 # сигнальная метка (флаг)
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')

num = 8619
n = len(str(num))
for i in range(1, n + 1):
    digit = num // 10 ** (n - i) % 10
    print(i, '-я', ' цифра равна ', digit, sep='')

num = 586
while num > 0:
    last_digit = num % 10
    print(last_digit, sep='*', end='#')
    num //= 10
    print()