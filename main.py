import tkinter as tk
from components.layout import AppLayout

def main():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("380x420")
    root.resizable(False, False)

    AppLayout(root)

    root.mainloop()

if __name__ == "__main__":
    main()
