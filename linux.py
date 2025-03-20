import tkinter as tk
import platform
uname = platform.uname()
proc = uname.processor if uname.processor else uname.machine
info = f"ОС: {uname.system}\nВерсия: {uname.version}\nПлатформа: {uname.release}\nПроцессор: {proc}"
root = tk.Tk()
label = tk.Label(root, text="Линукс\n" + info, font=("Arial", 12))
label.pack(padx=20, pady=20)
root.mainloop()
