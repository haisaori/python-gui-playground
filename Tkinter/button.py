import tkinter as tk 
from tkinter import ttk

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# button
def func_button():
    print('a basic button')
    print(radio_var.get())
button_string = tk.StringVar(value='A button with string var')
button = ttk.Button(window, text='A Simple Button', command=func_button, textvariable=button_string)
button.pack()

# checkbutton
check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(
    window, 
    text='Checkbox 1',
    command= lambda: print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5
    )
check.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'RadioButton 1',
    value='radio 1',
    variable=radio_var,
    command=lambda: print(radio_var.get())
    )
radio1.pack()
radio2 = ttk.Radiobutton(
    window,
    text='RadioButton 2',
    value=2,
    variable=radio_var
    )
radio2.pack()

# run
window.mainloop()