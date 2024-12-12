import keyboard
import pyperclip
import time

def paste_predefined_text():
    """Paste predefined text into RDP."""
    predefined_text = "This is the predefined text!"
    pyperclip.copy(predefined_text)
    time.sleep(0.2)  # Ensure clipboard updates
    print(f"Pasting predefined text: {predefined_text}")
    for _ in range(5):  # Paste multiple times for reliability
        keyboard.send("ctrl+v")
        time.sleep(0.5)

def copy_and_paste_live_text():
    """Copy text and paste it aggressively into RDP."""
    max_retries = 5
    copied_text = ""

    # Aggressive copying
    for attempt in range(max_retries):
        keyboard.send("ctrl+c")  # Copy selected text
        time.sleep(0.5)  # Wait for clipboard to update
        copied_text = pyperclip.paste()
        if copied_text:
            print(f"Copied text (Attempt {attempt + 1}): {copied_text}")
            break
    else:
        print("Failed to copy text after multiple attempts.")
        return

    # Aggressive pasting
    print("Pasting copied text...")
    for _ in range(5):  # Paste multiple times for reliability
        keyboard.send("ctrl+v")
        time.sleep(0.5)

def paste_hardcoded_text_1():
    """Manually paste hardcoded text #1."""
    hardcoded_text = "Hardcoded Text 1: Example of a manual entry."
    pyperclip.copy(hardcoded_text)
    time.sleep(0.2)  # Ensure clipboard updates
    print(f"Pasting hardcoded text #1: {hardcoded_text}")
    for _ in range(5):
        keyboard.send("ctrl+v")
        time.sleep(0.5)

def paste_hardcoded_text_2():
    """Manually paste hardcoded text #2."""
    hardcoded_text = "Hardcoded Text 2: Another manual entry for testing."
    pyperclip.copy(hardcoded_text)
    time.sleep(0.2)  # Ensure clipboard updates
    print(f"Pasting hardcoded text #2: {hardcoded_text}")
    for _ in range(5):
        keyboard.send("ctrl+v")
        time.sleep(0.5)

# Register hotkeys
keyboard.add_hotkey("ctrl+1", paste_predefined_text)
keyboard.add_hotkey("ctrl+2", copy_and_paste_live_text)
keyboard.add_hotkey("ctrl+3", paste_hardcoded_text_1)
keyboard.add_hotkey("ctrl+4", paste_hardcoded_text_2)

# Start the listener
print("Hotkey tool is running...")
print("Press Ctrl+1 to paste predefined text.")
print("Press Ctrl+2 to copy current text and paste it.")
print("Press Ctrl+3 to paste hardcoded text #1.")
print("Press Ctrl+4 to paste hardcoded text #2.")
print("Press 'Esc' to exit.")
keyboard.wait("esc")  # Exit on 'Esc'
