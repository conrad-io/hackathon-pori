import tkinter as tk
import subprocess
import threading

def execute_command():
    command = entry.get()
    
    def run_command():
        # Erzeuge den Prozess und leite stdout und stderr zusammen
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        # Kontinuierlich die Ausgabe lesen und im Label aktualisieren
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                # Ausgaben sammeln
                current_text = result_label.cget("text")
                result_label.config(text=current_text + output)

    # Den Befehl in einem neuen Thread ausführen
    thread = threading.Thread(target=run_command)
    thread.start()

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
