from tkinter import messagebox,IntVar
import customtkinter as ctk

# Initialize the CustomTkinter theme
ctk.set_appearance_mode("Dark")  # Options: "Light" or "Dark"
ctk.set_default_color_theme("blue")  # Other options: "green", "dark-blue"

class WizardApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.host_var = IntVar(value=0)
        # Window properties
        self.title("ACROBA Platform Installation Wizard")
        self.geometry("700x400")  # Adjust width to accommodate sidebar

        # Step counter to track the current step
        self.current_step = 0
        # Page methods for each step
        self.pages = [
            self.page_welcome,
            self.page_host_system,
            self.page_installation_directory,
            self.page_summary,
            self.page_complete
        ]

        # Main layout: Create two main frames (Sidebar and Content)
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")
        
        self.content_frame = ctk.CTkFrame(self, corner_radius=10)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)



        # Sidebar content (step labels)
        self.sidebar_label = ctk.CTkLabel(self.sidebar_frame, text="Steps", font=ctk.CTkFont(size=16, weight="bold"))
        self.sidebar_label.pack(pady=10)

        # Step labels in the sidebar
        self.step_labels = []
        for i in range(len(self.pages)-1):
            step_label = ctk.CTkLabel(self.sidebar_frame, text=f"Step {i+1}", font=ctk.CTkFont(size=14))
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

        self.back_button = ctk.CTkButton(self.button_frame, text="Back", command=self.prev_page, state="disabled")
        self.back_button.pack(side="left", padx=10)

        self.next_button = ctk.CTkButton(self.button_frame, text="Next", command=self.next_page)
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
            self.step_labels[self.current_step-1].configure(text_color="white")
        self.current_step += 1
        self.step_labels[self.current_step-1].configure(text_color="cyan")

        if self.current_step == len(self.pages) - 1:
            self.next_button.configure(text="Finish", command=self.finish)
        self.back_button.configure(state="normal")
        if self.current_step == 1 and self.host_var.get() == 0:
            self.next_button.configure(state="disabled")

        self.show_page()

    def prev_page(self):
        self.step_labels[self.current_step-1].configure(text_color="white")
        self.current_step -= 1
        self.step_labels[self.current_step-1].configure(text_color="cyan")

        if self.current_step == 0:
            self.back_button.configure(state="disabled")
        self.next_button.configure(state="normal")
        self.next_button.configure(text="Next", command=self.next_page)

        self.show_page()

    def finish(self):
        # Perform final actions, such as completing the installation
        messagebox.showinfo("Installation Complete", "The installation was successful!")
        self.quit()

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

    def page_installation_directory(self):
        label = ctk.CTkLabel(self.content_frame, text="Choose installation directory", font=ctk.CTkFont(size=18))
        label.pack(pady=10)

        dir_entry = ctk.CTkEntry(self.content_frame, width=400)
        dir_entry.insert(0, "C:/Program Files/MyApp")
        dir_entry.pack(pady=10)

    def page_summary(self):
        label = ctk.CTkLabel(self.content_frame, text="Ready to Install", font=ctk.CTkFont(size=18))
        label.pack(pady=50)

        summary = ctk.CTkLabel(self.content_frame, text="Installation directory: C:/Program Files/MyApp")
        summary.pack()

    def page_complete(self):
        label = ctk.CTkLabel(self.content_frame, text="Installation Complete", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=50)

        complete_message = ctk.CTkLabel(self.content_frame, text="The installation was successful!")
        complete_message.pack()

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

