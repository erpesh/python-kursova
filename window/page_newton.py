import tkinter as tk
from tkinter import ttk

from solving.newton import newton_method


class PageNewton(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.number_of_inputs = 2

        label = ttk.Label(self, text="Newton method")
        label.grid(row=0, column=0, columnspan=3, padx=2, pady=10)

        self.render_inputs()
        self.initial_numbers()
        self.add_button()
        self.tolerance_input()
        self.submit_button()

    def render_inputs(self):
        self.inputs = []

        for i in range(self.number_of_inputs):
            dct = {
                "label": ttk.Label(self, text=f"f{i + 1}() = "),
                "input": ttk.Entry(self, width=30)
            }
            self.inputs.append(dct)
            self.inputs[i]["label"].grid(row=1 + i, column=0, padx=2, pady=5)
            self.inputs[i]["input"].grid(row=1 + i, column=1, padx=2, pady=5)

    def update_widgets(self):
        self.init_nums.grid(row=self.number_of_inputs + 3, column=1, padx=2, pady=10)
        self.initial_nums_label.grid(row=self.number_of_inputs + 3, column=0, padx=2, pady=10)
        self.toler_lbl.grid(row=self.number_of_inputs + 4, column=0, padx=2, pady=10)
        self.toler_inpt.grid(row=self.number_of_inputs + 4, column=1, padx=2, pady=10)
        self.add_function_button.grid(row=self.number_of_inputs + 5, column=0, padx=2, pady=10)
        self.sbmt_button.grid(row=self.number_of_inputs + 5, column=1, padx=2, pady=10)
        self.answer.grid(row=self.number_of_inputs + 6, column=1, padx=2, pady=10)

    def add_input(self):
        self.number_of_inputs += 1

        # change initial numbers, add button, submit button positions
        self.update_widgets()

        self.inputs.append({
            "label": ttk.Label(self, text=f"f{self.number_of_inputs}() = "),
            "input": ttk.Entry(self, width=30)
        })
        self.inputs[self.number_of_inputs - 1]["label"].grid(row=2 + self.number_of_inputs, column=0, padx=2, pady=5)
        self.inputs[self.number_of_inputs - 1]["input"].grid(row=2 + self.number_of_inputs, column=1, padx=2, pady=5)

        if self.number_of_inputs == 10:
            self.add_function_button.destroy()

    def initial_numbers(self):
        self.init_nums = ttk.Entry(self, width=30)
        self.initial_nums_label = ttk.Label(self, text="Initial guesses: ")
        self.init_nums.grid(row=self.number_of_inputs + 3, column=1, padx=2, pady=10)
        self.initial_nums_label.grid(row=self.number_of_inputs + 3, column=0, padx=2, pady=10)

    def tolerance_input(self):
        self.toler_lbl = ttk.Label(self, text="Tolerance")
        self.toler_lbl.grid(row=self.number_of_inputs + 4, column=0, padx=2, pady=10)
        self.toler_inpt = ttk.Entry(self, width=30)
        self.toler_inpt.grid(row=self.number_of_inputs + 4, column=1, padx=2, pady=10)

    def add_button(self):
        self.add_function_button = ttk.Button(self, text="Add function", command=self.add_input)
        self.add_function_button.grid(row=self.number_of_inputs + 5, column=0, padx=2, pady=10)

    def handle_submit(self):
        funcs = [inp["input"].get() for inp in self.inputs]
        # nums = [[1, 1], [1, 2], [1.5, 2]]
        variables = ["x", "y"]

        try:
            nums = [int(x) for x in self.init_nums.get().split()]
            tolerance = float(self.toler_inpt.get())
            array, iters = newton_method(funcs=funcs, nums=nums, tolerance=tolerance, variables=variables)
            answer_string = ', '.join([str(x) for x in array]) + f"\tIterations: {iters}"
        except Exception as ex:
            print(ex)
            answer_string = "Something went wrong. Check your input."

        self.answer = ttk.Label(self, text=answer_string)
        self.answer.grid(row=self.number_of_inputs + 6, column=1, padx=2, pady=10)

    def submit_button(self):
        self.sbmt_button = ttk.Button(self, text="Submit", command=self.handle_submit)
        self.sbmt_button.grid(row=self.number_of_inputs + 5, column=1, padx=2, pady=10)
