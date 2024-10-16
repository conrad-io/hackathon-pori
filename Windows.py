import re
import subprocess
from tkinter import messagebox,IntVar,PhotoImage,StringVar
import customtkinter as ctk
from PIL import Image
import os
import time

class windows(ctk.CTk):
    # Define each page
    def page_welcome():
        label = ctk.CTkLabel(self.content_frame, text="Welcome to the Installation Wizard", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=50)

    def page_host_system():
        label = ctk.CTkLabel(self.content_frame, text="Please select your host system.", font=ctk.CTkFont(size=18))
        label.pack(pady=10)

        radiobutton_1 = ctk.CTkRadioButton(self.content_frame, text="Windows", value=1, variable= self.host_var, command=self.toggle_RadioButton)
        radiobutton_2 = ctk.CTkRadioButton(self.content_frame, text="Linux", value=2, variable= self.host_var, command=self.toggle_RadioButton)

        radiobutton_1.pack(padx=20, pady=10)
        radiobutton_2.pack(padx=20, pady=10)
    
    def toggle_RadioButton():
        self.next_button.configure(state="normal")

    def page_git_password():
        label = ctk.CTkLabel(self.content_frame, text="Please enter your password for the ACROBA Platform", font=ctk.CTkFont(size=18))
        label.pack(pady=10)
        password = StringVar()

        dir_entry = ctk.CTkEntry(self.content_frame, textvariable=password, show="*")
        dir_entry.insert(0, "")
        dir_entry.pack(pady=10)

    def page_summary():
        windows = self.host_var.get()==1
        self.gitInstalled = self.gitCheck(windows)
        self.dockerInstalled = self.dockerCheck(windows)
        self.wslInstalled = self.wslCheck()
        label = ctk.CTkLabel(self.content_frame, text="Ready to Install", font=ctk.CTkFont(size=18))
        label.pack(pady=50)

        summary = ctk.CTkLabel(self.content_frame, text=f"Selected host system: Windows" if windows else "Selected host system: Linux")
        summary.pack()
        summary = ctk.CTkLabel(self.content_frame, text="Git is installed and working" if self.gitInstalled else "Git not installed")
        summary.pack()
        summary = ctk.CTkLabel(self.content_frame, text="Docker is installed and working" if self.dockerInstalled else "Docker not installed")
        summary.pack()
        if windows:
            summary = ctk.CTkLabel(self.content_frame, text="wsl is installed and working" if self.wslInstalled else "wsl not installed")
            summary.pack()

    def notInstalledProgramm_installer():
        if not self.gitInstalled:
            label = ctk.CTkLabel(self.content_frame, text="git is missing :b").pack(pady=2)
            time.sleep(2)
            self.run_command("echo yes | sudo apt install git")

            
            pass
        if not self.dockerInstalled:
            pass
        if not self.wslInstalled:
            pass
        pass


    def clonePassword():
        # Just a label text
        label = ctk.CTkLabel(self.content_frame, text="password for the cloning process", font=ctk.CTkFont(size=18))
        label.pack(pady=15)

        # Terminal outputs are shown here
        result_text = ctk.CTkTextbox(self.content_frame, height=100, width=320, state="disable")
        result_text.pack(pady=2)

        # Button for cloning
        button = ctk.CTkButton(self.content_frame, text="install git", state="disable" if self.gitInstalled else "normal", font=ctk.CTkFont(size=18), command =lambda: self.run_command("sudo apt install git", result_text))
        button.pack(pady=10)


        # Button for cloning
        button = ctk.CTkButton(self.content_frame, text="install docker", state="disable" if self.dockerInstalled else "normal", font=ctk.CTkFont(size=18), command =lambda: self.run_command("git clone --progress https://github.com/acroba-hackathon/setup.git", result_text))
        button.pack(pady=10)


        # # Button for cloning
        # button = ctk.CTkButton(self.content_frame, text="install wsl", font=ctk.CTkFont(size=18), command =lambda: self.pathexist("git clone --progress https://github.com/acroba-hackathon/setup.git", result_text))
        # button.pack(pady=10)

        # Button for cloning
        button = ctk.CTkButton(self.content_frame, text="pull git repository and enter password", font=ctk.CTkFont(size=18), command =lambda: self.pathexist("git clone --progress https://github.com/acroba-hackathon/setup.git", result_text))
        button.pack(pady=10)

        # Button for installation
        button2 = ctk.CTkButton(self.content_frame, text="pinstall acroba enviornment", font=ctk.CTkFont(size=18), command =lambda: self.run_command("echo y | setup/setup.sh", result_text))
        button2.pack(pady=10)

        

    def page_complete():
        label = ctk.CTkLabel(self.content_frame, text="Installation Complete", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=50)

        complete_message = ctk.CTkLabel(self.content_frame, text="The installation was successful!")
        complete_message.pack()