import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")

        self.selected_path = tk.StringVar()
        self.selected_path.set("Selected Path: ")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="File Manager").pack()

        tk.Label(self.root, textvariable=self.selected_path).pack()

        tk.Button(self.root, text="Create File", command=self.create_file).pack()
        tk.Button(self.root, text="Create Folder", command=self.create_folder).pack()
        tk.Button(self.root, text="Remove File", command=self.remove_file).pack()
        tk.Button(self.root, text="Remove Folder", command=self.remove_folder).pack()
        tk.Button(self.root, text="Read File", command=self.read_file).pack()
        tk.Button(self.root, text="Rename File", command=self.rename_file).pack()
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

    def update_selected_path(self, path):
        self.selected_path.set(f"Selected Path: {path}")

    def create_file(self):
        file_name = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_name:
            notes = simpledialog.askstring("File Notes", "Enter some notes for the file:")
            with open(file_name, 'w') as file:
                file.write(notes)
            self.update_selected_path(file_name)
            messagebox.showinfo("Success", f"File '{file_name}' created")

    def create_folder(self):
        folder_name = simpledialog.askstring("Create Folder", "Enter folder name:")
        if folder_name:
            selected_directory = filedialog.askdirectory()
            if selected_directory:
                folder_path = os.path.join(selected_directory, folder_name)
                try:
                    os.makedirs(folder_path)
                    self.update_selected_path(os.path.abspath(folder_path))
                    messagebox.showinfo("Success", f"Folder '{folder_name}' created")
                except OSError as e:
                    messagebox.showerror("Error", f"Error creating folder: {e}")

    def remove_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            os.remove(file_path)
            self.update_selected_path(file_path)
            messagebox.showinfo("Success", f"File '{file_path}' removed")

    def remove_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            os.rmdir(folder_path)
            self.update_selected_path(folder_path)
            messagebox.showinfo("Success", f"Folder '{folder_path}' removed")

    def read_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                contents = file.read()
            self.update_selected_path(file_path)
            messagebox.showinfo("File Contents", f"Contents:\n{contents}")

    def rename_file(self):
        old_path = filedialog.askopenfilename()
        if old_path:
            new_name = simpledialog.askstring("Rename File", "Enter new name:")
            if new_name:
                new_path = os.path.join(os.path.dirname(old_path), new_name)
                os.rename(old_path, new_path)
                self.update_selected_path(new_path)
                messagebox.showinfo("Success", f"File renamed to '{new_name}'")

    def main(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    app = GUIApp(root)
    app.main()

if __name__ == "__main__":
    main()
