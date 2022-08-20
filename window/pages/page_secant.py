import random
import tkinter as tk
import traceback
from math import ceil, log10
from tkinter import ttk

from solving.graph import plot_graph
from solving.secant import secant_method
from window.exceptions.secant_exceptions import SecantExceptions


class PageSecant(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.number_of_inputs = 2
        self.initial_guesses = None
        self.answer = None

        back_btn = ttk.Button(self, text="Повернутися", command=lambda: controller.show_frame(0))
        back_btn.grid(row=0, column=0)

        label = ttk.Label(self, text="Метод січних")
        label.grid(row=0, column=0, columnspan=3, padx=2, pady=10)

        self.render_inputs()
        self.initial_numbers()
        self.variable_names()
        self.add_button()
        self.remove_button()
        self.tolerance_input()
        self.max_iter_input()
        self.submit_button()

    def update_widgets(self):
        self.init_nums_btn.grid(row=self.number_of_inputs + 3, column=1, padx=2, pady=10)
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
            self.initial_guesses = [[initial_nums[i][j].get() for j in range(len(initial_nums[i]))] for i in range(len(initial_nums))]
            win.withdraw()

        def generate_random_guesses(initial_nums):
            for i in range(len(initial_nums)):
                for j in range(len(initial_nums[i])):
                    initial_nums[i][j].delete(0, tk.END)
                    initial_nums[i][j].insert(-1, random.uniform(-10, 10))

        def create():
            win = tk.Toplevel(self)
            initial_nums = [[ttk.Entry(win, width=7) for _ in range(self.number_of_inputs)] for _ in range(self.number_of_inputs + 1)]
            for i in range(len(initial_nums)):
                for j in range(len(initial_nums[i])):
                    if self.initial_guesses is not None:
                        initial_nums[i][j].insert(-1, self.initial_guesses[i][j])
                    initial_nums[i][j].grid(row=j, column=i, padx=2, pady=5)
            sbmt_btn = ttk.Button(win, text="Зберегти", command=lambda: save_initial_guesses(initial_nums, win))
            sbmt_btn.grid(row=len(initial_nums) + 1)
            tst_btn = ttk.Button(win, text="Згенерувати", command=lambda: generate_random_guesses(initial_nums))
            tst_btn.grid(row=len(initial_nums) + 1, column=1)

        self.init_nums_btn = ttk.Button(self, text="Додати початкові", command=create)
        self.initial_nums_label = ttk.Label(self, text="Початкові наближення: ")
        self.init_nums_btn.grid(row=self.number_of_inputs + 3, column=1, padx=2, pady=10)
        self.initial_nums_label.grid(row=self.number_of_inputs + 3, column=0, padx=2, pady=10)

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
        funcs = [inp["input"].get() for inp in self.inputs]

        try:
            exceptions_object = SecantExceptions(funcs=funcs,
                                                 variables_entry=self.variables_entry,
                                                 tolerance_input=self.toler_inpt,
                                                 max_iter_entry=self.max_iter_entry,
                                                 init_nums_entry=self.initial_guesses)

            result, iters = secant_method(funcs=funcs.copy(),
                                          nums=exceptions_object.init_guesses,
                                          tolerance=exceptions_object.tolerance,
                                          variables=exceptions_object.variables,
                                          max_iter=exceptions_object.max_iter)
            # initial guesses handling
            if type(result) == str:
                answer_string = result
            else:
                answer_list = []
                for i in range(len(result)):
                    result[i] = round(result[i], ceil(-log10(exceptions_object.tolerance)))
                    answer_list.append(f"{exceptions_object.variables[i]}={result[i]}")
                answer_string = ", ".join(answer_list) + f"\tК-сть ітерацій: {iters}"
        except AttributeError:
            answer_string = "Перевірте коректність введеної функції"
        except Exception as ex:
            answer_string = ex
            print(traceback.format_exc())

        if self.answer is not None:
            self.answer.destroy()
        self.answer = ttk.Label(self, text=answer_string)
        self.answer.grid(row=self.number_of_inputs + 6, column=0, columnspan=4, padx=2, pady=10)

        if '=' in answer_string and self.number_of_inputs == 2:
            plot_graph(funcs, self.variables_entry.get().split())
