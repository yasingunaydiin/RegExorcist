import re
import tkinter as tk
from tkinter import messagebox

# Defines file paths and patterns
input_file = "/Users/yasingunaydin/Downloads/TS_TimeLine_News_Category_Split_Dataset-/sports_843648_lines.txt"
output_file = "/Users/yasingunaydin/Downloads/TS_TimeLine_News_Category_Split_Dataset-/sports_843648_lines-.txt"
words_to_remove = ["__label__sports"]
regex_to_remove = [r'[^\w\süğıöçŞİĞÜÇÖ\d\s]+']

# Reads the input file
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Adds a space after each asterisk - IF NEEDED
text = text.replace('*', '* ')

# Removes words and patterns from the text
for word in words_to_remove:
    text = text.replace(word, '')
for pattern in regex_to_remove:
    text = re.sub(pattern, '', text)

# Writes the cleaned text to the output file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(text)


# Counts words
word_count = len(text.split())

# Shows message box to indicate completion
root = tk.Tk()
root.withdraw()  # Hide the main window
messagebox.showinfo("Task Complete", "The process is complete.\nWord count: {}".format(word_count))