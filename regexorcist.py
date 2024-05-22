import re
import tkinter as tk
from tkinter import messagebox, filedialog
import customtkinter as ctk
from PIL import Image, ImageTk


# Default file paths and patterns
input_file = ""
output_file = ""
words_to_remove = ["__label__sports"]
regex_to_remove = [r'[^\w\süğıöçŞİĞÜÇÖ\d\s]+']

# State variables for checkboxes
remove_numbers = False
remove_non_letters = False
add_commas = False

def toggle_remove_numbers():
    global remove_numbers
    remove_numbers = not remove_numbers

def toggle_remove_non_letters():
    global remove_non_letters
    remove_non_letters = not remove_non_letters

def toggle_add_commas():
    global add_commas
    add_commas = not add_commas

# Function to process text
def process_text():
    global input_file, output_file
    
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()

    if not input_file:
        messagebox.showwarning("Fill input", "Please specify an input file.")
        return
    elif not output_file:
        messagebox.showwarning("Fill output", "Please specify an output file.")
        return
    
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    for word in words_to_remove:
        text = text.replace(word, '')
    for pattern in regex_to_remove:
        text = re.sub(pattern, '', text)
    if remove_numbers:
        text = re.sub(r'\d', '', text)  # Remove numbers if checkbox is checked
    if remove_non_letters:
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-letter characters if checkbox is checked
    if add_commas:
        words = text.split()
        text = '\n'.join([f"{word}," for word in words])

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

    word_count = len(text.split())
    messagebox.showinfo("Task Complete", f"The process is complete.\nWord count: {word_count}")

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

# Function to open settings window
def open_settings():
    settings_root = tk.Toplevel(root)
    settings_root.title("Settings")

    # this removes the maximize button
    settings_root.resizable(0,0)

    # Calculate the screen width and height
    screen_width = settings_root.winfo_screenwidth()
    screen_height = settings_root.winfo_screenheight()

    # Calculate the x and y coordinates for the center of the screen
    x_coordinate = (screen_width - 400) // 2
    y_coordinate = (screen_height - 100) // 2

    # Set the position of the Tk root window to the center
    settings_root.geometry(f'400x100+{x_coordinate}+{y_coordinate}')
    
    # Checkbox for removing numbers
    remove_numbers_checkbox_var = tk.BooleanVar()
    remove_numbers_checkbox = ctk.CTkCheckBox(
        settings_root,
        text="0-9",
        variable=remove_numbers_checkbox_var,
        command=toggle_remove_numbers,
        text_color=('#252525', '#f4f4f4'),
        border_width=2,
        border_color='#e6e6e6',
        checkbox_height=20,
        checkbox_width=20,
        hover='#fff'
    )
    remove_numbers_checkbox.grid(row=0, column=0, padx=10, pady=5)

    # Checkbox for removing non-letter characters
    remove_non_letters_checkbox_var = tk.BooleanVar()
    remove_non_letters_checkbox = ctk.CTkCheckBox(
        settings_root,
        text="Non-Letters",
        variable=remove_non_letters_checkbox_var,
        command=toggle_remove_non_letters,
        text_color=('#252525', '#f4f4f4'),
        border_width=2,
        border_color='#e6e6e6',
        checkbox_height=20,
        checkbox_width=20,
        hover='#fff'
    )
    remove_non_letters_checkbox.grid(row=0, column=1, padx=20, pady=5)

    # Checkbox for adding commas and new lines
    add_commas_checkbox_var = tk.BooleanVar()
    add_commas_checkbox = ctk.CTkCheckBox(
        settings_root,
        text="CSV",
        variable=add_commas_checkbox_var,
        command=toggle_add_commas,
        text_color=('#252525', '#f4f4f4'),
        border_width=2,
        border_color='#e6e6e6',
        checkbox_height=20,
        checkbox_width=20,
        hover='#fff'
    )
    add_commas_checkbox.grid(row=0, column=2, padx=10, pady=5)

# GUI
root = ctk.CTk()
root.title('')
root.configure(fg_color="#fff")

# this removes the maximize button
root.resizable(0,0)

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the center of the screen
x_coordinate = (screen_width - 400) // 2
y_coordinate = (screen_height - 450) // 2

# Set the position of the Tk root window to the center
root.geometry(f'400x450+{x_coordinate}+{y_coordinate}')



