import socket
import datetime
import subprocess
import os

print("-- Разведка Цели --")

target = input("[+] Название цели (например google.com): ") #ввод цели

if not os.path.exists("results"):
    os.mkdir("results") #создание папки для результата

filename = f"results/{target}.txt" #создание txt файла для хранения результатов разведки

print(f"[+] Идет разведка {target}...")

try:
    print("\n[+] Проверяю доступность сайта (ping)...")
    try:
        ping_result = subprocess.check_output(["ping", "-c", "1", "-W", "1", target], #отправляет пакеты для проверки доступа сайта
                                              encoding="utf-8", stderr=subprocess.STDOUT)
        print("[+] Сайт доступен")
    except subprocess.CalledProcessError as e:
        print("[-] Ошибка")

    ip = socket.gethostbyname(target) #превращает название сайта в айпи

    print(f"\n[+] Айпи: {ip}")

    ports = [21, 22, 80, 443, 3306, 8080, 8443]
    #21=FTP, 22=SSH, 80=HTTP, 443=HTTPS, 3306=MySQL,
    #8080=HTTP, 8443=HTTPS
    open_ports = []

    print("[+] Порты...")

    for port in ports: #делает проверку всех портов из списка
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создает соединение для подготовки проверки портов
        sock.settimeout(1.2)
        result = sock.connect_ex((ip, port)) #пытается подключится к порту

        if result == 0:
            print(f"[+] Порт {port} открыт")
            open_ports.append(port)
        else:
            print(f"[-] Порт {port} закрыт")

        sock.close()

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[+] Время: {datetime.datetime.now()}")

    with open(filename, "w", encoding="utf-8") as f: #сохранение результата в файл
        f.write("-- Результат разведки --")
        f.write(f"\nЦель: {target}")
        f.write(f"\nАйпи: {ip}")
        f.write(f"\nВремя: {current_time}")
        f.write("\n\n")

        if open_ports:
            f.write("\nОткрытые порты:\n")
            for p in open_ports:
                f.write(f"\n[+]Порт {p} открыт")
        else:
            f.write("Открытых портов не найдено")

    print(f"\n[+] Результат успешно сохранен в {filename}")

except Exception as e:
    print(f"[-] Error: {e}")

