import tkinter as tk
import subprocess

def execute_command():
    # Den eingegebenen Befehl aus dem Eingabefeld holen
    command = entry.get()
    try:
        # Den Befehl mit subprocess ausführen und das Ergebnis erfassen
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        result_label.config(text=output)  # Ergebnis anzeigen
    except subprocess.CalledProcessError as e:
        # Fehlerfall: Fehlerausgabe anzeigen
        result_label.config(text=f"Error: {e.output}")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Command Executor")

# Eingabefeld für den Befehl
entry_label = tk.Label(root, text="Enter your command:")
entry_label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

# Button zum Ausführen des Befehls
execute_button = tk.Button(root, text="Execute", command=execute_command)
execute_button.pack()

# Label, um das Ergebnis anzuzeigen
result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack()

# GUI ausführen
root.mainloop()
