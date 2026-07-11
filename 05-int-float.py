num0 = float('1.2345')   # преобразование строки к числу с плавающей точкой

n = int(input())
if n == 1:
    print(10.5)
elif n == 2:
    print(21)
else:
    n2 = n - 2
    years = 21 + 4 * n2
    print(years)

num = float(input())
num2 = int(num)
num3 = num - num2
print(num3)

num = float(input())
num2 = num * 10
num3 = int(num2) % 10
print(num3)

tF = float(input())
tC = (5 / 9) * (tF - 32)
print(tC)

a, b = float(input()), float(input())
S = 0.5 * a * b
print(S)

a = max(3, 8, -3, 12, 9)
b = min(3, 8, -3, 12, 9)
c = max(3.14, 2.17, 9.8)
print(a)
print(b)
print(c)

print(abs(10))
print(abs(-7))
print(abs(0))
print(abs(-17.67))

a, b, c = int(input()), int(input()), int(input())
print('Наименьшее число =', min(a, b, c))
print('Наибольшее число =', max(a, b, c))

