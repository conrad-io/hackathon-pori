# Zum Testen von Existenz von Acroba
import os

cwd = os.getcwd()
foldername = "/testfolder"


# Fragen, ob Linux oder Windows
import tkinter as tk

def setWindows():
    global windows
    windows = True

windows = False

root = tk.Tk()

windowsbutton = tk.Button(root, text = "Windows", command=setWindows)
windowsbutton.pack()

linuxbutton = tk.Button(root, text="Linux")
linuxbutton.pack()

root.mainloop()


# Checken, ob git und docker installiert sind
import subprocess
import re

gitInstalled = False
dockerInstalled = False

try:
    ans = subprocess.Popen(["git", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, errors = ans.communicate()
    gitInstalled = True
except:
    pass

try:
    ans = subprocess.Popen(["docker", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, errors = ans.communicate()
    match = re.search(r'(\d+)\.', output)
    if int(match.group(1)) >= 24:
        dockerInstalled = True
except:
    pass


# Check, ob WSL installiert ist
windows = True
wslInstalled = False

if windows:
    try:
        ans = subprocess.Popen(["wsl", "cat", "/proc/version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, errors = ans.communicate()
        match = re.search(r'WSL(\d+)', output)
        if int(match.group(1)) == 2:
            wslInstalled = True
    except:
        pass

print(wslInstalled)