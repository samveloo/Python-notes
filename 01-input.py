number = 5
# del number # del - удаляет переменную # тут ошибка
print('Результат:', number)

del number  # а тут все нормально

number = 7
print('Результат:', number)

variable_name = input('Введите ваше имя: ')
print('Привет', variable_name)

name1 = 'Тимур'
name2 = name1
name1 = 'Гвидо'
print(name1)
print(name2)

# сначала тут печатается строка 'Как тебя зовут', а потом принимается на вход имя
name = input('Как тебя зовут? ')

first = input()
second = input()

print('I am', first, 'and', second)

name = input('Введите свое имя:')