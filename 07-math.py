import math

num1 = math.sqrt(2)     # вычисление квадратного корня из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

from math import sqrt, ceil, floor

num1 = sqrt(2)     # вычисление корня квадратного из двух
num2 = ceil(3.8)   # округление числа вверх
num3 = floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

from math import pi

R = float(input())
S =  pi * R ** 2
C = 2 * pi * R
print( S )
print( C )

from math import floor, ceil

x = float(input())
floorX = floor(x)
ceilX = ceil(x)
print(floorX + ceilX)

from math import sqrt
a, b = float(input()), float(input())
avgA = (a + b) / 2
avgGeo = sqrt(a * b)
avgGar = (2 * a * b) / (a + b)
avgK = sqrt((a**2 + b**2) / 2)
print(avgA, avgGeo, avgGar, avgK, sep='\n')

# код для решения квадратных уравнений
from math import sqrt
a, b, c = float(input()), float(input()), float(input())
D = b**2 - (4 * a * c)
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Нет корней')