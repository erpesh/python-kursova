import tkinter as tk
from tkinter import ttk

from window.pages.page_newton import PageNewton
from window.pages.page_secant import PageSecant


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Choose method")

        # putting the grid in its place by using grid
        label.grid(row=1, column=0, padx=2, pady=10)
        # checkbox for choosing solve method
        var_radio = tk.IntVar()

        checkbox = tk.Radiobutton(self, text="Newton method", variable=var_radio, value=0)
        checkbox.grid(row=2, column=0, columnspan=3, padx=2, pady=5)
        checkbox2 = tk.Radiobutton(self, text="Secant method", variable=var_radio, value=1)
        checkbox2.grid(row=3, column=0, columnspan=3, padx=2, pady=5)

        submit_method = ttk.Button(self, text="Submit", command=lambda: controller.show_frame(
            PageNewton if var_radio.get() == 0 else PageSecant))
        submit_method.grid(row=4, column=0, columnspan=3, padx=2, pady=5)

