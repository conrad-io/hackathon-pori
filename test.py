import re
import subprocess
from tkinter import messagebox,IntVar,PhotoImage,StringVar
import customtkinter as ctk
from PIL import Image
import os
import time

# Initialize the CustomTkinter theme
ctk.set_appearance_mode("Light")  # Options: "Light" or "Dark"
ctk.set_default_color_theme("dark-blue")  # Other options: "green", "dark-blue"

class WizardApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.host_var = IntVar(value=0)
        # Window properties
        # self.iconbitmap("cropped-ACROBA_logo_icon_RVB-32x32.ico")
        self.title("ACROBA Platform Installation Wizard")
        self.geometry("700x400")  # Adjust width to accommodate sidebar

        # Step counter to track the current step
        self.current_step = 0
        # Page methods for each step
        self.pages = [
            self.page_welcome,
            self.page_host_system,
            self.page_git_password,
            self.page_summary,
            self.notInstalledProgramm_installer,
            self.clonePassword,
            self.page_complete
        ]

        # Main layout: Create two main frames (Sidebar and Content)
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=10)
        self.sidebar_frame.pack(side="left", fill="y", padx=10, pady=10)
        
        self.content_frame = ctk.CTkFrame(self, corner_radius=10)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)



        # Sidebar content (step labels)
        self.sidebar_image = PhotoImage(file="ACROBA-logo-text2.png")
        self.sidebar_label = ctk.CTkLabel(self.sidebar_frame, image=self.sidebar_image, text="", width=50)
        self.sidebar_label.pack(pady=10)

        # Step labels in the sidebar
        self.step_labels = []
        for i in range(len(self.pages)-1):
            step_label = ctk.CTkLabel(self.sidebar_frame, text=f"Step {i+1}", font=ctk.CTkFont(size=14), text_color="#1E1F57")
            step_label.pack(pady=10)
            self.step_labels.append(step_label)

        # Wizard content (header and text)
        # self.header_label = ctk.CTkLabel(self.content_frame, text="Wizard Step 1", font=ctk.CTkFont(size=18, weight="bold"))
        # self.header_label.pack(pady=15)

        # self.content_label = ctk.CTkLabel(self.content_frame, text="", font=ctk.CTkFont(size=14), wraplength=450)
        # self.content_label.pack(pady=10)

        # Navigation buttons
        # Navigation buttons
        # self.back_button = ctk.CTkButton(self, text="Back", command=self.prev_page, state="disabled")
        # self.next_button = ctk.CTkButton(self, text="Next", command=self.next_page)

        # # Place buttons at the bottom
        # self.back_button.pack(side="left", padx=20, pady=20)
        # self.next_button.pack(side="right", padx=20, pady=20)
        self.button_frame = ctk.CTkFrame(self.content_frame)
        self.button_frame.pack(side="bottom", pady=20, fill="x")

        self.back_button = ctk.CTkButton(self.button_frame, text="Back", command=self.prev_page, state="disabled", bg_color="#1E1F57", fg_color="#1E1F57", hover_color="#00207f")
        self.back_button.pack(side="left", padx=10)

        self.next_button = ctk.CTkButton(self.button_frame, text="Next", command=self.next_page, bg_color="#1E1F57", fg_color="#1E1F57", hover_color="#00207f")
        self.next_button.pack(side="right", padx=10)

        # Initialize content and sidebar progress
        self.show_page()

    def show_page(self):
        # Clear the main frame
        for widget in self.content_frame.winfo_children():
            if widget != self.button_frame:
                widget.destroy()

        # Show the current step page
        self.pages[self.current_step]()
    
    # def show_first_page(self):
    #     self.current_step += 1
    #     self.step_labels[self.current_step].configure(text_color="cyan")
    #     if self.current_step == 1 and self.host_var.get() == 0:
    #         self.next_button.configure(state="disabled")
    #     self.show_page()
    
    def next_page(self):
        if(self.current_step != 0):
            self.step_labels[self.current_step-1].configure(text_color="#1E1F57")
        self.current_step += 1
        self.step_labels[self.current_step-1].configure(text_color="#8329f6")

        if self.current_step == len(self.pages) - 1:
            self.next_button.configure(text="Finish", command=self.finish)
        self.back_button.configure(state="normal")
        if self.current_step == 1 and self.host_var.get() == 0:
            self.next_button.configure(state="disabled")

        self.show_page()

    def prev_page(self):
        self.step_labels[self.current_step-1].configure(text_color="#1E1F57")
        self.current_step -= 1
        if(self.current_step != 0):
            self.step_labels[self.current_step-1].configure(text_color="#8329f6")

        if self.current_step == 0:
            self.back_button.configure(state="disabled")
        self.next_button.configure(state="normal")
        self.next_button.configure(text="Next", command=self.next_page)

        self.show_page()

    def finish(self):
        # Perform final actions, such as completing the installation
        messagebox.showinfo("Installation Complete", "The installation was successful!")
        self.quit()




    #------------------------------------------#
    #               rkinrwe windows           #
    #------------------------------------------#


    # Define each page
    def page_welcome(self):
        label = ctk.CTkLabel(self.content_frame, text="Welcome to the Installation Wizard", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=50)

    def page_host_system(self):
        label = ctk.CTkLabel(self.content_frame, text="Please select your host system.", font=ctk.CTkFont(size=18))
        label.pack(pady=10)

        radiobutton_1 = ctk.CTkRadioButton(self.content_frame, text="Windows", value=1, variable= self.host_var, command=self.toggle_RadioButton)
        radiobutton_2 = ctk.CTkRadioButton(self.content_frame, text="Linux", value=2, variable= self.host_var, command=self.toggle_RadioButton)

        radiobutton_1.pack(padx=20, pady=10)
        radiobutton_2.pack(padx=20, pady=10)
    
    def toggle_RadioButton(self):
        self.next_button.configure(state="normal")

    def page_git_password(self):
        label = ctk.CTkLabel(self.content_frame, text="Please enter your password for the ACROBA Platform", font=ctk.CTkFont(size=18))
        label.pack(pady=10)
        password = StringVar()

        dir_entry = ctk.CTkEntry(self.content_frame, textvariable=password, show="*")
        dir_entry.insert(0, "")
        dir_entry.pack(pady=10)

    def page_summary(self):
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

    def notInstalledProgramm_installer(self):
        label = ctk.CTkLabel(self.content_frame, text="oops, something is missing", font=ctk.CTkFont(size=18))
        label.pack(pady=15)

        # Terminal outputs are shown here
        result_text = ctk.CTkTextbox(self.content_frame, height=100, width=320, state="disable")
        result_text.pack(pady=2)

        if not self.gitInstalled:



            label = ctk.CTkLabel(self.content_frame, text="password of your system bellow")
            label.pack(pady=4)

            textBox = ctk.CTkEntry(self.content_frame, show="*")
            textBox.pack(pady=10)
                        
            # Button for cloning
            button = ctk.CTkButton(self.content_frame, text="install git", state="disable" if self.gitInstalled else "normal", font=ctk.CTkFont(size=18), command =lambda: self.run_command(f"echo {textBox.get()} | sudo -S apt install git", result_text))
            button.pack(pady=10)

            result_text.update_idletasks()
            
        if not self.dockerInstalled:
            button = ctk.CTkButton(self.content_frame, text="install docker", state="disable" if self.gitInstalled else "normal", font=ctk.CTkFont(size=18), command =lambda: self.run_command("sudo apt install --progress docker", result_text))
            button.pack(pady=10)
                
            result_text.update_idletasks()
            
        # if not self.wslInstalled:
        #     pass
        pass

    #   # Button for cloning
    #     button = ctk.CTkButton(self.content_frame, text="install git", state="disable" if self.gitInstalled else "normal", font=ctk.CTkFont(size=18), command =lambda: self.run_command("sudo apt install  --progress git", result_text))
    #     button.pack(pady=10)


    #     # Button for cloning
    #     button = ctk.CTkButton(self.content_frame, text="install docker", state="disable" if self.dockerInstalled else "normal", font=ctk.CTkFont(size=18), command =lambda: self.run_command("git clone --progress https://github.com/acroba-hackathon/setup.git", result_text))
    #     button.pack(pady=10)


    def clonePassword(self):
        # Just a label text
        label = ctk.CTkLabel(self.content_frame, text="password for the cloning process", font=ctk.CTkFont(size=18))
        label.pack(pady=15)

        # Terminal outputs are shown here
        result_text = ctk.CTkTextbox(self.content_frame, height=100, width=320, state="disable")
        result_text.pack(pady=2)

      


        # # Button for cloning
        # button = ctk.CTkButton(self.content_frame, text="install wsl", font=ctk.CTkFont(size=18), command =lambda: self.pathexist("git clone --progress https://github.com/acroba-hackathon/setup.git", result_text))
        # button.pack(pady=10)

        # Button for cloning
        button = ctk.CTkButton(self.content_frame, text="pull git repository and enter password", font=ctk.CTkFont(size=18), command =lambda: self.pathexist("git clone --progress https://github.com/acroba-hackathon/setup.git", result_text))
        button.pack(pady=10)

        # Button for installation
        button2 = ctk.CTkButton(self.content_frame, text="pinstall acroba enviornment", font=ctk.CTkFont(size=18), command =lambda: self.run_command("echo y | setup/setup.sh", result_text))
        button2.pack(pady=10)

        

    def page_complete(self):
        label = ctk.CTkLabel(self.content_frame, text="Installation Complete", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=50)

        complete_message = ctk.CTkLabel(self.content_frame, text="The installation was successful!")
        complete_message.pack()
    




    #------------------------------------------#
    #               chek certification          #
    #------------------------------------------#

    # Checking 
    def gitCheck(self, windows):
        command = "git --version"
        if windows:
            command = "wsl git --version"
        list = command.split(" ")
        try:
            ans = subprocess.Popen(list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, errors = ans.communicate()
            if "git version" in output:
                return True
        except:
            pass
        return False
    
    def wslCheck(self):
        try:
            ans = subprocess.Popen(["wsl", "cat", "/proc/version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, errors = ans.communicate()
            match = re.search(r'WSL(\d+)', output)
            if int(match.group(1)) == 2:
                return True
        except:
            pass
        return False
    
    def dockerCheck(self, windows):
        command = "docker --version"
        if windows:
            command = "wsl docker --version"
        list = command.split(" ")
        try:
            ans = subprocess.Popen(list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, errors = ans.communicate()
            match = re.search(r'(\d+)\.', output)
            if int(match.group(1)) >= 24:
                return True
        except:
            pass
        return False




    #------------------------------------------#
    #               command execution          #
    #------------------------------------------#


    def pathexist(self,command, result_text):
        path = "setup"
        
        result_text.configure(state="normal")
        result_text.delete(1.0, ctk.END)

        if os.path.isdir(path):
            result_text.insert(ctk.END, "already there")
            result_text.update_idletasks() 
            result_text.configure(state="disable")
            return

        self.run_command(command, result_text)

    def run_command(self, command, result_text):
        result_text.configure(state="normal")
        result_text.delete(1.0, ctk.END)

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        
        # Capture combined stdout and stderr in real-time
        for output_line in iter(process.stdout.readline, ""):
            print(output_line)
            result_text.insert(ctk.END, output_line)  # Insert the output into the text widget
            result_text.see(ctk.END)  # Scroll to the end of the text widget
            result_text.update_idletasks()  # Force GUI update

        process.stdout.close()
        process.wait()  # Ensure the process has fully completed

        result_text.configure(state="disable")



    #------------------------------------------#
    #               main and stuff            #
    #------------------------------------------#

if __name__ == "__main__":
    app = WizardApp()
    app.mainloop()

#     def update_content(self):
#         """Update the content area and sidebar based on the current step."""
#         # Update the main content
#         self.header_label.configure(text=f"Wizard Step {self.current_step + 1}")
#         self.content_label.configure(text=self.steps[self.current_step])

#         # Enable or disable back button based on step
#         self.back_button.configure(state="normal" if self.current_step > 0 else "disabled")

#         # Change Next button to Finish on the last step
#         if self.current_step == len(self.steps) - 1:
#             self.next_button.configure(text="Finish", command=self.finish)
#         else:
#             self.next_button.configure(text="Next", command=self.next)

#         # Update the sidebar to highlight the current step
#         for i, label in enumerate(self.step_labels):
#             if i == self.current_step:
#                 label.configure(text_color="cyan")  # Highlight the current step
#             else:
#                 label.configure(text_color="white")  # Reset others

#     def next(self):
#         """Proceed to the next step."""
#         if self.current_step < len(self.steps) - 1:
#             self.current_step += 1
#             self.update_content()

#     def back(self):
#         """Go to the previous step."""
#         if self.current_step > 0:
#             self.current_step -= 1
#             self.update_content()

#     def finish(self):
#         """Complete the wizard."""
#         self.header_label.configure(text="Wizard Complete!")
#         self.content_label.configure(text="Thank you for completing the wizard.")
#         self.next_button.pack_forget()  # Hide Next/Finish button
#         self.back_button.pack_forget()  # Hide Back button


# if __name__ == "__main__":
#     app = WizardApp()
#     app.mainloop()

