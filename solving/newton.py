import traceback
from sympy import Symbol
import numpy as np

from solving.evaled import EvaledMethods
from solving.solver import Solver


class NewtonMethod(Solver):
    def __init__(self, funcs, nums, variables, tolerance, max_iter):
        super().__init__()

        self.result, self.iters = self.solve(funcs, nums, variables, tolerance, max_iter)

    def calculate_new_x(self, function_list, jacobian, numbers, variables):
        try:
            j_mat = np.linalg.inv(self.j(jacobian, numbers, variables))
            f_mat = self.f(function_list, numbers, variables)
            jacobian_rev_multi_func = np.matmul(j_mat, f_mat)
        except Exception:
            print(traceback.format_exc())
            return None
        new_x = np.array(numbers) - jacobian_rev_multi_func
        return new_x

    def solve(self, funcs, nums, variables, tolerance, max_iter):
        funcs = self.parse_functions(funcs)
        jacobian, funcs = EvaledMethods.calculate_jacobian(funcs, variables)
        jacobian = np.array(jacobian)
        variables = [Symbol(var, real=True) for var in variables]
        nums = [float(num) for num in nums]
        new_x = self.calculate_new_x(funcs, jacobian, nums, variables)
        iters = 0
        for i in range(max_iter):
            iters += 1
            if new_x is None or True in [np.isnan(np.min(number)) for number in new_x]:
                return "Щось пішло не так, спробуйте інші числа", 0
            count = 0
            for q in range(len(new_x)):
                first_condition = abs(new_x[q] - nums[q]) < tolerance
                second_condition = sum(abs(self.f(funcs, nums, variables)) < tolerance) == len(nums)
                if first_condition or second_condition:
                    count += 1
            if count == len(nums):
                break
            nums = new_x
            new_x = self.calculate_new_x(funcs, jacobian, nums, variables=variables)
        else:
            print("Максимальна к-сть ітерацій досягнута!")
            return "Максимальна к-сть ітерацій досягнута!", max_iter
        return new_x.tolist(), iters


