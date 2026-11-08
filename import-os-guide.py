import os

# Получаем текущую папку
current_dir = os.getcwd()
print(f"Текущая директория: {current_dir}")

# Выводим список всех файлов в текущей папке
files = os.listdir('.')
print(f"Содержимое папки: {files}")

# Переходим в другую папку (замените на существующий путь)
# os.chdir('/path/to/directory')

# Создание одной папки
os.mkdir('new_folder')

# Создание вложенных папок (папка 'nested' и внутри нее 'data')
os.makedirs('nested/data', exist_ok=True)  # exist_ok=True предотвращает ошибку, если папка уже есть

# Удаление пустой папки
os.rmdir('new_folder')

# Переименование файла (или папки)
# os.rename('old_name.txt', 'new_name.txt')

# Удаление файла
# os.remove('new_name.txt')

# Узнаем тип ОС
print(f"Тип ОС: {os.name}")

# Получаем значение конкретной переменной окружения
path_env = os.environ.get('PATH')
print(f"Переменная PATH (первые 50 символов): {path_env[:50]}")

# Получаем размер файла (если файл существует)
if os.path.exists('script.py'):
    file_info = os.stat('script.py')
    print(f"Размер файла: {file_info.st_size} байт")

# Выполнить команду ping (для Windows -n, для Linux -c)
if os.name == 'nt':
    os.system('ping -n 1 google.com')
else:
    os.system('ping -c 1 google.com')

# Правильное объединение путей
full_path = os.path.join('documents', 'folder', 'file.txt')
print(f"Построенный путь: {full_path}")

# Проверка расширения файла
filename, extension = os.path.splitext('photo.jpg')
print(f"Имя: {filename}, Расширение: {extension}")