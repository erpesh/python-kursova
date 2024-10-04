from window.exceptions.exceptions import Exceptions


class NewtonExceptions(Exceptions):
    def __init__(self, funcs, variables_entry, tolerance_input, max_iter_entry, init_nums_entry):
        super().__init__(funcs, variables_entry, tolerance_input, max_iter_entry, init_nums_entry)

        self.funcs_exc()
        self.initial_guesses_exc()
        self.variables_exc()
        self.tolerance_exc()
        self.max_iter_exc()

    def initial_guesses_exc(self):
        if not self.init_nums_entry.get():
            raise Exception("Enter initial guesses")
        string_guesses = self.init_nums_entry.get().split(' ')
        if not all([self.isfloat(item) for item in string_guesses]):
            raise Exception("Initial guesses must be numbers")
        nums = [float(x) for x in string_guesses]
        if len(nums) != len(self.funcs):
            raise Exception("The number of initial guesses must equal the number of equations")

        self.init_guesses = nums

