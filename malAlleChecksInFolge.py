import os
import re
import subprocess

cwd = os.getcwd()
foldername = "/testfolder"

windows = True
alreadyInstalled = True if os.path.isdir(cwd + foldername) else False 
wslInstalled = False
dockerInstalled = False
gitInstalled = False

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

print(windows, alreadyInstalled, gitInstalled, dockerInstalled, wslInstalled)



# sudo apt install git-all

# sudo apt-get update
# sudo apt-get install ca-certificates curl
# sudo install -m 0755 -d /etc/apt/keyrings
# sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
# sudo chmod a+r /etc/apt/keyrings/docker.asc

# # Add the repository to Apt sources:
# echo \
#   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
#   $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
#   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# sudo apt-get update

# sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

