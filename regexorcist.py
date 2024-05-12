import re
import tkinter as tk
from tkinter import messagebox, filedialog
import customtkinter as ctk # https://customtkinter.tomschimansky.com/documentation/color



# Default file paths and patterns
input_file = ""
output_file = ""
words_to_remove = ["__label__sports"]
regex_to_remove = [r'[^\w\süğıöçŞİĞÜÇÖ\d\s]+']



def toggle_regex():
    global use_regex
    use_regex = not use_regex

# Default setting for regular expressions
use_regex = True


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

# Function to count words
def count_words():
    input_file = input_file_entry.get()
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    word_count = len(text.split())
    word_count_label.config(text=f"Word count: {word_count}")


# GUI
window = ctk.CTk(fg_color=('#fff', '#222323'))
window.title('RegExorcist')



icon = tk.PhotoImage(file="regexorcistmedium.png")
window.iconphoto(True, icon)



# Calculate the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates for the center of the screen
x_coordinate = (screen_width - 400) // 2  # Assuming width of 500 for the root window
y_coordinate = (screen_height - 500) // 2  # Assuming height of 600 for the root window

# Set the position of the Tk root window to the center
window.geometry(f'400x500+{x_coordinate}+{y_coordinate}')

# Set window size
window.geometry("400x500")

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
input_file_label = ctk.CTkLabel(
    window,
    text="Input File:",
    text_color=('#252525', '#f4f4f4')
    )
input_file_label.grid(row=0, column=0, padx=10, pady=5)
input_file_entry = ctk.CTkEntry(
    window,
    width=150,
    fg_color='#fff',
    border_color='#e6e6e6'
    )
input_file_entry.grid(row=0, column=1, padx=10, pady=5)
input_file_button = ctk.CTkButton(
    window,
    text="Browse",
    command=select_input_file,
    fg_color=('#e6e6e6', '#3e3f3f'),
    text_color=('#252525', '#f4f4f4'),
    width=50,
    hover='#000'
    )
input_file_button.grid(row=0, column=2, padx=10, pady=5)

# Output File Entry Widget
output_file_label = ctk.CTkLabel(
    window,
    text="Output File:",
    text_color=('#252525', '#f4f4f4')
    )
output_file_label.grid(row=1, column=0, padx=10, pady=5)
output_file_entry = ctk.CTkEntry(
    window,
    width=150,
    fg_color='#fff',
    border_color='#e6e6e6'
    )
output_file_entry.grid(row=1, column=1, padx=10, pady=5)
output_file_button = ctk.CTkButton(
    window,
    text="Browse",
    command=select_output_file,
    fg_color=('#e6e6e6', '#3e3f3f'),
    text_color=('#252525', '#f4f4f4'),
    width=50,
    hover='#000'
    )
output_file_button.grid(row=1, column=2, padx=10, pady=5)

# Text Entry Widget
label = ctk.CTkLabel(
    window,
    text="Add word:",
    text_color=('#252525', '#f4f4f4')
    )
label.grid(row=2, column=0, padx=10, pady=5)
entry = ctk.CTkEntry(
window,
width=150,
fg_color='#fff',
border_color='#e6e6e6'
)
entry.grid(row=2, column=1, padx=10, pady=5)

# Button to Add Word to Remove List
add_button = ctk.CTkButton(
    window,
    text="Add",
    command=add_word_to_remove,
    fg_color=('#e6e6e6', '#3e3f3f'),
    text_color=('#252525', '#f4f4f4'),
    width=50,
    hover='#000'
    )
add_button.grid(row=2, column=2, padx=10, pady=5)

# Checkbox for Regular Expressions
regex_checkbox_var = tk.BooleanVar()
regex_checkbox = ctk.CTkCheckBox(
    window, 
    text="Remove Regular Expressions", 
    variable=regex_checkbox_var, 
    command=toggle_regex,
    text_color=('#252525', '#f4f4f4'),
    border_width=2,
    border_color='#e6e6e6',
    checkbox_height=20,
    checkbox_width=20,
    hover='#fff'
)
regex_checkbox.grid(row=3, column=1, padx=10, pady=5)

# Button to Process Text
process_button = ctk.CTkButton(
    window,
    text="Process Text",
    command=process_text,
    fg_color=('#e6e6e6', '#3e3f3f'),
    text_color=('#252525', '#f4f4f4'),
    hover='#000'
)
process_button.grid(row=4, column=1, padx=10, pady=5)

# Button to Count Words
count_button = ctk.CTkButton(
    window,
    text="Count Words",
    command=count_words,
    fg_color=('#e6e6e6', '#3e3f3f'),
    text_color=('#252525', '#f4f4f4'),
    hover='#000'
)
count_button.grid(row=5, column=1, padx=10, pady=5)

# Label to display word count
word_count_label = ctk.CTkLabel(
    window,
    text="Word count: ",
    text_color=('#252525', '#f4f4f4')
)
word_count_label.grid(row=6, column=1, padx=10, pady=5)

window.mainloop()
