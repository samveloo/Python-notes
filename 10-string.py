s1 = 'Python'
s2 = "Pascal"

s = input()  # считали текст
num = int(input())  # считали текст и преобразовали его в целое число

s = 'Hello'
n = len(s)  # значение переменной равно 5
print(n)

s = 'All you need is programming'
if 'programming' in s:
    print('❤️')
else:
    print('💔')

s = 'abcdef'
for i in range(len(s)):
    print(s[i])

s = 'abcdef'
for c in s:
    print(c)

s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')

s = input()
total = 0

for i in range(len(s)):
    total += int(s[i])
print(total)

s = input()
for i in range(len(s)):
    if s[i] in '0123456789':
        print('Цифра')
        break
else:
    print('Цифр нет')

s = input()
count = 0 

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
        
print(count)

s = input().lower()

vowels = 0
consonants = 0

# вариант 1
for i in 'ауоыиэяюе':
    vowels += s.count(i)
for i in 'бвгджзйклмнпрстфхцчшщ':
    consonants += s.count(i)
    
print(f'Количество гласных букв равно {vowels}')
print(f'Количество согласных букв равно {consonants}')

# вариант 2
for i in s:
    if i in 'ауоыиэяюе':
        vowels += 1 
    elif i in 'бвгджзйклмнпрстфхцчшщ':
        consonants += 1 
    
print(f'Количество гласных букв равно {vowels}')
print(f'Количество согласных букв равно {consonants}')

s = int(input())
b = ''

while s > 0:
    b += str(s % 2)
    s //= 2
    
print(b[::-1])

s = 'abcdefghij'
print(s[1:7:2])
print(s[3::2])
print(s[:7:3])
print(s[::2])
print(s[::-1])
print(s[::-2])

s = 'abcdefghij'

print(s[2:][:-2])
print(s[1::2][::-1][:3])

s = s[:4] + 'X' + s[5:]

birth_year = 1992
name = 'Timur'
profession = 'math teacher'
text = 'My name is {0}, I was born in {1}, I work as a {2}.'.format(name, birth_year, profession)

print(text)

name = 'Timur'
city = 'Moscow'
text1 = 'My name is {0}-{0}-{0}!'.format(name, city)
text2 = '{1} is my city and {0} is my name!'.format(name, city)

print(text1)
print(text2)

first_name = 'Taylor'
second_name = 'Swift'
country = 'USA'
birth_date = '1989/12/13'
birth_place = 'West Reading, Pennsylvania'
text = '{0} {1} is a very famous singer from the {2}. She was born on {3} in {4}.'.format(first_name, second_name, country, birth_date, birth_place)
print(text)

first_name = 'Taylor'
last_name = 'Swift'
country = 'USA'
birth_date = '1989/12/13'
birth_place = 'West Reading, Pennsylvania'
text = f'{first_name} {last_name} is a very famous singer from the {country}. She was born on {birth_date} in {birth_place}.'
print(text)


print(f'5 + 2 = {5 + 2}')
print(f'5 - 2 = {5 - 2}')
print(f'5 * 2 = {5 * 2}')
print(f'5 / 2 = {5 / 2}')

number_pi = 3.141592653589793
a = 1 / 8
b = 1 / 2
c = 1 / 3

print(f'{a=:.3f}')         # a=0.125
print(f'{number_pi=:6f}')  # number_pi=3.141593
print(f'{number_pi:6f}')   # 3.141593
print(f'{b=:.3f}')         # b=0.500
print(f'{c=:.3f}')         # c=0.333
print('------')
print(f'{c:.3f}')          # 0.333
print(f'{c:.1f}')          # 0.3
print(f'{c:.2f}')          # 0.33
print(f'{c:.10f}')         # 0.3333333333

print('---')

# По умолчанию символом заполнителем является пробел, но можно его заменить на другое значение

number = 12345.6789
print(f"Число {number=}")
print(f"|{number:=<25}|")
print(f"|{number:=>25}|")
print(f"|{number:=^25}|")
print('-' * 25)
text = "Python 3.10"
print(f"Строка {text=}")
print(f"|{text:-<25}|")
print(f"|{text:!>25}|")
print(f"|{text:?^25}|")

n = 12345

print(f'{n:8d}')  # 12345
print(f'{n:7d}')  # 12345
print(f'{n:6d}')  # 12345
print(f'{n:5d}')  # 12345
print(f'{n:4d}')  # 12345

n = 12345

print(f'{n:08d}')  # 00012345
print(f'{n:07d}')  # 0012345
print(f'{n:06d}')  # 012345
print(f'{n:05d}')  # 12345
print(f'{n:04d}')  # 12345

n = 12345678912345
print(f'{n:,d}')      # 12,345,678,912,345
print(f'{n:_d}')      # 12_345_678_912_345

sep = '_'             # вложенная f-строка
print(f'{n:{sep}d}')  # 12_345_678_912_345

# Если вы попытаетесь указать другие знаки разделителя вместо знаков "," и "_" , получите ошибку
# Также нельзя совмещать указание разделителя с указанием количества разрядов.

# < Выравнивает выражение в фигурных скобках по левому краю. У строк такое поведение по умолчанию
# > Выравнивает выражение в фигурных скобках по правому краю. У чисел такое поведение по умолчанию
# ^ Выравнивает выражение в фигурных скобках по центру

# Символы "|" используются в f-строке, чтобы помочь очертить интервал.
# Число после «:» указывает на количество символов в ширину.

number = 12345.6789
print(f"Число {number=}")
print(f"|{number:25}|")
print(f"|{number:<25}|")
print(f"|{number:>25}|")
print(f"|{number:^25}|")

print('-' * 25)

text = "Python 3.10"

print(f"Строка {text=}")
print(f"|{text:25}|")
print(f"|{text:<25}|")
print(f"|{text:>25}|")
print(f"|{text:^25}|")