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