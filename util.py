import tkinter as tk
from tkinter import messagebox

def get_button(window, text, color, command, fg='White'):
    button = tk.Button(window, text=text, bg=color, fg=fg, command=command, activebackground='black', activeforeground='white')
    button.config(font=("Arial", 12), width=20, height=2)
    return button

def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label

def get_txt_label(window, text):
    label = tk.Label(window, text=text)
    label.config(font=("Arial", 12), fg='Black', justify='left')
    return label

def get_entry_text(window):
    inputtxt = tk.Text(window,height=2,width=15,font=("Arail", 32))
    return inputtxt

def msg_box(title, description):
    messagebox.showinfo(title, description)
    
    
    
    