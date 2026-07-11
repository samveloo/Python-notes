num1 = 4            # число
num2 = 9            # число
num3 = num1 + num2  # число
print(num3)

# двухзначное число
num = 17
a = num % 10  # вычисляем последнюю цифру числа
b = num // 10  # вычисляем первую цифру числа
print(a)
print(b)

# трехзначное число
num = 754
a = num % 10             # вычисляем последнюю цифру числа
b = (num % 100) // 10    # вычисляем среднюю цифру числа
c = num // 100           # вычисляем первую цифру числа
print(a)
print(b)
print(c)

# Запишем формулу для вычисления i-й цифры n-значного числа num в общем виде:
# ! (num // 10 ** (n - i)) % 10

# математические действия
print("Результат:", 5 + 5)  # сложение
print("Результат:", 5 - 5)  # вычитание
print("Результат:", 5 * 5)  # умножение
print("Результат:", 5 / 5)  # деление
print("Результат:", 5 // 5)  # целочисленное деление
print("Результат:", 5 ** 5)  # степень
print(2 ** (-1))
print(2 ** 2 ** 3)  # 2 ** (2 ** 3) = 2 ** 8
print("Результат:", 5 % 5)  # остаток

"""
Оператор	                Описание
()	                        Скобки
**	                        Возведение в степень
-	                        Унарный минус
/, *, //, %	                Умножение, деление, целочисленное деление, остаток от деления
+, -	                    Сложение, вычитание
"""

# математические функции
print("Результат:", min(5, 6, 3, 0, -3, 9))  # min - минимальное значение
print("Результат:", max(5, 6, 3, 0, -3, 9))  # max - максимальное значение
print("Результат:", abs(-6))  # abs - модуль
print("Результат:", pow(2, 3))  # pow - возведение в степень, аналог **
print("Результат:", round(5 / 3))  # round - округление

# int - со строки в число
s = "1987"
year = int(s)
int(year)

num00 = int(input())

num = 17
s00 = str(num)

num4 = -6        # унарный минус
num5 = 17 - 7    # бинарный минус

# решение задач
x = 3 
y = 4 
z = x + y 
z = z + 1  # 8
x = y 
y = 5
x = z + y + 7
print(x)  # 20

num = input()
a = int(num)
b = a + 1 
c = a + 2
print(a, b, c, sep = "\n")

a, b, c = int(input()), int(input()), int(input())
print(a + b + c)

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print((a + b + c + d) * 3)

a, b = int(input()), int(input())
x = 3 * (a + b) ** 3 + 275 * b * b - 127 * a - 41
print(x)

a = int(input())
print("Следующее за числом", a, "число:", a + 1)
print("Для числа", a, "предыдущее число:", a - 1)

a = int(input())
v = a ** 3
s = 6 * a ** 2
print("Объем =", v)
print("Площадь полной поверхности =", s)

a, b = int(input()), int(input())
print(a, "+", b, "=", a + b)
print(a, "-",b, "=", a - b)
print(a, "*", b, "=", a * b)

b1, q, n = int(input()), int(input()), int(input())
print(b1 * q ** (n - 1))

a = int(input())
print(a // 100)

p = int(input())
m = int(input())
print(m // p)
print(m % p)

n = int(input())
a = n + (n % 2)
print(a // 2)

m = int(input())
h = m // 60
m2 = m - (h * 60)  # или m % 60
print(m, "мин - это", h, "час", m2, "минут.")

a = int(input())
print((a + 3) // 4)

s = 13
k = -5
d = s + 2
s = d
k = 2 * s
print(s + k + d)

a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)

x = input()
s = int(x)
s2 = int(x + x)
s3 = int(x + x + x)
res = s + s2 + s3
print(res)