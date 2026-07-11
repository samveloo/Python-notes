print("Hello World")
# sep - разделитель между элементами, end - конец строки
print("Результат:", 5, 7, sep = '|', end = '!\n')

minus = '-'
print('aa', 'bb', 'cc', sep = minus)

print('a', '\n', 'b', '\n', 'c', sep = '*', end = '#')

print('a', 'b', 'c', sep = '*', end = 'finish')

arg1 = 'Hello'
sep1 = '_-_'
end2 = '+++'
print(arg1, 'everyone', sep = sep1, end = '! ')
print('How', 'are', 'you', 'in', '2025?', sep = ' ', end = end2)
 
print('a', 'b', 'c', sep = '', end = '')
print('d', 'e', 'f', sep = '', end = '')

print("Python", end="\n\n\n")

# Множественное присваивание
name, surname = 'Timur', 'Guev'
print('Имя:', name, 'Фамилия:', surname)
# или
name = 'Timur'
surname = 'Guev'
print('Имя:', name, 'Фамилия:', surname)

name, surname = input(), input()
print("Имя:", name, "Фамилия:", surname)

name1 = 'Timur'
name2 = 'Gvido'

name1, name2 = name2, name1
print(name1, name2)

# специальные символы
print("Second \" \\ \t  Line")
print('Second " Line')

# input - ввод чего-либо
input("Введите ваше имя: ")

print('Как тебя зовут?')  # вывод текста

print('Привет,', input())  # ввод текста и вывод текста