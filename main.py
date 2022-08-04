from window.tkinter_app import start_tkinter
from sympy import Symbol, solve

if __name__ == '__main__':
    start_tkinter()
    x = Symbol("x")
    equatio = "x**2-2*x-15"
    print(solve(equatio, x))
    # funcs = ["2*a-3*b+5*c+d+41", "7*a+2*b-c+28", "-a+2*b-7*c-2*d-46", "3*a+7*b-6*c+d-31"]
    # nums = [[1, 1, 2, 3], [1, 2], [1.5, 2]]
    # variables = ["a", "b", "c", 'd']
    # array, iters = newton_method(funcs=funcs, nums=[1, 2, 0.1, 1], tolerance=10**-4, variables=variables)
    # print(array)
    # for i in range(len(array)):
    #     if abs(round(array[i]) - array[i]) < 10**-4:
    #         array[i] = round(array[i])
    # print(array)
