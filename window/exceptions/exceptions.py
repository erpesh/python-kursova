class Exceptions:
    def __init__(self, funcs, variables_entry, tolerance_input, max_iter_entry, init_nums_entry):
        self.funcs = funcs
        self.variables_entry = variables_entry
        self.tolerance_input = tolerance_input
        self.max_iter_entry = max_iter_entry
        self.init_nums_entry = init_nums_entry

        self.variables = None
        self.tolerance = None
        self.max_iter = None
        self.init_guesses = None

    @staticmethod
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def funcs_exc(self):
        if not all(self.funcs):
            raise Exception("Введіть всі рівняння")
        if not all(['=' in func for func in self.funcs]):
            raise Exception("Рівняння повинні мати знак дорівнює")

    def variables_exc(self):
        variables = self.variables_entry.get().split(' ')
        variables_lengths = [len(x) for x in variables]
        used_letters = ['e', 'l', 'o', 'g', 's', 'i', 'n', 'c', 't', 'p', 'a']
        if not self.variables_entry.get():
            raise Exception("Ввадіть змінні")
        if sum(variables_lengths) != len(variables):
            raise Exception("Змінні повинні складатись з 1 латинської літери")
        if len(variables) != len(self.funcs):
            raise Exception("К-сть змінних повинна дорівнювати к-сті рівнянь")
        if not all([item.isalpha() for item in variables]):
            raise Exception("Змінні повинні бути латинськими літерами")
        for letter in used_letters:
            if letter in variables:
                raise Exception(f'Літера "{letter}" не може бути змінною')

        self.variables = variables

    def tolerance_exc(self):
        if not self.tolerance_input.get():
            raise Exception("Введіть точність")
        if not self.isfloat(self.tolerance_input.get()):
            raise Exception("Точність повинна бути числом")
        tolerance = float(self.tolerance_input.get())
        if tolerance < 0:
            raise Exception("Точність повинна бути додатнім числом")

        self.tolerance = tolerance

    def max_iter_exc(self):
        if not self.max_iter_entry.get():
            raise Exception("Введіть максимальну к-сть ітерацій")
        if not self.max_iter_entry.get().isnumeric():
            raise Exception("К-сть ітерацій повинна бути додатнім, цілим числом")
        max_iter = int(self.max_iter_entry.get())

        self.max_iter = max_iter
