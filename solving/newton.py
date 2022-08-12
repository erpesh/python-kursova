import traceback
from sympy import Symbol, lambdify
import numpy as np

from solving.utils.jacobian import calculate_jacobian
from solving.utils.parse_functionss import parse_functions


def f(funcs, num_list, variables):
    # print(funcs)
    # print(num_list)
    # print(variables)
    # print(type(funcs[0]))
    # print(type(num_list[0]))
    # print(type(variables[0]))
    result_list = [lambdify(variables, func)(*num_list) for func in funcs]
    return np.array(result_list)


def j(jac, num_list, variables):
    result_matrix = [[lambdify(variables, equation)(*num_list) for equation in jac_row] for jac_row in jac]
    return np.array(result_matrix)


def calculate_new_x(function_list, jacobian, numbers, variables):
    try:
        j_mat = np.linalg.inv(j(jacobian, numbers, variables))
        f_mat = f(function_list, numbers, variables)
        jacobian_rev_multi_func = np.matmul(j_mat, f_mat)
    except Exception:
        print(traceback.format_exc())
        return None
    new_x = np.array(numbers) - jacobian_rev_multi_func
    return new_x


def newton_method(funcs, nums, variables, tolerance=0.00001, max_iter=1000):
    funcs = parse_functions(funcs)
    jacobian, funcs = calculate_jacobian(funcs, variables)
    jacobian = np.array(jacobian)
    variables = [Symbol(var, real=True) for var in variables]
    nums = [float(num) for num in nums]
    new_x = calculate_new_x(funcs, jacobian, nums, variables)
    iters = 0
    for i in range(max_iter):
        iters += 1
        if new_x is None or True in [np.isnan(np.min(number)) for number in new_x]:
            return "Щось пішло не так, спробуйте інші числа", 0
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
    else:
        print("Максимальна к-сть ітерацій досягнута!")
        return "Максимальна к-сть ітерацій досягнута!", max_iter
    return new_x.tolist(), iters
