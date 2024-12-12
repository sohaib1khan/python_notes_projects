import keyboard
import pyperclip
import time

def paste_predefined_text():
    """Paste a predefined text aggressively."""
    predefined_text = "This is the predefined text!"
    pyperclip.copy(predefined_text)
    time.sleep(0.1)  # Ensure clipboard has updated
    keyboard.send("ctrl+v")  # Paste using Ctrl+V
    print("Pasted predefined text into the RDP.")

def copy_and_paste_live_text():
    """Copy the selected text and paste it aggressively into RDP."""
    # Try to copy text aggressively
    max_retries = 5
    for attempt in range(max_retries):
        keyboard.send("ctrl+c")  # Copy selected text
        time.sleep(0.2)  # Allow time for the clipboard to update
        text = pyperclip.paste()  # Get clipboard content
        
        if text:  # Ensure the clipboard is not empty
            print(f"Copied (Attempt {attempt + 1}): {text}")
            break
        print(f"Retrying to copy... (Attempt {attempt + 1})")
    else:
        print("Failed to copy text after multiple attempts.")
        return

    # Paste the copied text aggressively
    print("Pasting the copied text...")
    for _ in range(3):  # Paste multiple times to ensure RDP receives it
        keyboard.send("ctrl+v")  # Paste using Ctrl+V
        time.sleep(0.2)  # Delay between paste actions
    print("Pasted text into the RDP.")

# Register hotkeys
keyboard.add_hotkey("ctrl+1", paste_predefined_text)
keyboard.add_hotkey("ctrl+2", copy_and_paste_live_text)

# Instructions and start the listener
print("Hotkey tool is running...")
print("Press Ctrl+1 to paste predefined text.")
print("Press Ctrl+2 to copy current text and paste it.")
print("Press 'Esc' to exit.")
keyboard.wait("esc")  # Exit on 'Esc'
