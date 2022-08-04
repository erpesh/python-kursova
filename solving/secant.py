import numpy as np
from math import (
    e
)


def f(variables, functions):
    _nums = []
    for func in functions:
        for var in variables:
            func = func.replace(var, f"({variables[var]})", len(func))
        ev = eval(func)
        _nums.append(ev)
    return _nums


def fill_dict(nums, dct):
    i = 0
    for key in dct:
        dct[key] = str(nums[i])
        i += 1
    return dct


def calculate(funcs, nums, variables):
    A_matrix_dct = {variables[i]: 0 for i in range(len(funcs))}

    A = np.array([[1] + f(fill_dict(nums[i], A_matrix_dct), funcs) for i in range(len(funcs) + 1)]).transpose()
    C = np.array([1] + [0 for _ in range(len(funcs))]).transpose()
    try:
        B = np.matmul(np.linalg.inv(A), C)
    except Exception:
        return None

    new_x = 0
    for i in range(len(funcs) + 1):
        new_x += B[i] * np.array(nums[i])

    for i in range(len(nums) - 1):
        nums[i] = nums[i + 1]
    nums[-1] = new_x.tolist()

    return nums


def handle_functions(funcs):
    for i in range(len(funcs)):
        func_splited = funcs[i].split('=')
        funcs[i] = func_splited[0] + "-" + f"({func_splited[1]})"
    return funcs


def secant_method(funcs, nums, variables, tolerance=0.00001, max_iter=1000):
    funcs = handle_functions(funcs)
    iters = 0
    for i in range(max_iter):
        if nums is None:
            return "Try another numbers"
        first_cond_list = abs(np.array(nums[-1]) - np.array(nums[-2])) < tolerance
        first_condition = sum(first_cond_list) == len(nums[0])
        second_cond_dct = {variables[i]: 0 for i in range(len(funcs))}
        second_cond_dct = fill_dict(nums[-1], second_cond_dct)
        second_cond_list = abs(np.array(f(second_cond_dct, funcs))) < tolerance
        second_condition = sum(second_cond_list) == len(nums[0])
        if first_condition or second_condition:
            break
        else:
            nums = calculate(funcs, nums, variables)
        iters += 1
    else:
        print("Maximum number of iterations is reached!")
    return nums[-1], iters
