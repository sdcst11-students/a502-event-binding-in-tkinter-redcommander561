#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

import tkinter as tk
from math import sqrt

def calculate_hypotenuse():
    side1 = float(s1_entry.get())
    side2 = float(s2_entry.get())
    
    
    hypotenuse = sqrt(side1**2 + side2**2)

    
    result_entry.delete(0, tk.END)
    result_entry.insert(0, f"Hypotenuse: {hypotenuse:.2f}")


app = tk.Tk()
app.title("Right Triangle Hypotenuse Calculator")


s1label = tk.Label(app, text="Enter side 1:")
s1label.grid(row=0, column=0, padx=10, pady=10)
s1_entry = tk.Entry(app)
s1_entry.grid(row=0, column=1, padx=10, pady=10)

s2_label = tk.Label(app, text="Enter side 2:")
s2_label.grid(row=1, column=0, padx=10, pady=10)
s2_entry = tk.Entry(app)
s2_entry.grid(row=1, column=1, padx=10, pady=10)


calculate = tk.Button(app, text="Calculate Hypotenuse", command=calculate_hypotenuse)
calculate.grid(row=2, column=0, columnspan=2, pady=10)


result_entry = tk.Entry(app, width=30)
result_entry.grid(row=3, column=0, columnspan=2, pady=10)


app.mainloop()