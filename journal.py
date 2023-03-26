import tkinter as tk
import csv
import time
from tkinter import messagebox


class JournalApp:

    def __init__(self, master):
        self.master = master
        master.title("DIJO - The Journal App")

        # Define the entry prompt
        tk.Label(master, text="Enter a journal entry:", font=("Arial", 12, "bold")).pack()

        # Create the entry field and set focus on it
        self.entry = tk.Entry(master, width=50, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.focus()

        # Define the entry prompt
        tk.Label(master, text="Journal Logs:", font=("Arial", 12, "bold")).pack()

        # Create the display area
        self.display = tk.Text(master, height=20, width=60, font=("Arial", 12))
        self.display.pack(pady=10)

        # Load existing entries from the CSV file
        with open('journal_entries.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for log_type, log_text, log_time in reader:
                formatted_time = time.strftime('%b %d, %Y %I:%M %p', time.strptime(log_time, '%Y-%m-%d %H:%M:%S'))
                tag = f'[{log_type.upper()}]' if log_type in ['n', 't', 'e', 'd'] else ''
                log_entry = f'{tag} - {formatted_time} - {log_text}'
                self.display.insert(tk.END, log_entry + "\n")

        # Bind the enter key to the submit_entry function
        self.master.bind('<Return>', self.submit_entry)

    def submit_entry(self, event=None):
        # Get the text from the entry field and clear it
        entry_text = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        # Check if the text starts with n, t, e, or d
        if entry_text and entry_text[0].lower() in ['n', 't', 'e', 'd']:
            log_type = entry_text[0].lower()
            log_text = entry_text[1:].strip()
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

            # Add the new entry to the display area
            tag = f'[{log_type.upper()}]'
            log_entry = f'{tag} - {time.strftime("%b %d, %Y %I:%M %p", time.localtime())} - {log_text}'
            self.display.insert(tk.END, log_entry + "\n")

            # Add the new entry to the CSV file
            with open('journal_entries.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([log_type, log_text, timestamp])

        else:
            # Show an error message if the input is invalid
            tk.messagebox.showerror("Invalid Input", "Please start your entry with n, t, e, or d.")


# Start the GUI
root = tk.Tk()
app = JournalApp(root)
root.mainloop()
