import tkinter as tk
from tkinter import ttk


class PageSecant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2")
        label.grid(row=0, column=4, padx=2, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1")
                             # command=lambda: controller.show_frame(PageNewton))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=2, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage")
                             # command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=2, pady=10)
