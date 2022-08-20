import tkinter as tk
from tkinter import ttk


class MethodPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    def update_widgets(self):
        self.init_nums.grid(row=self.number_of_inputs + 3, column=1, padx=2, pady=10)
        self.initial_nums_label.grid(row=self.number_of_inputs + 3, column=0, padx=2, pady=10)
        self.variables_label.grid(row=self.number_of_inputs + 3, column=2, padx=2, pady=10)
        self.variables_entry.grid(row=self.number_of_inputs + 3, column=3, padx=2, pady=10)
        self.toler_lbl.grid(row=self.number_of_inputs + 4, column=0, padx=2, pady=10)
        self.toler_inpt.grid(row=self.number_of_inputs + 4, column=1, padx=2, pady=10)
        self.max_iter_lbl.grid(row=self.number_of_inputs + 4, column=2, padx=2, pady=10)
        self.max_iter_entry.grid(row=self.number_of_inputs + 4, column=3, padx=2, pady=10)
        self.add_function_button.grid(row=self.number_of_inputs + 5, column=0, padx=2, pady=10)
        self.remove_function_button.grid(row=self.number_of_inputs + 5, column=1, padx=2, pady=10)
        if self.number_of_inputs == 2:
            self.remove_function_button.grid_remove()
        self.sbmt_button.grid(row=self.number_of_inputs + 5, column=2, columnspan=2, padx=2, pady=10)
        if self.answer:
            self.answer.grid(row=self.number_of_inputs + 6, column=1, padx=2, pady=10)

    def render_inputs(self):
        self.inputs = []

        for i in range(self.number_of_inputs):
            dct = {
                "label": ttk.Label(self, text=f"Рівняння {i + 1}"),
                "input": ttk.Entry(self, width=60),
            }
            self.inputs.append(dct)
            self.inputs[i]["label"].grid(row=1 + i, column=0, padx=2, pady=5)
            self.inputs[i]["input"].grid(row=1 + i, column=1, columnspan=3, padx=2, pady=5)

    def add_function(self):
        pass

    def remove_function(self):
        pass

    def variable_names(self):
        self.variables_label = ttk.Label(self, text="Змінні: ")
        self.variables_label.grid(row=self.number_of_inputs + 3, column=2, padx=2, pady=10)
        self.variables_entry = ttk.Entry(self, width=15)
        self.variables_entry.grid(row=self.number_of_inputs + 3, column=3, padx=2, pady=10)

    def tolerance_input(self):
        self.toler_lbl = ttk.Label(self, text="Точність")
        self.toler_lbl.grid(row=self.number_of_inputs + 4, column=0, padx=2, pady=10)
        self.toler_inpt = ttk.Entry(self, width=15)
        self.toler_inpt.grid(row=self.number_of_inputs + 4, column=1, padx=2, pady=10)

    def initial_numbers(self):
        pass

    def max_iter_input(self):
        self.max_iter_lbl = ttk.Label(self, text="Максимальна к-сть ітерацій")
        self.max_iter_lbl.grid(row=self.number_of_inputs + 4, column=2, padx=2, pady=10)
        self.max_iter_entry = ttk.Entry(self, width=15)
        self.max_iter_entry.grid(row=self.number_of_inputs + 4, column=3, padx=2, pady=10)

    def add_button(self):
        self.add_function_button = ttk.Button(self, text="Додати функцію", command=self.add_function)
        self.add_function_button.grid(row=self.number_of_inputs + 5, column=0, padx=2, pady=10)

    def remove_button(self):
        self.remove_function_button = ttk.Button(self, text="Видалити функцію", command=self.remove_function)
        if self.number_of_inputs > 2:
            self.remove_function_button.grid(row=self.number_of_inputs + 5, column=1, padx=2, pady=10)

    def submit_button(self):
        self.sbmt_button = ttk.Button(self, text="Вирахувати", command=self.handle_submit, width=30)
        self.sbmt_button.grid(row=self.number_of_inputs + 5, column=2, columnspan=2, padx=2, pady=10)

    def handle_submit(self):
        pass
