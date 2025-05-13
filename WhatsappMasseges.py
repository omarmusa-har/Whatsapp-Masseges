import tkinter as tk
from tkinter import messagebox
import pywhatkit
import time

def send_to_all_repeated():
    numbers = numbers_text.get("1.0", tk.END).strip().splitlines()
    message = msg_entry.get("1.0", tk.END).strip()

    try:
        repeat_count = int(count_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Repeat count must be an integer.")
        return

    if not message:
        messagebox.showerror("Error", "Message is empty!")
        return

    success = 0
    fail = 0

    for num in numbers:
        num = num.strip()
        if not num.startswith("+") or len(num) < 10:
            continue

        for i in range(repeat_count):
            try:
                # Send the message instantly
                if i == 0:  # Open WhatsApp Web only for the first send
                    pywhatkit.sendwhatmsg_instantly(num, message, wait_time=15, tab_close=True)
                    time.sleep(5)
                else:
                    pywhatkit.sendwhatmsg_instantly(num, message, wait_time=15, tab_close=True)
                    time.sleep(5)
                success += 1
            except Exception as e:
                print(f"Error sending to {num}: {e}")
                fail += 1
                break

    # Show result
    result_label.config(text=f"Sent: {success} messages\nFailed: {fail}", fg="green")

# GUI setup
root = tk.Tk()
root.title("Bulk WhatsApp Message Sender")
root.geometry("500x550")

tk.Label(root, text="Phone numbers (with country code - one per line):").pack()
numbers_text = tk.Text(root, height=10, width=50)
numbers_text.pack()

tk.Label(root, text="Message:").pack()
msg_entry = tk.Text(root, height=5, width=50)
msg_entry.pack()

tk.Label(root, text="Repeat count per number:").pack()
count_entry = tk.Entry(root, width=10)
count_entry.pack()

tk.Button(root, text="Send", command=send_to_all_repeated).pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
