import tkinter as tk

class Buttons:
    def __init__(self, root, on_click):
        frame = tk.Frame(root)
        frame.pack(expand=True)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"],
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = tk.Button(
                    frame,
                    text=text,
                    font=("Arial", 14),
                    width=5,
                    height=2,
                    command=lambda t=text: on_click(t)
                )
                btn.grid(row=r, column=c, padx=5, pady=5)
