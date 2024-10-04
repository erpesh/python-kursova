from window.exceptions.exceptions import Exceptions


class SecantExceptions(Exceptions):
    def __init__(self, funcs, variables_entry, tolerance_input, max_iter_entry, init_nums_entry):
        super().__init__(funcs, variables_entry, tolerance_input, max_iter_entry, init_nums_entry)

        self.funcs_exc()
        self.initial_guesses_exc()
        self.variables_exc()
        self.tolerance_exc()
        self.max_iter_exc()

    def initial_guesses_exc(self):
        if self.init_nums_entry is None:
            raise Exception("Enter initial guesses")
        if not all(self.isfloat(item) for row in self.init_nums_entry for item in row):
            raise Exception("Initial guesses must be numbers")

        self.init_guesses = [[float(item) for item in row] for row in self.init_nums_entry]
