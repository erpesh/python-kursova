# check if string is float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def funcs_exc(funcs):
    if not all(funcs):
        raise Exception("Enter all functions")


def initial_guesses_exc(init_nums, funcs):
    if not init_nums.get():
        raise Exception("Enter initial guesses")
    string_guesses = init_nums.get().split(' ')
    if not all([isfloat(item) for item in string_guesses]):
        raise Exception("Initial guesses must be numbers")
    nums = [float(x) for x in string_guesses]
    if len(nums) != len(funcs):
        raise Exception("Number of initial guesses should be equal to number of functions")
    return nums


def variables_exc(variables_entry, funcs):
    variables = variables_entry.get().split(' ')
    variables_lengths = [len(x) for x in variables]
    if not variables_entry.get():
        raise Exception("Enter the variable names")
    if sum(variables_lengths) != len(variables):
        raise Exception("Use only 1-letter variables")
    if len(variables) != len(funcs):
        raise Exception("You must enter the same number of variables as the functions")
    if not all([item.isalpha() for item in variables]):
        raise Exception("Variables must be letters")
    return variables


def tolerance_exc(toler_inpt):
    if not toler_inpt.get():
        raise Exception("Enter tolerance")
    if not isfloat(toler_inpt.get()):
        raise Exception("Tolerance should be a number")
    tolerance = float(toler_inpt.get())
    if tolerance < 0:
        raise Exception("Tolerance should be positive")
    return tolerance


def max_iter_exc(max_iter_entry):
    if not max_iter_entry.get():
        raise Exception("Enter max iterations number")
    if not max_iter_entry.get().isnumeric():
        raise Exception("Max iterations should be a positive number")
    max_iter = int(max_iter_entry.get())
    return max_iter
