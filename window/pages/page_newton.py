import tkinter as tk
from math import log10, ceil
from tkinter import ttk
import traceback

from solving.evaled import EvaledMethods
from solving.newton import NewtonMethod
from window.exceptions.newton_exceptions import NewtonExceptions
from window.pages.method_page import MethodPage


class PageNewton(MethodPage):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.number_of_inputs = 2
        self.answer = None

        back_btn = ttk.Button(self, text="Повернутися", command=lambda: controller.show_frame(0))
        back_btn.grid(row=0, column=0)

        label = ttk.Label(self, text="Метод Ньютона")
        label.grid(row=0, column=1, columnspan=3, padx=2, pady=10)

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

    def handle_submit(self):

        funcs = [inp["input"].get() for inp in self.inputs]

        try:
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
            EvaledMethods.plot_graph(funcs, self.variables_entry.get().split())
