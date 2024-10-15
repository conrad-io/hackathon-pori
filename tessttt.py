import subprocess
import tkinter as tk
from tkinter import messagebox
import gitlab

# Function to run the Git command with user-provided credentials
def git_clone():
    username = username_entry.get()
    password = password_entry.get()
    repo_url = repo_entry.get()

    if not username or not password or not repo_url:
        messagebox.showerror("Error", "All fields must be filled!")
        return

    # Create the command for cloning with embedded credentials
    clone_command = f"git clone https://{username}:{password}@{repo_url}"

    try:
        result = subprocess.run(clone_command, shell=True, check=True, capture_output=True, text=True)
        messagebox.showinfo("Success", "Repository cloned successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to clone repo: {e.output}")

# Create the Tkinter window
root = tk.Tk()
root.title("Git Login")

# Username input
tk.Label(root, text="Git Username").grid(row=0, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

# Password input
tk.Label(root, text="Git Password/Token").grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Repo URL input
tk.Label(root, text="Repo URL (without https)").grid(row=2, column=0)
repo_entry = tk.Entry(root)
repo_entry.grid(row=2, column=1)

# Clone button
clone_button = tk.Button(root, text="Clone Repository", command=git_clone)
clone_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
