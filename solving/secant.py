import traceback

import numpy as np
from sympy import Symbol

from solving.evaled import EvaledMethods
from solving.solver import Solver


class SecantMethod(Solver):
    def __init__(self, funcs, nums, variables, tolerance, max_iter):
        super().__init__()

        self.result, self.iters = self.solve(funcs, nums, variables, tolerance, max_iter)

    def calculate(self, funcs, nums, variables):
        A = np.array([[1] + self.f(funcs, nums[i], variables).tolist() for i in range(len(funcs) + 1)]).transpose()
        C = np.array([1] + [0 for _ in range(len(funcs))]).transpose()
        try:
            B = np.matmul(np.linalg.inv(A), C)
        except Exception as ex:
            print(traceback.format_exc())
            return None

        new_x = 0
        for i in range(len(funcs) + 1):
            new_x += B[i] * np.array(nums[i])

        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]
        nums[-1] = new_x.tolist()

        return nums

    def solve(self, funcs, nums, variables, tolerance, max_iter):
        funcs = self.parse_functions(funcs)
        funcs = EvaledMethods.eval_functions(funcs, variables)
        variables = [Symbol(var, real=True) for var in variables]
        iters = 0
        for i in range(max_iter):
            if nums is None:
                return "Щось пішло не так, спробуйте інші числа", 0
            first_cond_list = abs(np.array(nums[-1]) - np.array(nums[-2])) < tolerance
            first_condition = sum(first_cond_list) == len(nums[0])
            second_cond_list = abs(np.array(self.f(funcs=funcs, variables=variables, num_list=nums[-1]))) < tolerance
            second_condition = sum(second_cond_list) == len(nums[0])
            if first_condition or second_condition:
                break
            else:
                nums = self.calculate(funcs, nums, variables)
            iters += 1
        else:
            print("Maximum number of iterations is reached!")
        return nums[-1], iters


