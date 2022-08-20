import numpy as np
from sympy import lambdify

from solving.utils.parse_functions import parse_functions


def f(funcs, variables, num_list):
    result_list = [lambdify(variables, func)(*num_list) for func in funcs]
    return result_list


def calculate(funcs, nums, variables):
    A = np.array([[1] + f(funcs, variables, nums[i]) for i in range(len(funcs) + 1)]).transpose()
    C = np.array([1] + [0 for _ in range(len(funcs))]).transpose()
    try:
        B = np.matmul(np.linalg.inv(A), C)
    except Exception as ex:
        print(ex)
        return None

    new_x = 0
    for i in range(len(funcs) + 1):
        new_x += B[i] * np.array(nums[i])

    for i in range(len(nums) - 1):
        nums[i] = nums[i + 1]
    nums[-1] = new_x.tolist()

    return nums


def secant_method(funcs, nums, variables, tolerance=0.00001, max_iter=1000):
    funcs = parse_functions(funcs)
    iters = 0
    for i in range(max_iter):
        if nums is None:
            return "Щось пішло не так, спробуйте інші числа", 0
        first_cond_list = abs(np.array(nums[-1]) - np.array(nums[-2])) < tolerance
        first_condition = sum(first_cond_list) == len(nums[0])
        second_cond_list = abs(np.array(f(funcs, variables, num_list=nums[-1]))) < tolerance
        second_condition = sum(second_cond_list) == len(nums[0])
        if first_condition or second_condition:
            break
        else:
            nums = calculate(funcs, nums, variables)
        iters += 1
    else:
        print("Maximum number of iterations is reached!")
    return nums[-1], iters
