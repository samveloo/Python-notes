import time

# Имя нашего словаря
DICTIONARY_FILE = "../rockyou.txt"

# Пароль, который мы ищем (попробуй ввести что-то популярное, например: qwerty, iloveyou или 123456)
target_password = input("Введите пароль для симуляции взлома: ")

print("\n[+] Загрузка словаря и начало атаки...\n")
start_time = time.time()

found = False
count = 0

# errors='ignore' спасет нас от кривых символов, на которых споткнулся архиватор
with open(DICTIONARY_FILE, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        count += 1
        
        # Убираем невидимый символ переноса строки \n в конце слова
        guess = line.strip()
        
        # Чтобы консоль не лагала, показываем процесс каждые 50 000 попыток
        if count % 50000 == 0:
            print(f"Проверено паролей: {count}... Текущий: {guess}", end="\r")
            
        # Проверяем совпадение
        if guess == target_password:
            end_time = time.time()
            print("\n" + "="*40)
            print(f"Пароль взломан: {guess}")
            print(f"Позиция в словаре: № {count}")
            print(f"Затрачено времени: {round(end_time - start_time, 2)} сек.")
            print("="*40)
            found = True
            break

if not found:
    end_time = time.time()
    print(f"\nПароль не найден в словаре. Проверено строк: {count}")
    print(f"Время поиска: {round(end_time - start_time, 2)} сек.")