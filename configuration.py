import customtkinter as ctk
from tkinter import messagebox

# Initialize the CustomTkinter theme
ctk.set_appearance_mode("Dark")  # Options: "Light" or "Dark"
ctk.set_default_color_theme("blue")  # Other options: "green", "dark-blue"

class WizardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.geometry("700x400")  # Adjust width to accommodate sidebar
        self.title("Installation Wizard")

        # Initialize step
        self.current_step = 0

        # Frame for the pages
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Page methods for each step
        self.pages = [
            self.page_welcome,
            self.page_license,
            self.page_installation_directory,
            self.page_summary,
            self.page_complete
        ]

        # Navigation buttons
        self.prev_button = ctk.CTkButton(self, text="Back", command=self.prev_page, state="disabled")
        self.next_button = ctk.CTkButton(self, text="Next", command=self.next_page)
        self.finish_button = ctk.CTkButton(self, text="Finish", command=self.finish, state="disabled")

        # Place buttons at the bottom
        self.prev_button.pack(side="left", padx=20, pady=20)
        self.next_button.pack(side="right", padx=20, pady=20)
        self.finish_button.pack(side="right", padx=20, pady=20)

        # Show the first page
        self.show_page()

    def show_page(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Show the current step page
        self.pages[self.current_step]()

    def next_page(self):
        self.current_step += 1

        if self.current_step == len(self.pages) - 1:
            self.next_button.config(state="disabled")
            self.finish_button.config(state="normal")
        self.prev_button.config(state="normal")

        self.show_page()

    def prev_page(self):
        self.current_step -= 1

        if self.current_step == 0:
            self.prev_button.config(state="disabled")
        self.next_button.config(state="normal")
        self.finish_button.config(state="disabled")

        self.show_page()

    def finish(self):
        # Perform final actions, such as completing the installation
        messagebox.showinfo("Installation Complete", "The installation was successful!")
        self.quit()

    # Define each page
    def page_welcome(self):
        label = ctk.CTkLabel(self.main_frame, text="Welcome to the Installation Wizard", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=50)

    def page_license(self):
        label = ctk.CTkLabel(self.main_frame, text="Please accept the license agreement", font=ctk.CTkFont(size=18))
        label.pack(pady=10)

        license_text = ctk.CTkTextbox(self.main_frame, height=150, width=500)
        license_text.insert("1.0", "License agreement text goes here...")
        license_text.config(state="disabled")
        license_text.pack(pady=10)

        accept_var = ctk.StringVar(value="0")
        accept_check = ctk.CTkCheckBox(self.main_frame, text="I accept the terms and conditions", variable=accept_var)
        accept_check.pack(pady=10)

    def page_installation_directory(self):
        label = ctk.CTkLabel(self.main_frame, text="Choose installation directory", font=ctk.CTkFont(size=18))
        label.pack(pady=10)

        dir_entry = ctk.CTkEntry(self.main_frame, width=400)
        dir_entry.insert(0, "C:/Program Files/MyApp")
        dir_entry.pack(pady=10)

    def page_summary(self):
        label = ctk.CTkLabel(self.main_frame, text="Ready to Install", font=ctk.CTkFont(size=18))
        label.pack(pady=50)

        summary = ctk.CTkLabel(self.main_frame, text="Installation directory: C:/Program Files/MyApp")
        summary.pack()

    def page_complete(self):
        label = ctk.CTkLabel(self.main_frame, text="Installation Complete", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=50)

        complete_message = ctk.CTkLabel(self.main_frame, text="The installation was successful!")
        complete_message.pack()

if __name__ == "__main__":
    app = WizardApp()
    app.mainloop()
