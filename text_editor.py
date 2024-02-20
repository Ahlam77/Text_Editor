import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file and display its contents in the text editor."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    
    window.title(f'AhlamTextEditor - {filepath}')

def save_file():
    """Save the contents of the text editor into a file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    
    window.title(f'AhlamTextEditor - {filepath}')

def create_widgets():
    window = tk.Tk()
    window.title("Ahlam Text Editor")
    window.rowconfigure(0, minsize=600)
    window.columnconfigure(1, minsize=800)

    txt_edit = tk.Text(window)
    # Change background and text color here
    txt_edit.configure(bg='light gray', fg='black')  # Example: light gray background, black text

    frame_buttons = tk.Frame(window, relief=tk.RAISED)
    btn_open = tk.Button(frame_buttons, text="Open File", command=open_file)
    btn_save = tk.Button(frame_buttons, text="Save As", command=save_file)

    btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(column=0, row=1, sticky="ew", padx=5)

    frame_buttons.grid(column=0, row=0, sticky="ns")
    txt_edit.grid(column=1, row=0, sticky="nsew")

    return window, txt_edit

def main():
    window, txt_edit = create_widgets()
    window.mainloop()

if __name__ == "__main__":
    main()
