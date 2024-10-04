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
            raise Exception("Enter all equations")
        if not all(['=' in func for func in self.funcs]):
            raise Exception("Equations must have an equal sign")

    def variables_exc(self):
        variables = self.variables_entry.get().split(' ')
        variables_lengths = [len(x) for x in variables]
        USED_LETTERS = ['e', 'l', 'o', 'g', 's', 'i', 'n', 'c', 't', 'p', 'a']
        if not self.variables_entry.get():
            raise Exception("Enter variables")
        if sum(variables_lengths) != len(variables):
            raise Exception("Variables must consist of 1 English letter")
        if len(variables) != len(self.funcs):
            raise Exception("The number of variables must be equal to the number of equations")
        if not all([item.isalpha() for item in variables]):
            raise Exception("Variables must be English letters")
        if any([variables[i] in variables[i+1:] for i in range(len(variables))]):
            raise Exception("Variable names must be unique")
        for letter in USED_LETTERS:
            if letter in variables:
                raise Exception(f'The letter "{letter}" cannot be a variable, use another letter')

        self.variables = variables

    def tolerance_exc(self):
        if not self.tolerance_input.get():
            raise Exception("Enter precision")
        if not self.isfloat(self.tolerance_input.get()):
            raise Exception("Precision must be a number")
        tolerance = float(self.tolerance_input.get())
        if tolerance < 0:
            raise Exception("Precision must be a positive number")

        self.tolerance = tolerance

    def max_iter_exc(self):
        if not self.max_iter_entry.get():
            raise Exception("Enter maximum number of iterations")
        if not self.max_iter_entry.get().isnumeric():
            raise Exception("Number of iterations must be a positive integer")
        max_iter = int(self.max_iter_entry.get())

        self.max_iter = max_iter
