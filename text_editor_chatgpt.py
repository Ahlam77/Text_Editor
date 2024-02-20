import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            editor.delete('1.0', tk.END)
            editor.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(editor.get('1.0', tk.END))

# Create the root window
root = tk.Tk()
root.title("Ahlam Text Editor")

# Text area for editing
editor = tk.Text(root, wrap="word")
editor.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Function buttons (Open and Save)
open_button = tk.Button(root, text="Open", command=open_file)
open_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

save_button = tk.Button(root, text="Save", command=save_file)
save_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Configure grid weights to allow text area expansion
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Run the application
root.mainloop()
