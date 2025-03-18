import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def process_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        run_ticket_reader([file_path])

def process_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        ticket_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.startswith("ticket") and f.endswith(".txt")]
        if ticket_files:
            run_ticket_reader(ticket_files)
        else:
            messagebox.showwarning("Advertencia", "No se encontraron archivos de tickets en la carpeta seleccionada.")

def run_ticket_reader(ticket_files):
    try:
        subprocess.run(["python", "ticket_reader.py", *ticket_files], check=True)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Ocurrió un error al ejecutar ticket_reader.py")

# Crear la interfaz
root = tk.Tk()
root.title("Gestor de Tickets")
root.geometry("400x200")

tk.Label(root, text="Seleccione una opción:", font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="📄 Cargar un archivo", command=process_file, width=30).pack(pady=5)
tk.Button(root, text="📂 Cargar una carpeta", command=process_folder, width=30).pack(pady=5)

tk.Button(root, text="Salir", command=root.quit, width=30).pack(pady=20)

root.mainloop()
