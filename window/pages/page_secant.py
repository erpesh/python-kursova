import random
import tkinter as tk
from tkinter import ttk

from window.pages.method_page import MethodPage


class PageSecant(MethodPage):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.method = "Secant"
        self.number_of_inputs = 2
        self.initial_guesses = None
        self.answer = None

        back_btn = ttk.Button(self, text="Повернутися", command=lambda: controller.show_frame(0))
        back_btn.grid(row=0, column=0)

        label = ttk.Label(self, text="Метод січних")
        label.grid(row=0, column=1, padx=2, pady=10)

        self.read_button()
        self.render_inputs()
        self.initial_numbers()
        self.variable_names()
        self.add_button()
        self.remove_button()
        self.tolerance_input()
        self.max_iter_input()
        self.submit_button()

    def add_function(self):
        self.number_of_inputs += 1

        # change initial numbers, add button, submit button positions
        self.update_widgets()

        self.inputs.append({
            "label": ttk.Label(self, text=f"Рівняння {self.number_of_inputs}"),
            "input": ttk.Entry(self, width=60)
        })
        self.inputs[self.number_of_inputs - 1]["label"].grid(row=2 + self.number_of_inputs, column=0, padx=2, pady=5)
        self.inputs[self.number_of_inputs - 1]["input"].grid(row=2 + self.number_of_inputs, column=1, columnspan=3,
                                                             padx=2, pady=5)

        if self.number_of_inputs == 5:
            self.add_function_button.grid_remove()

        self.initial_guesses = None

    def remove_function(self):
        self.number_of_inputs -= 1
        self.inputs[-1]["label"].destroy()
        self.inputs[-1]["input"].destroy()
        self.inputs = self.inputs[:-1]
        self.update_widgets()
        self.initial_guesses = None

    def initial_numbers(self):

        def save_initial_guesses(initial_nums, win):
            self.initial_guesses = [[initial_nums[i][j].get() for j in range(len(initial_nums[i]))] for i in
                                    range(len(initial_nums))]
            win.withdraw()

        def generate_random_guesses(initial_nums):
            for i in range(len(initial_nums)):
                for j in range(len(initial_nums[i])):
                    initial_nums[i][j].delete(0, tk.END)
                    initial_nums[i][j].insert(-1, random.uniform(-10, 10))

        def create():
            win = tk.Toplevel(self)
            initial_nums = [[ttk.Entry(win, width=7) for _ in range(self.number_of_inputs)] for _ in
                            range(self.number_of_inputs + 1)]
            for i in range(len(initial_nums)):
                for j in range(len(initial_nums[i])):
                    if self.initial_guesses is not None:
                        initial_nums[i][j].insert(-1, self.initial_guesses[i][j])
                    initial_nums[i][j].grid(row=j, column=i, padx=2, pady=5)
            sbmt_btn = ttk.Button(win, text="Зберегти", command=lambda: save_initial_guesses(initial_nums, win))
            sbmt_btn.grid(row=len(initial_nums) + 1)
            tst_btn = ttk.Button(win, text="Згенерувати", command=lambda: generate_random_guesses(initial_nums))
            tst_btn.grid(row=len(initial_nums) + 1, column=1)

        self.init_nums = ttk.Button(self, text="Додати початкові", command=create)
        self.initial_nums_label = ttk.Label(self, text="Початкові наближення: ")
        self.init_nums.grid(row=self.number_of_inputs + 3, column=1, padx=2, pady=10)
        self.initial_nums_label.grid(row=self.number_of_inputs + 3, column=0, padx=2, pady=10)

