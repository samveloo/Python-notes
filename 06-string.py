s1 = 'abcdef'
length1 = len(s1)                 # считаем длину строки из переменной s1
length2 = len('Python rocks!')    # считаем длину строкового литерала
print(length1)
print(length2)

num1 = 1777                       # целое число
num2 = 17.77                      # число с плавающей точкой
s1 = str(num1)                    # преобразовали целое число в строку '1777'
s2 = str(num2)                    # преобразовали число с плавающей точкой в строку '17.77'

print('a', 'b', 'c', sep='*', end='!')
print()  # переход на новую строку
print('a' + '*' + 'b' + '*' + 'c' + '!')

s = 'Hi' * 4
print(s)

print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

LName = input()
SName = input()
print(f"Hello {LName} {SName}! You have just delved into Python")

city1, city2, city3 = input(), input(), input()
len1 = len(city1)
len2 = len(city2)
len3 = len(city3)

if len1 < len2 and len1 < len3:
    print(city1)
else:
    if len2 < len1 and len2 < len3:
        print(city2)
    else:
        if len3 < len1 and len3 < len2:
            print(city3)
            
if len1 > len2 and len1 > len3:
    print(city1)
else:
    if len2 > len1 and len2 > len3:
        print(city2)
    else:
        if len3 > len1 and len3 > len2:
            print(city3)

s = 'https://example.com/'
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')

s = input()
if '.' not in s:
    print('Введенная строка не содержит символа точки')

if len(s) == 1 and s in 'aeiou':
    print('YES')

s = 'Sigma'
print('a' in s)
print('z' in s)

print('ab' in 'abc')
print('ac' in 'abc')

s1 = 'Зеландия'
s2 = 'Новая Зеландия'
if s1 in s2:
    print('Строка', s1, 'является подстрокой для строки', s2)
else:
    print('Строка', s1, 'не является подстрокой для строки', s2)