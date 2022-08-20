import traceback

import matplotlib.pyplot as plt
from sympy import Symbol, Eq, Or, log, sin, cos, tan, cot, atan, acot, asin, acos, pi
from sympy.plotting import plot, plot_implicit
from math import e


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