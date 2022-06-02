from sympy import *
import numpy as np
from math import (
    e
)


def calculate_jacobian(functions, variables):
    function_list = functions.copy()

    lets = [Symbol(variables[i]) for i in range(len(function_list))]
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
    for i in range(len(function_list)):
        ev = eval(function_list[i])
        dif = [ev.diff(lets[j]) for j in range(len(function_list))]
        diffs.append(dif)
    jacobian = np.array(diffs)
    return jacobian


def j(jac, num_list, variables):
    string_nums = [str(jac[l][i]) for l in range(len(jac)) for i in range(len(jac))]
    for i in range(len(string_nums)):
        for q in range(len(num_list)):
            string_nums[i] = string_nums[i].replace(variables[q], str(num_list[q]), len(string_nums[i]))
        string_nums[i] = eval(string_nums[i])
    return np.array(string_nums).reshape(len(num_list), len(num_list))


def f(funcs, num_list, variables):
    funcs_list = funcs.copy()
    for i in range(len(funcs_list)):
        for q in range(len(num_list)):
            funcs_list[i] = funcs_list[i].replace(variables[q], '(' + str(num_list[q]) + ')', len(funcs_list[i]))
        funcs_list[i] = eval(funcs_list[i])
    return np.array(funcs_list)


def calculate_new_x(function_list, jacobian, numbers, variables):
    try:
        jacobian_rev_multi_func = np.matmul(np.linalg.inv(j(jacobian, numbers, variables)), f(function_list, numbers, variables))
    except Exception:
        return None
    new_x = np.array(numbers) - jacobian_rev_multi_func
    return new_x


def newton_method(funcs, nums, variables, tolerance=0.00001, max_iter=1000):
    jacobian = calculate_jacobian(funcs, variables)
    jacobian = np.array(jacobian)
    new_x = calculate_new_x(funcs, jacobian, nums, variables)
    iters = 0
    for i in range(max_iter):
        if new_x is None:
            return "Try another numbers", 0
        count = 0
        for q in range(len(new_x)):
            first_condition = abs(new_x[q] - nums[q]) < tolerance
            second_condition = sum(abs(f(funcs, nums, variables=variables)) < tolerance) == len(nums)
            if first_condition or second_condition:
                count += 1
        if count == len(nums):
            break
        nums = new_x
        new_x = calculate_new_x(funcs, jacobian, nums, variables=variables)
        iters = i
    else:
        print("Maximum number of iterations is reached!")
        return "Maximum number of iterations is reached!", max_iter
    return new_x.tolist(), iters
