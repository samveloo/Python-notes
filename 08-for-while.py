from tracemalloc import stop


for i in range(10):
    print('Hello')

""" for название_переменной_цикла in range(количество_повторений):
    блок кода 
"""

for i in range(5):
    num = int(input())
    print('Квадрат вашего числа равен:', num * num)

print('Цикл завершен')

for i in range(4):
    j = i + 1
    print(i, j)

total = 0
for i in range(3):
    total = total - i
    print(total)

n = int(input())
for i in range(n + 1):
    print(f'Квадрат числа {i} равен {i**2}')

n = int(input())

for i in range(n):
    print('*' * n)
    n = n - 1

m, p, n = int(input()), int(input()), int(input())

for i in range(n):
    print(i + 1, m)
    m = m * (1 + p / 100)

# range(start, stop, step)

# параметр start – это старт последовательности (включительно)
# параметр stop – это стоп последовательности (не включительно)
# параметр step – это величина шага

prod = 1
for i in range(-7, -3, 1):
    if i < -5:
        prod = prod * i

print(prod)

total_len = 0
for _ in range(3):
    word = input()
    total_len = total_len + len(word)
print(total_len)

num = int(input())
flag = True
for i in range(2, num):
    if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
if num == 1:
    print('Это единица, она не простая и не составная') 
elif flag == True:
    print('Число простое')
else:
    print('Число составное')