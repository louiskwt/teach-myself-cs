# Implement Newton-Raphson method for square root
def square_root(x: int) -> float:
    if x == 0:
        return 0.0
    
    g: float = 1.0
    epsilon: float = 0.01
    diff: float = abs(x - (g**2))
    while diff > epsilon:
        g = (g + x / g) / 2
        diff = abs(x - g**2)
    return round(g, 3)


while True:
    try:
        x = float(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a number!")

if x < 0:
    print("Error: Negative numbers don't have real square roots.")
else:
    print(f'The approximate square root of {x} is {square_root(x)}')