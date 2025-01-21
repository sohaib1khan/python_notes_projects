import tkinter as tk
from tkinter import messagebox
import pyperclip
import time

class RDPHelperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RDP Helper App")
        self.root.geometry("600x400")
        self.root.configure(bg="#f5f5f5")
        
        # Predefined Text
        self.predefined_text = "This is the predefined text!"
        tk.Label(root, text="Predefined Text:", bg="#f5f5f5", font=("Arial", 12, "bold")).pack(pady=(10, 5))
        self.predefined_display = tk.Text(root, height=3, wrap="word", bg="white", font=("Arial", 12))
        self.predefined_display.insert("1.0", self.predefined_text)
        self.predefined_display.config(state="disabled")
        self.predefined_display.pack(padx=10, pady=(0, 10), fill="x")
        
        # Copy Predefined Text Button
        self.copy_predefined_btn = tk.Button(root, text="Copy Predefined Text", command=self.copy_predefined_text, bg="#d1e7dd", font=("Arial", 12))
        self.copy_predefined_btn.pack(pady=5)
        
        # Live Copy Section
        tk.Label(root, text="Live Copied Text:", bg="#f5f5f5", font=("Arial", 12, "bold")).pack(pady=(10, 5))
        self.live_copy_display = tk.Text(root, height=3, wrap="word", bg="white", font=("Arial", 12))
        self.live_copy_display.config(state="disabled")
        self.live_copy_display.pack(padx=10, pady=(0, 10), fill="x")
        
        # Copy and Paste Live Text Button
        self.copy_paste_live_btn = tk.Button(root, text="Copy & Paste Live Text", command=self.copy_and_paste_live_text, bg="#d1e7dd", font=("Arial", 12))
        self.copy_paste_live_btn.pack(pady=5)
        
        # Exit Button
        self.exit_btn = tk.Button(root, text="Exit Application", command=self.root.quit, bg="#d1e7dd", font=("Arial", 12))
        self.exit_btn.pack(pady=20)

    def copy_predefined_text(self):
        """Copy predefined text to clipboard."""
        pyperclip.copy(self.predefined_text)
        messagebox.showinfo("Success", "Predefined text copied!")

    def copy_and_paste_live_text(self):
        """Copy live text and aggressively paste it."""
        pyperclip.copy("")  # Clear clipboard
        time.sleep(0.5)  # Ensure clipboard updates
        live_text = "Live text from clipboard"
        pyperclip.copy(live_text)
        self.live_copy_display.config(state="normal")
        self.live_copy_display.delete("1.0", "end")
        self.live_copy_display.insert("1.0", live_text)
        self.live_copy_display.config(state="disabled")
        messagebox.showinfo("Success", "Live text copied and pasted!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RDPHelperApp(root)
    root.mainloop()
