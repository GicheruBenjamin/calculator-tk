import tkinter as tk

class Display:
    def __init__(self, root):
        self.var = tk.StringVar()

        entry = tk.Entry(
            root,
            textvariable=self.var,
            font=("Arial", 20),
            justify="right",
            bd=8
        )
        entry.pack(fill="x", padx=10, pady=10)

    def update(self, value):
        self.var.set(value)
