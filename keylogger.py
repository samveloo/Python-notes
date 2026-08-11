import os
import evdev
from evdev import InputDevice, ecodes

LOG_FILE = "/home/samvel/Документы/IT/python/log.txt"

def find_keyboard():
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if "keyboard" in device.name.lower() or "kbd" in device.name.lower():
            return device.path
    for device in devices:
        if 1 in device.capabilities():
            return device.path
    return None

kbd_path = find_keyboard()

if not kbd_path:
    print(" Клавиатура не найдена в системе!")
    exit()

print(f"Найдено устройство клавиатуры: {kbd_path}")
device = InputDevice(kbd_path)

print("Слушатель клавиатуры запущен. Нажимайте клавиши в ЛЮБОМ окне...")
print("Для выхода нажмите Ctrl+C в терминале.")

try:
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY and event.value == 1:
            key_name = ecodes.KEY.get(event.code, f"KEY_{event.code}")
            
            if isinstance(key_name, list):
                key_name = key_name[0]
                
            clean_key = key_name.replace("KEY_", "")
            
            if clean_key == "SPACE":
                clean_key = " "
            elif clean_key == "ENTER":
                clean_key = "\n"
            else:
                if len(clean_key) > 1:
                    clean_key = f" [{clean_key}] "
                else:
                    clean_key = clean_key.lower() # переводим буквы в нижний регистр

            with open(LOG_FILE, "a", encoding="utf-8") as file:
                file.write(clean_key)
                
except KeyboardInterrupt:
    print("\nРабота завершена!")
