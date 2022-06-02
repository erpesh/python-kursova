import tkinter as tk
from tkinter import ttk


class PageSecant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.number_of_inputs = 2
        self.answer = None

        label = ttk.Label(self, text="Secant method")
        label.grid(row=0, column=0, columnspan=3, padx=2, pady=10)

