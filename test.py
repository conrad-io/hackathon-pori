import customtkinter as ctk

# Initialize the CustomTkinter theme
ctk.set_appearance_mode("Dark")  # Options: "Light" or "Dark"
ctk.set_default_color_theme("blue")  # Other options: "green", "dark-blue"

class WizardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title("Fancy Wizard Window with Progress Sidebar")
        self.geometry("700x400")  # Adjust width to accommodate sidebar

        # Step counter to track the current step
        self.current_step = 0
        self.steps = [
            "Welcome to the Custom Wizard!\nThis is Step 1: Introduction.",
            "This is Step 2: Please fill in the details.",
            "Step 3: Review your details and finish the wizard!"
        ]

        # Main layout: Create two main frames (Sidebar and Content)
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")

        self.content_frame = ctk.CTkFrame(self, corner_radius=10)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        # Sidebar content (step labels)
        self.sidebar_label = ctk.CTkLabel(self.sidebar_frame, text="Steps", font=ctk.CTkFont(size=16, weight="bold"))
        self.sidebar_label.pack(pady=15)

        # Step labels in the sidebar
        self.step_labels = []
        for i in range(len(self.steps)):
            step_label = ctk.CTkLabel(self.sidebar_frame, text=f"Step {i+1}", font=ctk.CTkFont(size=14))
            step_label.pack(pady=10)
            self.step_labels.append(step_label)

        # Wizard content (header and text)
        self.header_label = ctk.CTkLabel(self.content_frame, text="Wizard Step 1", font=ctk.CTkFont(size=18, weight="bold"))
        self.header_label.pack(pady=15)

        self.content_label = ctk.CTkLabel(self.content_frame, text="", font=ctk.CTkFont(size=14), wraplength=450)
        self.content_label.pack(pady=10)

        # Navigation buttons
        self.button_frame = ctk.CTkFrame(self.content_frame)
        self.button_frame.pack(side="bottom", pady=20, fill="x")

        self.back_button = ctk.CTkButton(self.button_frame, text="Back", command=self.back, state="disabled")
        self.back_button.pack(side="left", padx=10)

        self.next_button = ctk.CTkButton(self.button_frame, text="Next", command=self.next)
        self.next_button.pack(side="right", padx=10)

        # Initialize content and sidebar progress
        self.update_content()

    def update_content(self):
        """Update the content area and sidebar based on the current step."""
        # Update the main content
        self.header_label.configure(text=f"Wizard Step {self.current_step + 1}")
        self.content_label.configure(text=self.steps[self.current_step])

        # Enable or disable back button based on step
        self.back_button.configure(state="normal" if self.current_step > 0 else "disabled")

        # Change Next button to Finish on the last step
        if self.current_step == len(self.steps) - 1:
            self.next_button.configure(text="Finish", command=self.finish)
        else:
            self.next_button.configure(text="Next", command=self.next)

        # Update the sidebar to highlight the current step
        for i, label in enumerate(self.step_labels):
            if i == self.current_step:
                label.configure(text_color="cyan")  # Highlight the current step
            else:
                label.configure(text_color="white")  # Reset others

    def next(self):
        """Proceed to the next step."""
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_content()

    def back(self):
        """Go to the previous step."""
        if self.current_step > 0:
            self.current_step -= 1
            self.update_content()

    def finish(self):
        """Complete the wizard."""
        self.header_label.configure(text="Wizard Complete!")
        self.content_label.configure(text="Thank you for completing the wizard.")
        self.next_button.pack_forget()  # Hide Next/Finish button
        self.back_button.pack_forget()  # Hide Back button


if __name__ == "__main__":
    app = WizardApp()
    app.mainloop()

