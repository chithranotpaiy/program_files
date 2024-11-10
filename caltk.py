import tkinter as tk

def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create entry widget for displaying input and output
entry = tk.Entry(root, width=15, borderwidth=3)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '00', '.', '/',
    'C', '='
]

# Create and place buttons on the grid
row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=10, command=calculate).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button == 'C':
        tk.Button(root, text=button, width=10, command=clear).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=10, command=lambda char=button: button_click(char)).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
