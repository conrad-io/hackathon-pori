import tkinter as tk
import subprocess
import re

def doChecks(windows=False):
    gitInstalled = False
    dockerInstalled = False
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

    return windows, gitInstalled, dockerInstalled, wslInstalled


root = tk.Tk()

mswButton = tk.Button(root, text="Windows", command=lambda: doChecks(True))
mswButton.pack()

uButton = tk.Button(root, text="Ubuntu", command= lambda: doChecks(False))
uButton.pack()

root.mainloop()