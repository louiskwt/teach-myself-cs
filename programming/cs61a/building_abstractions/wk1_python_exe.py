# Ex  1 Translating Newton's Square root method in python

def square(x):
    return x * x

def sqrt(x):
    def good_enough(guess, x):
        return abs(square(guess) - x) < 0.001

    def average(x, y):
        return (x + y) / 2

    def improve(guess, x):
        return average(guess, (x / guess))

    def sqrt_iter(guess, x):
        if good_enough(guess, x):
            return round(guess, 3) 
        else:
            return sqrt_iter(improve(guess, x), x)

    return sqrt_iter(1.0, x)

sqrt(2)

print(square(sqrt(2)))

# writing square sum
def get_larger(x, y):
    if x < y:
        return y

    return x

def three_square_sum(x, y, z):
    lg_1 = get_larger(x, y)
    lg_2 = get_larger(y, z)

    if lg_1 == lg_2:
        lg_2 = get_larger(x, z)

    return square(lg_1) + square(lg_2)

ans_2 = three_square_sum(2, 4, 3)  # expect 25

# print(ans_2)
