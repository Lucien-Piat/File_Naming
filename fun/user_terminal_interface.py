import tkinter as tk
from tkinter import ttk

def user_choice(list_original, list_modif):
    current_index = [0]
    output_list = []

    def update_label():
        if current_index[0] < len(list_original):
            label1.config(text=list_original[current_index[0]])
            label2.config(text=list_modif[current_index[0]])

    def ok_clicked():
        if current_index[0] < len(list_original):
            output_list.append(list_modif[current_index[0]])
            current_index[0] += 1
            update_label()
        if current_index[0] == len(list_original):
            root.destroy() 

    def not_ok_clicked():
        if current_index[0] < len(list_original):
            output_list.append(list_original[current_index[0]])
            current_index[0] += 1
            update_label()
        if current_index[0] == len(list_original):
            root.destroy() 

    root = tk.Tk()
    root.title("Message")

    label1 = ttk.Label(root, text="")
    label1.pack(pady=5)

    label2 = ttk.Label(root, text="")
    label2.pack(pady=5)

    ok_button = ttk.Button(root, text="OK", command=ok_clicked)
    ok_button.pack(side='left', padx=5, pady=10)

    not_ok_button = ttk.Button(root, text="Not OK", command=not_ok_clicked)
    not_ok_button.pack(side='right', padx=5, pady=10)

    update_label()  

    root.mainloop()

    return output_list