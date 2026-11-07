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

