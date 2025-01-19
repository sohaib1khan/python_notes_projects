import tkinter as tk
from tkinter import messagebox, ttk
import pyperclip
import time
import keyboard  # Library to simulate typing

class TextCopyDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Copy Dashboard")

        self.text_status = tk.StringVar()
        self.text_status.set("No text copied yet.")

        self.retry_count = tk.IntVar()
        self.retry_count.set(3)

        # Frame for predefined text
        predefined_frame = ttk.LabelFrame(root, text="Predefined Text")
        predefined_frame.pack(padx=10, pady=10, fill="x")

        self.predefined_texts = ["Sample Path 1", "Sample Path 2"]
        self.text_listbox = tk.Listbox(predefined_frame, height=4)
        for text in self.predefined_texts:
            self.text_listbox.insert(tk.END, text)
        self.text_listbox.pack(side="left", padx=5, pady=5)

        copy_button = ttk.Button(predefined_frame, text="Copy Selected Text", command=self.copy_predefined_text)
        copy_button.pack(side="right", padx=5, pady=5)

        type_button = ttk.Button(predefined_frame, text="Type Selected Text", command=self.type_predefined_text)
        type_button.pack(side="right", padx=5, pady=5)

        # Frame for custom text
        custom_frame = ttk.LabelFrame(root, text="Custom Text")
        custom_frame.pack(padx=10, pady=10, fill="x")

        self.custom_text_entry = ttk.Entry(custom_frame)
        self.custom_text_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        custom_copy_button = ttk.Button(custom_frame, text="Copy Custom Text", command=self.copy_custom_text)
        custom_copy_button.pack(side="right", padx=5, pady=5)

        custom_type_button = ttk.Button(custom_frame, text="Type Custom Text", command=self.type_custom_text)
        custom_type_button.pack(side="right", padx=5, pady=5)

        # Frame for retry settings
        retry_frame = ttk.LabelFrame(root, text="Retry Settings")
        retry_frame.pack(padx=10, pady=10, fill="x")

        retry_label = ttk.Label(retry_frame, text="Retries:")
        retry_label.pack(side="left", padx=5, pady=5)

        retry_spinbox = ttk.Spinbox(retry_frame, from_=1, to=10, textvariable=self.retry_count, width=5)
        retry_spinbox.pack(side="left", padx=5, pady=5)

        # Status display
        status_frame = ttk.LabelFrame(root, text="Status")
        status_frame.pack(padx=10, pady=10, fill="x")

        self.status_label = ttk.Label(status_frame, textvariable=self.text_status)
        self.status_label.pack(padx=5, pady=5)

        # Exit button
        exit_button = ttk.Button(root, text="Exit", command=self.root.quit)
        exit_button.pack(pady=10)

    def copy_predefined_text(self):
        selected = self.text_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a predefined text.")
            return
        text = self.predefined_texts[selected[0]]
        self.copy_text_to_clipboard(text)

    def type_predefined_text(self):
        selected = self.text_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a predefined text.")
            return
        text = self.predefined_texts[selected[0]]
        self.simulate_typing(text)

    def copy_custom_text(self):
        text = self.custom_text_entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter custom text to copy.")
            return
        self.copy_text_to_clipboard(text)

    def type_custom_text(self):
        text = self.custom_text_entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter custom text to type.")
            return
        self.simulate_typing(text)

    def copy_text_to_clipboard(self, text):
        retries = self.retry_count.get()
        for attempt in range(retries):
            pyperclip.copy(text)
            time.sleep(0.5)  # Wait for clipboard to update
            copied_text = pyperclip.paste()
            if copied_text == text:
                self.text_status.set(f"Text copied successfully on attempt {attempt + 1}: {text}")
                return
        self.text_status.set("Failed to copy text after multiple attempts.")
        messagebox.showerror("Error", "Failed to copy text after multiple attempts.")

    def simulate_typing(self, text):
        for char in text:
            keyboard.write(char)
            time.sleep(0.05)  # Adjust the delay for typing speed
        self.text_status.set(f"Text typed successfully: {text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextCopyDashboard(root)
    root.mainloop()
