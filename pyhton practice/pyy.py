import tkinter as tk
from tkinter import messagebox
import math

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to add characters to the entry widget
def add_to_entry(char):
    entry.insert(tk.END, char)

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Advanced calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Cannot compute square root of a negative number!"
    return math.sqrt(x)

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Invalid input for logarithm!"
    return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Cannot compute factorial of a negative number!"
    if x == 0:
        return 1
    return x * factorial(x - 1)

# Function to create the GUI calculator
def create_calculator():
    root = tk.Tk()
    root.title("Calculator")

    # Entry widget to display and input expression
    global entry
    entry = tk.Entry(root, width=30, font=("Arial", 14), justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Buttons for numbers and operations
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]
    row = 1
    col = 0
    for button in buttons:
        tk.Button(root, text=button, width=5, height=2, font=("Arial", 12),
                  command=lambda char=button: add_to_entry(char)).grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Button to clear the entry
    tk.Button(root, text="C", width=5, height=2, font=("Arial", 12), command=clear_entry).grid(row=row, column=0, padx=5, pady=5)

    # Button to evaluate the expression
    tk.Button(root, text="=", width=5, height=2, font=("Arial", 12), command=evaluate_expression).grid(row=row, column=1, columnspan=3, padx=5, pady=5)

    root.mainloop()

# Create the calculator GUI
create_calculator()
