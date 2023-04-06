import tkinter as tk 
from tkinter import ttk

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# button
def func_button():
    print('a basic button')
button_string = tk.StringVar(value='A button with string var')
button = ttk.Button(window, text='A Simple Button', command=func_button, textvariable=button_string)
button.pack()

# run
window.mainloop()