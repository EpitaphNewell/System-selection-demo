import tkinter as tk
import platform
uname = platform.uname()
info = f"ОС: {uname.system}\nВерсия: {uname.version}\nПлатформа: {uname.release}\nПроцессор: {uname.processor}"
root = tk.Tk()
label = tk.Label(root, text="Виндовс\n" + info, font=("Arial", 12))
label.pack(padx=20, pady=20)
root.mainloop()
