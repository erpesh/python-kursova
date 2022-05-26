import tkinter as tk
from tkinter import ttk


# class InitialWindow:
#     def __init__(self, master):
#         self.error_label = None
#         self.inputs_list = None
#         self.function_submit = None
#
#         self.master = master
#         self.master.title("Equation Solver")
#
#         self.entry = tk.Entry(master, width=10, borderwidth=5)
#         self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#
#         self.my_button = tk.Button(master, text="Submit", command=self.refresh)
#         self.my_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
#
#     def refresh(self):
#         # FunctionsInput(self.master, self.entry.get())
#         self.my_button.destroy()
#         self.entry.destroy()
#         if self.error_label is not None:
#             self.error_label.destroy()
#         ChooseMethod(self.master)
#
#
# class ChooseMethod(InitialWindow):
#     def __init__(self, master):
#         super().__init__(master)
#
#         self.var1 = tk.IntVar()
#         self.var2 = tk.IntVar()
#         self.chec1 = tk.Checkbutton(self.master, text="Метод Ньютона", variable=self.var1, onvalue=1, offvalue=0,
#                                     command=self.print_selection)
#         self.chec1.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
#         self.chec2 = tk.Checkbutton(self.master, text="Метод січних", variable=self.var2, onvalue=1, offvalue=0,
#                                     command=self.print_selection)
#         self.chec2.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
#
#     def print_selection(self):
#         print(self.var1.get(), self.var2.get())
#         if (self.var1.get() == 1) & (self.var2.get() == 0):
#             print('I love Python ')
#         elif (self.var1.get() == 0) & (self.var2.get() == 1):
#             print('I love C++')
#         elif (self.var1.get() == 0) & (self.var2.get() == 0):
#             print('I do not anything')
#         else:
#             print('I love both')
#
#     def refresh_to_choose_window(self):
#         pass
#
#
# class FunctionsInput(ChooseMethod):
#     def __init__(self, master, number):
#         super().__init__(master)
#         self.refresh_window(number)
#
#     def function_input(self, i):
#         input_label_dct = {
#             "input": tk.Entry(self.master, width=50, borderwidth=5),
#             "label": tk.Label(self.master, text=f"Enter function number {i + 1}")
#         }
#         self.inputs_list.append(input_label_dct)
#         self.inputs_list[i]["label"].grid(row=i, column=0, columnspan=2, padx=10, pady=10)
#         self.inputs_list[i]["input"].grid(row=i, column=2, columnspan=3, padx=10, pady=10)
#
#     def refresh_window(self, number):
#         self.inputs_list = list()
#         n = number
#         try:
#             n = int(n)
#             if n < 2 or n > 10:
#                 raise ValueError
#
#             for i in range(int(n)):
#                 self.function_input(i)
#
#             self.function_submit = tk.Button(self.master, text="Submit", command=self.submit_functions)
#             self.function_submit.grid(row=len(self.inputs_list) + 1, column=0, columnspan=5, padx=10, pady=10)
#
#             self.my_button.destroy()
#             self.entry.destroy()
#             if self.error_label is not None:
#                 self.error_label.destroy()
#
#         except ValueError:
#             self.error_label = tk.Label(self.master, text="Enter integer between 2 and 10!")
#             self.error_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
#
#     def submit_functions(self):
#         functions = [element["input"].get() for element in self.inputs_list]
#         newL = tk.Label(self.master, text=functions)
#         newL.grid(row=len(self.inputs_list) + 2, column=0, columnspan=5, padx=10, pady=10)
#
#
# def open_window():
#     root = tk.Tk()
#     root.title("window")
#     root.geometry("650x350")
#     cls = InitialWindow(root)
#     root.mainloop()


