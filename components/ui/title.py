import tkinter as tk

class Title:
    def __init__(self, root):
        label = tk.Label(
            root,
            text="Calculator",
            font=("Arial", 18, "bold")
        )
        label.pack(pady=10)
