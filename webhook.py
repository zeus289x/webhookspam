import requests
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = r"""
          ___     __              __      __             
|  |    |__     |__)    |__|    /  \    /  \    |__/    
|/\|    |___    |__)    |  |    \__/    \__/    |  \    
                                                        
    """
    print(Fore.CYAN + banner)
    print(Fore.BLUE + "Bu tool Zeus289 tarafından hazırlanmıştır.".center(80))
    print(Fore.BLUE + "İletişim için: discord.gg/289".center(80))
    print(Fore.YELLOW + "-" * 80)

def send_webhook_messages(webhook_url, message, count, delay):
    for i in range(count):
        payload = {"content": message}
        response = requests.post(webhook_url, json=payload)
        
        if response.status_code == 204:
            print(Fore.GREEN + f"[{i+1}/{count}] Mesaj gönderildi: {message}")
        else:
            print(Fore.RED + f"[{i+1}/{count}] Hata! Kod: {response.status_code}")
        
        time.sleep(delay)

def main():
    clear_console()
    print_banner()
    
    print(Fore.YELLOW + "Lütfen bilgileri doldurun:")
    webhook_url = input(Fore.CYAN + "Webhook URL: ")
    message = input(Fore.CYAN + "Gönderilecek mesaj: ")
    count = int(input(Fore.CYAN + "Kaç tane mesaj atılsın: "))
    delay = int(input(Fore.CYAN + "Mesajlar arasındaki bekleme süresi (saniye): "))

    print(Fore.MAGENTA + "\nMesaj gönderiliyor...\n")
    send_webhook_messages(webhook_url, message, count, delay)
    print(Fore.GREEN + "\nGörev tamamlandı!")

if __name__ == "__main__":
    main()