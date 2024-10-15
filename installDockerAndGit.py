import subprocess

def installDocker(windows=False):
    listOfCommands = [
        "sudo apt-get update",
        "sudo apt-get install -y ca-certificates curl",
        "sudo mkdir -m 0755 -p /etc/apt/keyrings",
        "sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc",
        "sudo chmod a+r /etc/apt/keyrings/docker.asc",
        'echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $(VERSION_CODENAME)) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null',
        "sudo apt-get update",
        "sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"
    ]
    
    for command in listOfCommands:
        if windows:
            # Füge "wsl" am Anfang des Befehls hinzu
            command = f"wsl {command}"
        
        try:
            print(f"Ausführe: {command}")
            ans = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
            print(ans.stdout)
            if ans.stderr:
                print(f"Fehler: {ans.stderr}")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")

# Beispielaufruf
installDocker(windows=True)


        

def installGit(windows=False):
    list = ["sudo", "apt", "install", "git-all"]
    if windows:
        list.insert(0, "wsl")
    try:
        ans = subprocess.Popen(list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, errors = ans.communicate()
        print(output)
    except:
        print(errors)

def installWSL2():
    print("Installing Ubuntu 20.04")
    ans = subprocess.Popen(["wsl", "--set-default-version", "2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, errors = ans.communicate()
    print(output)

    prog = subprocess.Popen(['runas', '/noprofile', '/user:Administrator', "wsl", "--install", "-d", "Ubuntu-20.04"],stdin=subprocess.PIPE)
    prog.stdin.write('!Samk2024!'.encode())
    output, errors = prog.communicate()
    print(output)