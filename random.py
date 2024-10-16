import subprocess
cp = subprocess.run(["wsl", "~", "-e", "sudo", "apt", "update"], capture_output=True)
print(cp.stdout.decode())