import sys
import logging
# Глушим лишние предупреждения от Scapy при запуске
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import ARP, Ether, srp, get_if_addr, conf

def scan_my_network():
    print("🛰️  Запуск сетевого сканера...")
    
    # 1. Автоматически узнаем IP-адрес твоего ноута в локальной сети (например, 192.168.1.5)
    try:
        my_ip = get_if_addr(conf.iface)
        # Превращаем его в маску подсети (например, 192.168.1.0/24), чтобы сканировать все 254 адреса
        ip_parts = my_ip.split(".")
        target_ip_range = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"
        print(f"🏠 Твой IP: {my_ip} | Сканирую диапазон подсети: {target_ip_range}")
    except Exception as e:
        print(f"❌ Не удалось определить IP подсети: {e}")
        return

    # 2. Создаем ARP-запрос (спрашиваем "Кто здесь?")
    arp_request = ARP(pdst=target_ip_range)
    
    # 3. Упаковываем его в Ethernet-кадр, чтобы отправить на широковещательный адрес (всем сразу)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_packet = broadcast / arp_request

    # 4. Отправляем пакеты в сеть и ждем ответы (таймаут 3 секунды, чтобы долго не ждать)
    print("🔍 Отправляю пакеты в Wi-Fi сеть, жду ответы от устройств...")
    answered_list = srp(arp_request_packet, timeout=3, verbose=False)[0]

    # 5. Выводим результат
    print("\n" + "="*50)
    print(f"{'IP-Адрес устройства':<20} | {'MAC-Адрес (Физический адрес)':<20}")
    print("="*50)
    
    devices_count = 0
    for element in answered_list:
        # Из каждого ответа вытаскиваем IP и MAC-адрес прибора
        device_ip = element[1].psrc
        device_mac = element[1].hwsrc
        
        # Пометка, если устройство — твой собственный ноутбук
        marker = " (Это ты)" if device_ip == my_ip else ""
        
        print(f"{device_ip:<20} | {device_mac:<20}{marker}")
        devices_count += 1
        
    print("="*50)
    print(f"🏁 Сканирование завершено. Всего в сети найдено устройств: {devices_count}")

if __name__ == "__main__":
    scan_my_network()