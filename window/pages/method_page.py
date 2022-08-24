import math
import tkinter as tk
import traceback
from tkinter import ttk

from solving.evaled import EvaledMethods
from solving.newton import NewtonMethod
from solving.secant import SecantMethod
from window.exceptions.newton_exceptions import NewtonExceptions
from window.exceptions.secant_exceptions import SecantExceptions


class MethodPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.method = None

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
        funcs = [inp["input"].get() for inp in self.inputs]

        try:
            exceptions_object = None
            solver_object = None
            if self.method == "Secant":
                exceptions_object = SecantExceptions(funcs=funcs,
                                                     variables_entry=self.variables_entry,
                                                     tolerance_input=self.toler_inpt,
                                                     max_iter_entry=self.max_iter_entry,
                                                     init_nums_entry=self.initial_guesses)

                solver_object = SecantMethod(funcs=funcs.copy(),
                                             nums=exceptions_object.init_guesses,
                                             tolerance=exceptions_object.tolerance,
                                             variables=exceptions_object.variables,
                                             max_iter=exceptions_object.max_iter)
            if self.method == "Newton":
                exceptions_object = NewtonExceptions(funcs=funcs,
                                                     variables_entry=self.variables_entry,
                                                     tolerance_input=self.toler_inpt,
                                                     max_iter_entry=self.max_iter_entry,
                                                     init_nums_entry=self.init_nums)

                solver_object = NewtonMethod(funcs=funcs.copy(),
                                             nums=exceptions_object.init_guesses,
                                             tolerance=exceptions_object.tolerance,
                                             variables=exceptions_object.variables,
                                             max_iter=exceptions_object.max_iter)

            result, iters = solver_object.result, solver_object.iters

            # initial guesses handling
            if type(result) == str:
                answer_string = result
            else:
                answer_string = self.build_result(result, exceptions_object, iters)
        except AttributeError:
            print(traceback.format_exc())
            answer_string = "Перевірте коректність введеної функції"
        except Exception as ex:
            answer_string = ex
            print(traceback.format_exc())

        if self.answer is not None:
            self.answer.destroy()
        self.answer = ttk.Label(self, text=answer_string)
        self.answer.grid(row=self.number_of_inputs + 6, column=0, columnspan=4, padx=2, pady=10)

        if '=' in answer_string and self.number_of_inputs == 2:
            EvaledMethods.plot_graph(funcs, self.variables_entry.get().split())

    @staticmethod
    def build_result(result, exceptions_object, iters):
        answer_list = []
        for i in range(len(result)):
            result[i] = round(result[i], math.ceil(-math.log10(exceptions_object.tolerance)))
            answer_list.append(f"{exceptions_object.variables[i]}={result[i]}")
        answer_string = ", ".join(answer_list) + f"\tК-сть ітерацій: {iters}"
        return answer_string
