# Ex  1 Translating Newton's Square root method in python

def square(x):
    return x * x

def sqrt(x):
    def good_enough(guess, x):
        return abs(square(guess) - x) < 0.01

    def average(x, y):
        return (x + y) / 2

    def improve(guess, x):
        return average(guess, (x / guess))

    def sqrt_iter(guess, x):
        if good_enough(guess, x):
            return guess
        else:
            return sqrt_iter(improve(guess, x), x)

    return sqrt_iter(1.0, x)

ans = sqrt(2)

print(square(ans))
