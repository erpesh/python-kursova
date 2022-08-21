import traceback

import matplotlib.pyplot as plt
from sympy import Symbol, Eq, Or, log, sin, cos, tan, cot, atan, acot, asin, acos, pi
from sympy.plotting import plot_implicit
from math import e
import numpy as np

class EvaledMethods:

    @staticmethod
    def plot_graph(funcs, variables):
        plt.rcParams["xtick.labelsize"] = 10
        plt.rcParams["xtick.color"] = "red"

        try:
            lets = [Symbol(x) for x in variables]
            for i in range(len(funcs)):
                for j in range(len(funcs)):
                    funcs[i] = funcs[i].replace(variables[j], f"lets[{j}]")
            funcs = [func.split('=') for func in funcs]
            first_equation = Eq(eval(funcs[0][0]), eval(funcs[0][1]))
            second_equation = Eq(eval(funcs[1][0]), eval(funcs[1][1]))
            p = plot_implicit(Or(first_equation, second_equation), (lets[0], -15, 15), (lets[1], -10, 10))
        except Exception as ex:
            print(traceback.format_exc())

    @staticmethod
    def calculate_jacobian(functions, variables):
        function_list = functions.copy()

        lets = [Symbol(variables[i], real=True) for i in range(len(function_list))]
        for i in range(len(function_list)):
            for k in range(len(function_list)):
                j = 0
                while True:
                    if len(function_list[i]) == j:
                        break
                    if function_list[i][j] == variables[k]:
                        function_list[i] = function_list[i][:j] + f"lets[{k}]" + function_list[i][j + 1:]
                        j += len(f"lets[{k}]") - 1
                    j += 1
        diffs = []
        evaled_functions = []
        for i in range(len(function_list)):
            ev = eval(function_list[i])
            evaled_functions.append(ev)
            dif = [ev.diff(lets[j]) for j in range(len(function_list))]
            diffs.append(dif)
        jacobian = np.array(diffs)
        return jacobian, evaled_functions