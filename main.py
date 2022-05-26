from solving.newton import newton_method
from solving.secant import secant_method
#
#
# def solve_equation(method, functions, numbers, variables, tolerance, max_iter):
#     if method == "Newton":
#         return newton_method(funcs=functions, nums=numbers, variables=variables, tolerance=tolerance, max_iter=max_iter)
#     elif method == "secant":
#         return secant_method(funcs=functions, nums=numbers, variables=variables, tolerance=tolerance, max_iter=max_iter)
#
# def main():
#     pass
#
# if __name__ == '__main__':
#     # # main()
#     funcs = ["2*a-3*b+5*c+d+41", "7*a+2*b-c+28", "-a+2*b-7*c-2*d-46", "3*a+7*b-6*c+d-31"]
#     nums = [[1, 1, 2, 3], [1, 2], [1.5, 2]]
#     variables = ["a", "b", "c", 'd']
#     array, iters = newton_method(funcs=funcs, nums=[1, 2, 0.1, 1], tolerance=10**-4, variables=variables)
#     print(array)
#     for i in range(len(array)):
#         if abs(round(array[i]) - array[i]) < 10**-4:
#             array[i] = round(array[i])
#     print(array)
#     open_window()
#     # get_func()

import tkinter as tk
from tkinter import ttk


class TkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, PageNewton, PageSecant):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Choose method")

        # putting the grid in its place by using grid
        label.grid(row=1, column=0, padx=10, pady=10)
        # checkbox for choosing solve method
        var_radio = tk.IntVar()

        checkbox = tk.Radiobutton(self, text="Newton method", variable=var_radio, value=0)
        checkbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        checkbox2 = tk.Radiobutton(self, text="Secant method", variable=var_radio, value=1)
        checkbox2.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        submit_method = ttk.Button(self, text="Submit", command=lambda: controller.show_frame(
            PageNewton if var_radio.get() == 0 else PageSecant))
        submit_method.grid(row=4, column=0, columnspan=3, padx=5, pady=5)


# second window frame page1
class PageNewton(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.number_of_inputs = 2
        self.inputs = None
        self.add_function_button = None
        self.init_nums = None
        self.sbmt_button = None

        label = ttk.Label(self, text="Newton method")
        label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.render_inputs()
        self.initial_numbers()
        self.add_button()
        self.submit_button()

    def render_inputs(self):
        self.inputs = []

        for i in range(self.number_of_inputs):
            dct = {
                "label": ttk.Label(self, text=f"Enter function number {i + 1}"),
                "input": ttk.Entry(self, width=30)
            }
            self.inputs.append(dct)
            self.inputs[i]["label"].grid(row=1 + i, column=0, padx=10, pady=5)
            self.inputs[i]["input"].grid(row=1 + i, column=1, padx=10, pady=5)

    def add_input(self):
        self.number_of_inputs += 1

        # change initial numbers, add button, submit button positions
        self.add_function_button.grid(row=self.number_of_inputs + 4, column=0, padx=10, pady=10)
        self.init_nums.grid(row=self.number_of_inputs + 3, column=0, columnspan=2, padx=10, pady=10)
        self.sbmt_button.grid(row=self.number_of_inputs + 4, column=1, padx=10, pady=10)

        self.inputs.append({
            "label": ttk.Label(self, text=f"Enter function number {self.number_of_inputs}"),
            "input": ttk.Entry(self, width=30)
        })
        self.inputs[self.number_of_inputs - 1]["label"].grid(row=2 + self.number_of_inputs, column=0, padx=10, pady=5)
        self.inputs[self.number_of_inputs - 1]["input"].grid(row=2 + self.number_of_inputs, column=1, padx=10, pady=5)

        if self.number_of_inputs == 10:
            self.add_function_button.destroy()

    def initial_numbers(self):
        self.init_nums = ttk.Entry(self, width=30)
        self.init_nums.grid(row=self.number_of_inputs + 3, column=0, columnspan=2, padx=10, pady=10)

    def add_button(self):
        self.add_function_button = ttk.Button(self, text="Add function", command=self.add_input)
        self.add_function_button.grid(row=self.number_of_inputs + 4, column=0, padx=10, pady=10)

    def handle_submit(self):
        funcs = [inp["input"].get() for inp in self.inputs]
        # nums = [[1, 1, 2, 3], [1, 2], [1.5, 2]]
        variables = ["x", "y"]
        nums = [int(x) for x in self.init_nums.get().split()]
        array, iters = newton_method(funcs=funcs, nums=nums, tolerance=10**-4, variables=variables)
        answer_string = ', '.join([str(x) for x in array]) + f"\tIterations: {iters}"
        answer = ttk.Label(self, text=answer_string)
        answer.grid(row=self.number_of_inputs + 5, column=1, padx=10, pady=10)

    def submit_button(self):
        self.sbmt_button = ttk.Button(self, text="Submit", command=self.handle_submit)
        self.sbmt_button.grid(row=self.number_of_inputs + 4, column=1, padx=10, pady=10)


# third window frame page2
class PageSecant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2")
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(PageNewton))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
app = TkinterApp()
app.mainloop()
