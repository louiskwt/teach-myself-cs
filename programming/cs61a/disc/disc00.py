# Q1 What is the value of the final expression in this sequence?
f = min
f = max
g, h = min, max
max = g   # g = min, so max = g = min | f = max
max(f(2, g(h(1, 5), 3)), 4)

"""
h(1, 5)  h = max >> 5
g(5, 3) g = min >> 3
f(2, 3) f = max >> 3
max(3, 4) max = min >> 3

Ans = 3  ok
"""


