import subprocess


def installDocker(windows=False):
    listOfCommands = ["sudo apt-get update", 
            "sudo apt-get install ca-certificates curl",
            "sudo install -m 0755 -d /etc/apt/keyrings",
            "sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc",
            "sudo chmod a+r /etc/apt/keyrings/docker.asc",
            """echo \
                "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
                $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
                sudo tee /etc/apt/sources.list.d/docker.list > /dev/null""",
            "sudo apt-get update",
            "sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"]
    for command in listOfCommands:
        list = command.split(sep=" ")
        if windows:
            list.insert(0, "wsl")
        try:
            ans = subprocess.Popen(list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, errors = ans.communicate()
            print(output)
        except:
            print(errors)
        

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
    # wsl --install -d Ubuntu-20.04
    print("Installing Ubuntu 20.04")
    #!!!!!!!!!!!!!!!! wsl --set-default-version 2
    #ans = subprocess.Popen(["wsl", "--install", "-d", "Ubuntu-20.04"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #print("Yeahhhhhhhhhh")
    #output, errors = ans.communicate()
    #print(output)

    #https://stackoverflow.com/questions/47380378/run-process-as-admin-with-subprocess-run-in-python
    

    prog = subprocess.Popen(['runas', '/noprofile', '/user:Administrator', "wsl", "--install", "-d", "Ubuntu-20.04"],stdin=subprocess.PIPE)
    prog.stdin.write('!Samk2024!'.encode())
    prog.communicate()
    print("HHHHHH")
    #output, errors = ans.communicate()
    #print(output)

installWSL2()
