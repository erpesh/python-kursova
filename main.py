from sympy import Symbol, Eq
from sympy.plotting import plot

from solving.graph import plot_graph
from solving.secant import secant_method
from window.tkinter_app import start_tkinter

if __name__ == '__main__':
    start_tkinter()
    # plot_graph(["sin(x)+cos(y)=1/2", "cos((x-y)/2)=3**0.5/2"], ['x', 'y'])
    # x = Symbol('x')
    # y = Symbol('y')
    # eqs = ["x**2+y**2=20", "x**2-y**2=-2"]
    # print([eval(part) for part in eqs[1].split('=')])
