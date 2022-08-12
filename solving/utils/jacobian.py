from sympy import Symbol, log, sin, cos, tan, cot, atan, acot, asin, acos, pi
from math import e
import numpy as np


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
    evalled_functions = []
    for i in range(len(function_list)):
        ev = eval(function_list[i])
        evalled_functions.append(ev)
        dif = [ev.diff(lets[j]) for j in range(len(function_list))]
        diffs.append(dif)
    jacobian = np.array(diffs)
    return jacobian, evalled_functions
