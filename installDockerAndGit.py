import subprocess

# sudo usermod -aG docker $USER
def installDocker(windows=False):
    command = "curl -sSL https://get.docker.com/ | sh"
    if windows:
        # Füge "wsl" am Anfang des Befehls hinzu
        command = f"wsl ~ -e curl -sSL https://get.docker.com/ | sh"
    try:
        print(f"Ausführe: {command}")
        ans = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        print(ans.stdout)
        if ans.stderr:
            print(f"Fehler: {ans.stderr}")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Beispielaufruf


        

def installGit(windows=False):
    list = ["sudo", "apt", "install", "-y", "git"]
    if windows:
        list.insert(0, "wsl")
    try:
        ans = subprocess.Popen(list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, errors = ans.communicate()
        print(output)
    except:
        print(errors)

installGit(True)

def installWSL2():
    print("Installing Ubuntu 20.04")
    ans = subprocess.Popen(["wsl", "--set-default-version", "2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, errors = ans.communicate()
    print(output)

    prog = subprocess.Popen(['runas', '/noprofile', '/user:Administrator', "wsl", "--install", "-d", "Ubuntu-20.04"],stdin=subprocess.PIPE)
    prog.stdin.write('!Samk2024!'.encode())
    output, errors = prog.communicate()
    print(output)