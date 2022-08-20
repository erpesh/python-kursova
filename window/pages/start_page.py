import tkinter as tk
from tkinter import ttk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Виберіть метод")

        # putting the grid in its place by using grid
        label.grid(row=1, column=0, padx=2, pady=10)

        # buttons for choosing solve method
        checkbox = tk.Button(self, text="Метод Ньютона", command=lambda: controller.show_frame(1))
        checkbox.grid(row=2, column=0, columnspan=3, padx=2, pady=5)
        checkbox2 = tk.Button(self, text="Метод січних", command=lambda: controller.show_frame(2))
        checkbox2.grid(row=3, column=0, columnspan=3, padx=2, pady=5)
