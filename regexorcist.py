import re
import tkinter as tk
from tkinter import messagebox, filedialog



# Default file paths and patterns
input_file = ""
output_file = ""
words_to_remove = ["__label__sports"]
regex_to_remove = [r'[^\w\süğıöçŞİĞÜÇÖ\d\s]+']

# Function to process text
def process_text():
    global input_file, output_file
    
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    text = text.replace('*', '* ')

    for word in words_to_remove:
        text = text.replace(word, '')
    for pattern in regex_to_remove:
        text = re.sub(pattern, '', text)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

    word_count = len(text.split())
    messagebox.showinfo("Task Complete", f"The process is complete.\nWord count: {word_count}")


# GUI
root = tk.Tk()
root.title("RegExorcist")

# Set window size
root.geometry("500x200")

# Add word to remove list
def add_word_to_remove():
    word = entry.get()
    if word:
        words_to_remove.append(word)
        entry.delete(0, tk.END)

# Open file dialog for input file selection
def select_input_file():
    global input_file
    input_file = filedialog.askopenfilename()
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file)

# Open file dialog for output file selection
def select_output_file():
    global output_file
    output_file = filedialog.asksaveasfilename()
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_file)

# Input File Entry Widget
input_file_label = tk.Label(root, text="Input File:")
input_file_label.grid(row=0, column=0, padx=10, pady=5)
input_file_entry = tk.Entry(root, width=20)
input_file_entry.grid(row=0, column=1, padx=10, pady=5)
input_file_button = tk.Button(root, text="Browse", command=select_input_file)
input_file_button.grid(row=0, column=2, padx=10, pady=5)

# Output File Entry Widget
output_file_label = tk.Label(root, text="Output File:")
output_file_label.grid(row=1, column=0, padx=10, pady=5)
output_file_entry = tk.Entry(root, width=20)
output_file_entry.grid(row=1, column=1, padx=10, pady=5)
output_file_button = tk.Button(root, text="Browse", command=select_output_file)
output_file_button.grid(row=1, column=2, padx=10, pady=5)

# Text Entry Widget
label = tk.Label(root, text="Add word to remove:")
label.grid(row=2, column=0, padx=10, pady=5)
entry = tk.Entry(root)
entry.grid(row=2, column=1, padx=10, pady=5)

# Button to Add Word to Remove List
add_button = tk.Button(root, text="Add", command=add_word_to_remove)
add_button.grid(row=2, column=2, padx=10, pady=5)

# Button to Process Text
process_button = tk.Button(root, text="Process Text", command=process_text)
process_button.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()
