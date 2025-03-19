import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
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
root.geometry("450x250")

font = ("Helvetica", 11)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = ttk.Frame(root, padding="5")
frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=5)

label = ttk.Label(frame, text="Select an option:", font=font, anchor="center")
label.grid(row=0, column=0, pady=10, columnspan=2)

style = ttk.Style() 
style.configure("TButton",
                padding= [5,10] ,
                relief="raised",
                font = font,
                width=20)

# Add buttons with better spacing
button1 = ttk.Button(frame, text="📄 Load a file", command=process_file, style="TButton")
button1.grid(row=1, column=0, pady=5, padx=10, sticky="ew")


button2 = ttk.Button(frame, text="📂 Load a folder", command=process_folder, style="TButton")
button2.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

frame2 = ttk.Frame(root, padding="5")
frame2.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)  

# Add an exit button with a different color
exit_button = ttk.Button(frame2, text="Exit", command=root.quit, style="TButton", width=10)
exit_button.grid(row=0, column=0, pady=20, padx=10, sticky="ew", columnspan=2)
frame2.grid_columnconfigure(0, weight=1)

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)

root.mainloop()
