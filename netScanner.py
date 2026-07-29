import sys
import logging
import urllib.request
import json
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import ARP, Ether, srp, get_if_addr, conf

def get_vendor(mac_address):
    # Сервис, который бесплатно отдает название бренда по MAC-адресу
    url = f"https://macvendors.com{mac_address}"
    try:
        # Делаем запрос к API
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=2) as response:
            return response.read().decode('utf-8')
    except:
        return "Неизвестный бренд"

def scan_my_network():
    print("🛰️  Запуск продвинутого сетевого сканера...")
    
    try:
        my_ip = get_if_addr(conf.iface)
        ip_parts = my_ip.split(".")
        target_ip_range = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"
    except Exception as e:
        print(f"❌ Ошибка сети: {e}")
        return

    arp_request = ARP(pdst=target_ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_packet = broadcast / arp_request

    print("🔍 Сканирую Wi-Fi сеть и пробиваю производителей устройств (это займет чуть больше времени)...")
    answered_list, _ = srp(arp_request_packet, timeout=3, verbose=False)

    print("\n" + "="*85)
    print(f"{'IP-Адрес':<18} | {'MAC-Адрес':<20} | {'Производитель техники':<30}")
    print("="*85)
    
    for element in answered_list:
        device_ip = element[1].psrc
        device_mac = element[1].hwsrc
        
        # Определяем бренд по MAC-адресу
        vendor = get_vendor(device_mac)
        
        marker = " (Это ты)" if device_ip == my_ip else ""
        print(f"{device_ip:<18} | {device_mac:<20} | {vendor}{marker}")
        
    print("="*85)
    print("🏁 Сканирование завершено!")

if __name__ == "__main__":
    scan_my_network()
