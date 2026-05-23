import tkinter as tk
from tkinter import messagebox

def get_button(window, text, color, command, fg='White'):
    button = tk.Button(window, text=text, bg=color, fg=fg, command=command, activebackground='#555555', activeforeground='#FFFFFF')
    button.config(font=("Arial", 12, "bold"), width=20, height=1)
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
    inputtxt = tk.Text(window,height=1,width=15,font=("Arail", 12))
    return inputtxt

def msg_box(title, description):
    messagebox.showinfo(title, description)
    
    
    
    
