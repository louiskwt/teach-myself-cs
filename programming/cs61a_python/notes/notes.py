# defining function
from operator import mul

def square(x):  # formal parameter / signature
    return mul(x, x) # not evaluated right away

print(square(5))
# in env diagram
# import --> func mul(...) not explicitly defined signature
# function --> func square(x)
# invoking func generates a local frame with its own bindings
# ----square 
# ------ x [2]
# ------ return value 4

def pressure(v, t, n):
        """Compute the pressure in pascals of an ideal gas.

        Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v

help(pressure)
