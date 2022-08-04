import tkinter as tk
from math import ceil, log10
from tkinter import ttk

from solving.newton import newton_method
from window.exceptions.newton_exceptions import funcs_exc, initial_guesses_exc, variables_exc, tolerance_exc, max_iter_exc


class PageSecant(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.number_of_inputs = 2
        self.answer = None

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

        if self.number_of_inputs == 10:
            self.add_function_button.grid_remove()

    def remove_function(self):
        self.number_of_inputs -= 1
        self.inputs[-1]["label"].destroy()
        self.inputs[-1]["input"].destroy()
        self.inputs = self.inputs[:-1]
        self.update_widgets()

    def initial_numbers(self):
        self.init_nums = ttk.Entry(self, width=15)
        self.initial_nums_label = ttk.Label(self, text="Початкові наближення: ")
        self.init_nums.grid(row=self.number_of_inputs + 3, column=1, padx=2, pady=10)
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
        try:
            funcs = [inp["input"].get() for inp in self.inputs]
            # funcs handling
            funcs_exc(funcs)
            # initial guesses handling
            nums = initial_guesses_exc(self.init_nums, funcs)
            # variables handling
            variables = variables_exc(self.variables_entry, funcs)
            # tolerance handling
            tolerance = tolerance_exc(self.toler_inpt)
            # max iter handling
            max_iter = max_iter_exc(self.max_iter_entry)
            result, iters = newton_method(funcs=funcs, nums=nums, tolerance=tolerance, variables=variables,
                                          max_iter=max_iter)
            # bad initial guesses handling
            if type(result) == str:
                answer_string = result
            else:
                answer_list = []
                for i in range(len(result)):
                    result[i] = round(result[i], ceil(-log10(tolerance)))
                    answer_list.append(f"{variables[i]}={result[i]}")
                answer_string = ", ".join(answer_list) + f"\tК-сть ітерацій: {iters}"
        except AttributeError:
            answer_string = "Перевірте коректність введеної функції"
        except Exception as ex:
            answer_string = ex
            # print(traceback.format_exc())

        if self.answer is not None:
            self.answer.destroy()
        self.answer = ttk.Label(self, text=answer_string)
        self.answer.grid(row=self.number_of_inputs + 6, column=0, columnspan=4, padx=2, pady=10)
