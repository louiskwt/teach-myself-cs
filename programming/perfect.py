####################
## TEST YOURSELF!
## Modify the perfect squares example to print 
## imaginary perfect sqrts if given a negative num.
####################
ans, neg_flag = 0, False
while True:
    try:
        x = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Input must be an integer")
    
neg_flag = x < 0

while ans**2 < abs(x):
    ans = ans + 1
if ans**2 == abs(x):
    if neg_flag:
        ans = f'{ans}i'
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")

