answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы учим Python =)')
    print('Python - отличный язык!')
else:
    print("Не совсем так")

""" 
Выражение                        Описание
if x > 7	                     если x больше 7
if x < 7                         если x меньше 7
if x >= 7                        если x больше либо равен 7
if x <= 7                        если x меньше либо равен 7
if x == 7	                     если x равен 7
if x != 7                        если x не равен 7
"""

# решение задач
num1, num2 = int(input()), int(input())
if num1 > num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)

if num1 == num2:  # используем двойное равенство
    print(num1, 'равно', num2)
if num1 != num2:
    print(num1, 'не равно', num2)

age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')

num = int(input())
message = 'Четное' if num % 2 == 0 else 'Нечетное'
print(message)

a, b, c = int(input()), int(input()), int(input())
if 2 * b == a + c:
    print("YES")
else:
    print("NO")

a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)

x = int(input())

if 1000 <= x <= 9999 and (x % 17 == 0 or x % 7 == 0):
    print('YES')
else:
    print('NO')

x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a: 
    print('YES')
else:
    print('NO')

year = int(input())
if (year % 4 == 0 and not(year % 100 == 0)) or year % 400 == 0:
    print('YES')
else:
    print('NO')

# вложеный оператор
grade = int(input('Введите вашу отметку по 100-балльной системе: '))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70: 
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)

# каскадный оператор
grade = int(input('Введите вашу отметку: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)

# решение задач
angle = int(input())

if angle % 90 == 0:
    if angle == 0:
        print('Нулевой')
    elif angle == 90:
        print('Прямой')
    elif angle == 180:
        print('Развёрнутый')
else:
    if 0 < angle < 90:
        print('Острый')
    elif 90 < angle < 180:
        print('Тупой')
    elif 180 < angle < 270:
        print('Выпуклый')
    else:
        print('Ни острый, ни тупой, ни выпуклый')

a, b, c = int(input()), int(input()), int(input())
if a != b and a != c and b != c:
    print('Разносторонний')
elif a == b != c or a == c != b or b == c != a:
    print('Равнобедренный')
else:
    print('Равносторонний')
    
a, b, c = int(input()), int(input()), int(input())
numbers = [a, b, c]
numbers.sort()
print(numbers[1])

a = int(input())
31 = [1, 3, 5, 7, 8, 10, 12]
30 = [4, 6, 9, 11]
28 = [2]
if a in 31:
    print(31)
elif a in 30:
    print(30)
else:
    print(28)

num1, num2, op = int(input()), int(input()), input()
if op == '/':
    if num2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(num1 / num2)
elif op == '*':
    print(num1 * num2)
elif op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
else:
    print('Неверная операция')

col1, col2 = input(), input()
if col1 != 'красный' and col1 != 'синий' and col1 != 'желтый' or col2 != 'красный' and col2 != 'синий' and col2 != 'желтый':
    print('ошибка цвета')
if (col1 == 'желтый' or col2 == 'желтый') and (col1 == 'красный' or col2 == 'красный'):
    print('оранжевый')
if (col1 == 'желтый' or col2 == 'желтый') and (col1 == 'синий' or col2 == 'синий'):
    print('зеленый')
if (col1 == 'красный' or col2 == 'красный') and (col1 == 'синий' or col2 == 'синий'):
    print('фиолетовый')
if (col1 == col2) and ((col1 == 'красный' or col1 == 'синий' or col1 == 'желтый') and (col2 == 'красный' or col2 == 'синий' or col2 == 'желтый')):
    print(col1)

num = int(input())
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = 0
if num in red:
    print('красный')
elif num in black:
    print('черный')
elif num == green:
    print('зеленый')
else:
    print('ошибка ввода')