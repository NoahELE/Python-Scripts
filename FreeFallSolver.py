import math

import sympy


g = -10
m = sympy.Symbol("m")
h = sympy.Symbol("h")
t = sympy.Symbol("t")
v0 = sympy.Symbol("v0")
equations = [v0 * t + 1 / 2 * g * t ** 2 - h, v0 - 0, m - 0.73, h - 1.6]

print(sympy.solve(equations, m, h, t, v0))
