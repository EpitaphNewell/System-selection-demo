import platform
import subprocess
import sys
if platform.system() == "Windows":
    print("Win")
    subprocess.run([sys.executable, "windows.py"])
elif platform.system() == "Linux":
    print("Linux")
    subprocess.run([sys.executable, "linux.py"])
else:
    print("Не поддерживаемая система (Мак_Ос что-ль?)")
