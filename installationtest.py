import subprocess
import sys

def run_powershell_command(command):
    """
    Führt einen PowerShell-Befehl aus und gibt die Ausgabe zurück.
    """
    try:
        result = subprocess.run(["powershell.exe", "-Command", command], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Fehler: {e}")
        sys.exit(1)

def run_wsl_command(command):
    """
    Führt einen Befehl in der Ubuntu-Umgebung in WSL aus.
    """
    try:
        result = subprocess.run(["wsl", "-d", "Ubuntu-20.04", "-e", "bash", "-c", command], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Ausführung in WSL: {e}")
        sys.exit(1)

def check_wsl_installation():
    """
    Überprüft, ob WSL bereits installiert ist.
    """
    result = run_powershell_command("wsl -l -v")
    if "Ubuntu-20.04" in result:
        print("Ubuntu 20.04 ist bereits installiert!")
    else:
        print("WSL scheint noch nicht installiert zu sein. Starte Installation...")
        install_ubuntu_20_04()

def install_wsl2():
    """
    Installiert WSL2 und aktiviert es.
    """
    print("Installiere WSL2...")

    # WSL-Feature aktivieren
    run_powershell_command("wsl --install")

    # WSL2 als Standard festlegen
    run_powershell_command("wsl --set-default-version 2")

def install_ubuntu_20_04():
    """
    Installiert die Ubuntu 20.04-Distribution in WSL2.
    """
    print("Installiere Ubuntu 20.04...")

    # Installiere explizit Ubuntu 20.04
    run_powershell_command("wsl --install -d Ubuntu-20.04")

    # Überprüfen, ob die Installation erfolgreich war
    result = run_powershell_command("wsl -l -v")
    if "Ubuntu-20.04" in result:
        print("Ubuntu 20.04 wurde erfolgreich installiert.")
    else:
        print("Es gab ein Problem bei der Installation von Ubuntu 20.04.")

def create_unix_user(username="test", password="pass"):
    """
    Erstellt einen neuen Benutzer mit dem angegebenen Namen und Passwort auf Ubuntu.
    """
    print(f"Erstelle Unix-Benutzer '{username}'...")

    # Befehl um einen neuen Benutzer zu erstellen und Passwort festzulegen
    commands = [
        f"sudo adduser --disabled-password --gecos '' {username}",
        f"echo '{username}:{password}' | sudo chpasswd",
        f"sudo usermod -aG sudo {username}"
    ]

    for command in commands:
        print(f"Führe aus: {command}")
        output = run_wsl_command(command)
        print(output)

    print(f"Benutzer '{username}' wurde erfolgreich erstellt.")

def install_docker_on_ubuntu():
    """
    Installiert Docker Engine auf Ubuntu innerhalb von WSL2.
    """
    print("Installiere Docker Engine auf Ubuntu...")

    commands = [
        "sudo apt-get update",
        "sudo apt-get install -y ca-certificates curl gnupg",
        "sudo install -m 0755 -d /etc/apt/keyrings",
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg",
        "echo \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
        "sudo apt-get update",
        "sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin",
        "sudo usermod -aG docker $USER",
    ]

    for command in commands:
        print(f"Führe aus: {command}")
        output = run_wsl_command(command)
        print(output)

    print("Docker wurde erfolgreich installiert.")
def make_dir():
    run_wsl_command("sudo apt-get update")


def main():

    print("Starte die Installation von Docker in Ubuntu...")
    #install_docker_on_ubuntu()
    make_dir()

    print("Installation abgeschlossen. Docker ist jetzt auf Ubuntu 20.04 in WSL2 verfügbar.")

if __name__ == "__main__":
    main()
