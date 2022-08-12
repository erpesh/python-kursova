# check if string is float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def funcs_exc(funcs):
    if not all(funcs):
        raise Exception("Введіть всі рівняння")
    if not all(['=' in func for func in funcs]):
        raise Exception("Рівняння повинні мати знак дорівнює")


def initial_guesses_exc(init_nums, funcs):
    if not init_nums.get():
        raise Exception("Введіть початкові наближенння")
    string_guesses = init_nums.get().split(' ')
    if not all([isfloat(item) for item in string_guesses]):
        raise Exception("Початкові наближення повинні бути цифрами")
    nums = [float(x) for x in string_guesses]
    if len(nums) != len(funcs):
        raise Exception("К-сть початкових наближень має бути рівною к-сті рівнянь")
    return nums


def variables_exc(variables_entry, funcs):
    variables = variables_entry.get().split(' ')
    variables_lengths = [len(x) for x in variables]
    used_letters= ['e', 'l', 'o', 'g', 's', 'i', 'n', 'c', 't', 'p', 'a']
    if not variables_entry.get():
        raise Exception("Ввадіть змінні")
    if sum(variables_lengths) != len(variables):
        raise Exception("Змінні повинні складатись з 1 латинської літери")
    if len(variables) != len(funcs):
        raise Exception("К-сть змінних повинна дорівнювати к-сті рівнянь")
    if not all([item.isalpha() for item in variables]):
        raise Exception("Змінні повинні бути латинськими літерами")
    for letter in used_letters:
        if letter in variables:
            raise Exception(f'Літера "{letter}" не може бути змінною')

    return variables


def tolerance_exc(toler_inpt):
    if not toler_inpt.get():
        raise Exception("Введіть точність")
    if not isfloat(toler_inpt.get()):
        raise Exception("Точність повинна бути числом")
    tolerance = float(toler_inpt.get())
    if tolerance < 0:
        raise Exception("Точність повинна бути додатнім числом")
    return tolerance


def max_iter_exc(max_iter_entry):
    if not max_iter_entry.get():
        raise Exception("Введіть максимальну к-сть ітерацій")
    if not max_iter_entry.get().isnumeric():
        raise Exception("К-сть ітерацій повинна бути додатнім, цілим числом")
    max_iter = int(max_iter_entry.get())
    return max_iter
