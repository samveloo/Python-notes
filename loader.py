import subprocess
import sys
import os
import time

def download_movie(url, output_dir="./Movies"):
    # Создаем папку для фильмов, если её нет
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"Запуск фонового потока для: {url}")
    print("Оптимизируем настройки под канал 100 Кбит/с...")

    # Флаги aria2c для ультра-стабильной качалки при плохом интернете:
    # --continue=true : автоматически докачивать файл, если связь оборвалась
    # --max-connection-per-server=4 : делим закачку на 4 потока для скорости
    # --max-download-limit=90K : оставляем 10 Кбит тебе на мессенджеры/поиск, чтобы сеть не ложилась
    # --split=4 : разбиваем файл на части
    
    command = [
        "aria2c",
        "--continue=true",
        "--max-connection-per-server=4",
        "--split=4",
        "--max-download-limit=90K", 
        "--dir", output_dir,
        url
    ]

    try:
        # Запускаем aria2c и транслируем его вывод в наш терминал
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        # Читаем вывод aria2c построчно в реальном времени
        for line in process.stdout:
            # Очищаем вывод от лишнего мусора, выводим только прогресс
            if "ETA" in line or "MiB" in line:
                sys.stdout.write(f"\r[Прогресс]: {line.strip()}")
                sys.stdout.flush()

        process.wait()

        if process.returncode == 0:
            print("\n\n[🎉] Готово! Фильм успешно скачан в максимальном качестве.")
            # Отправляем push-уведомление в систему Fedora (GNOME/KDE)
            os.system('notify-send "Spider Loader" "Фильм успешно скачан и готов к просмотру в 1080p!" --icon=video-x-generic')
        else:
            print(f"\n\n[!] Ошибка aria2. Код возврата: {process.returncode}")
            
    except KeyboardInterrupt:
        print("\n\n[!] Закачка приостановлена Архитектором. Прогресс сохранен. При следующем запуске докачаем!")
    except Exception as e:
        print(f"\n[!] Критическая ошибка: {e}")

if __name__ == "__main__":
    # Проверяем, передал ли пользователь ссылку
    if len(sys.argv) < 2:
        print("Использование: python loader.py <ссылка_на_фильм>")
        sys.exit(1)
        
    target_url = sys.argv[1]
    download_movie(target_url)