# Load image and create PhotoImage object
logo_image = Image.open("/Users/yasingunaydin/Documents/GitHub/RegExorcist/images/RegExorcist_mac.png")
settings_image = ctk.CTkImage(Image.open("/Users/yasingunaydin/Documents/GitHub/RegExorcist/images/settings.png").resize((20,20)))
process_image = ctk.CTkImage(Image.open("/Users/yasingunaydin/Documents/GitHub/RegExorcist/images/run.png").resize((20,20)))

# Resize image
image_width = 100  # Set your desired width
image_height = 100  # Set your desired height
myImage = logo_image.resize((image_width, image_height))

photo = ImageTk.PhotoImage(myImage)

# Get the background color of the window for logo
window_bg_color = root.cget('bg')



# Display image without border and with matching border color
image_label = tk.Label(root, image=photo, bg=window_bg_color)
image_label.grid(row=1, column=0, columnspan=3, padx=10, pady=0)

# Add label for "RegExorcist" text
regex_label = ctk.CTkLabel(
    root,
    text="RegExorcist",
    text_color=('#252525', '#f4f4f4'),
    font=("Helvetica", 25, "bold")
)
regex_label.grid(row=2, column=0, columnspan=3, padx=10, pady=0)

# Add label for "version" text
version_label = ctk.CTkLabel(
    root,
    text="Version 0.0.3",
    text_color=('#252525', '#f4f4f4'),
    font=("Helvetica", 10)
)
version_label.grid(row=3, column=0, columnspan=3, padx=10, pady=0)

# Input File Entry Widget
input_file_label = ctk.CTkLabel(
    root,
    text="Input File:",
    text_color=('#252525', '#f4f4f4')
)
input_file_label.grid(row=4, column=0, padx=5, pady=5)

input_file_entry = ctk.CTkEntry(
    root,
    width=200,
    fg_color='#fff',
    border_color='#e6e6e6'
)
input_file_entry.grid(row=4, column=1, padx=10, pady=5)

input_file_button = ctk.CTkButton(
    root,
    text="Browse",
    command=select_input_file,
    fg_color=('#e6e6e6', '#3e3f3f'),
    text_color=('#252525', '#f4f4f4'),
    width=50,
    hover='#000'
)
input_file_button.grid(row=4, column=2, padx=10, pady=5)

# Output File Entry Widget
output_file_label = ctk.CTkLabel(
    root,
    text="Output File:",
    text_color=('#252525', '#f4f4f4')
)
output_file_label.grid(row=5, column=0, padx=10, pady=5)

output_file_entry = ctk.CTkEntry(
    root,
    width=200,
    fg_color='#fff',
    border_color='#e6e6e6'
)
output_file_entry.grid(row=5, column=1, padx=10, pady=5)

output_file_button = ctk.CTkButton(
    root,
    text="Browse",
    command=select_output_file,
    fg_color=('#e6e6e6', '#3e3f3f'),
    text_color=('#252525', '#f4f4f4'),
    width=50,
    hover='#000'
)
output_file_button.grid(row=5, column=2, padx=10, pady=5)

# Text Entry Widget
label = ctk.CTkLabel(
    root,
    text="Specific:",
    text_color=('#252525', '#f4f4f4')
)
label.grid(row=6, column=0, padx=10, pady=5)

entry = ctk.CTkEntry(
    root,
    width=200,
    fg_color='#fff',
    border_color='#e6e6e6'
)
entry.grid(row=6, column=1, padx=10, pady=5)

# Button to Add Word to Remove List
add_button = ctk.CTkButton(
    root,
    text="Add",
    command=add_word_to_remove,
    fg_color=('#e6e6e6', '#3e3f3f'),
    text_color=('#252525', '#f4f4f4'),
    width=50,
    hover='#000'
)
add_button.grid(row=6, column=2, padx=10, pady=5)



# Button to Process Text at the bottom
process_button = ctk.CTkButton(
    root,
    image=process_image,
    command=process_text,
    text = '',
    width=20,
    height=35,
    fg_color=('#e6e6e6', '#3e3f3f'),
    hover='#000'
)
process_button.grid(row=9, column=1,columnspan=2, pady=10)

# Add settings button
settings_button = ctk.CTkButton(
    root,
    image=settings_image,
    command=open_settings,
    text = '',
    width=20,
    height=35,
    fg_color=('#e6e6e6', '#3e3f3f'),
    hover='#000'
)
settings_button.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
