"""
Exponential sum functions.

Examples
--------
>>> python expsum func1 2000 10 7 17
>>> python expsum func1 8000 11 21 31
>>> python expsum func2 1200 100
>>> python expsum func2 4000 800
>>> python expsum func3 1000
>>> python expsum func3 4000
>>> python expsum func4 4000 4
>>> python expsum func5 4000 50 100
>>> python expsum func6 2000 4
>>> python expsum func7 8000 4
"""
import argparse
import numpy as np
import functions
import plotter


def main():

    choices = ['func1', 'func2', 'func3', 'func4', 'func5', 'func6', 'func7']

    parser = argparse.ArgumentParser()
    parser.add_argument('fn', help='function to plot', choices=choices)
    parser.add_argument('vars', nargs='*', type=int, help='function variables')
    parser.add_argument('-a', '--anim', action='store_true', help='animate plot')
    args = parser.parse_args()

    if args.fn == 'func1':
        nt, a, b, c = args.vars
        func = functions.func1
        z = np.array([np.exp(2 * np.pi * 1j * func(n, a, b, c)) for n in range(1, nt + 1)])

    if args.fn == 'func2':
        nt, a = args.vars
        func = functions.func2
        z = np.array([np.exp(2 * np.pi * 1j * func(n, a)) for n in range(1, nt + 1)])

    if args.fn == 'func3':
        nt, = args.vars
        func = functions.func3
        z = np.array([np.exp(2 * np.pi * 1j * func(n)) for n in range(1, nt + 1)])

    if args.fn == 'func4':
        nt, a = args.vars
        func = functions.func4
        z = np.array([np.exp(2 * np.pi * 1j * func(n, a)) for n in range(1, nt + 1)])

    if args.fn == 'func5':
        nt, a, b = args.vars
        func = functions.func5
        z = np.array([np.exp(2 * np.pi * 1j * func(n, a, b)) for n in range(1, nt + 1)])

    if args.fn == 'func6':
        nt, a = args.vars
        func = functions.func6
        z = np.array([np.exp(2 * np.pi * 1j * func(n, a)) for n in range(1, nt + 1)])

    if args.fn == 'func7':
        nt, a = args.vars
        func = functions.func7
        z = np.array([np.exp(2 * np.pi * 1j * func(n, a)) for n in range(1, nt + 1)])

    z = z.cumsum()

    plotter.plot_expsum(z)
    if args.anim:
        plotter.animate_expsum(z)
    plotter.show()


if __name__ == '__main__':
    main()
