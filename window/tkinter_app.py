import tkinter as tk

from window.pages.page_newton import PageNewton
from window.pages.page_secant import PageSecant
from window.pages.start_page import StartPage


class TkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Equations solver")
        # self.state('zoomed')

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = []

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, PageNewton, PageSecant):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames.append(frame)

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(0)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def start_tkinter():
    app = TkinterApp()
    app.mainloop()

