from sympy import lambdify
import numpy as np


class Solver:
    @staticmethod
    def parse_functions(funcs):
        for i in range(len(funcs)):
            func_splited = funcs[i].split('=')
            funcs[i] = func_splited[0] + "-" + f"({func_splited[1]})"
        return funcs

    @staticmethod
    def f(funcs, num_list, variables):
        result_list = [lambdify(variables, func)(*num_list) for func in funcs]
        return np.array(result_list)

    @staticmethod
    def j(jac, num_list, variables):
        result_matrix = [[lambdify(variables, equation)(*num_list) for equation in jac_row] for jac_row in jac]
        return np.array(result_matrix)
