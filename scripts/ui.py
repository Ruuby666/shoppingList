import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# Function to find a file in the current folder and subfolders
def find_file(filename):
    current_directory = os.getcwd()  # Get the current directory
    for root, dirs, files in os.walk(current_directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Function to process a single file
def process_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        run_ticket_reader([file_path])

# Function to process a folder
def process_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        ticket_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.startswith("ticket") and f.endswith(".txt")]
        if ticket_files:
            run_ticket_reader(ticket_files)
        else:
            messagebox.showwarning("Warning", "No ticket files were found in the selected folder.") 

# It will search for ticket_reader.py in the current directory and subdirectories
def run_ticket_reader(ticket_files):
    ticket_reader_file = find_file("ticket_reader.py")
    if ticket_reader_file:
        try:
            subprocess.run(["python", ticket_reader_file, *ticket_files], check=True)
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "An error occurred while running ticket_reader.py")
    else:
        messagebox.showerror("Error", "ticket_reader.py file not found.")

# Create the Tkinter interface
root = tk.Tk()
root.title("Ticket Manager")
root.geometry("400x200")

tk.Label(root, text="Select an option:", font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="📄 Load a file", command=process_file, width=30).pack(pady=5)
tk.Button(root, text="📂 Load a folder", command=process_folder, width=30).pack(pady=5)

tk.Button(root, text="Exit", command=root.quit, width=30).pack(pady=20)

root.mainloop()

