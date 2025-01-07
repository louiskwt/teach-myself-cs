####################
## EXAMPLE: while loops 
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use a counter
####################
face = "٩( ๑╹ ꇴ╹)۶"
n = input(f"You are in the Lost Forest\n****************\n****************\n {face} \n****************\n****************\nGo left or right? ").lower()
count = 0

while n == "right" or n == "Right":
    count += 1
    tree = "*******"
    if count == 1:
        face = "( •͡˘ _•͡˘)"
    elif count == 2:
        face = "	(╥﹏╥)"
    elif count >= 3:
        face = " ヽ(`Д´)ﾉ︵ ┻━┻"
        tree = "       "

    n = input(f"You are in the Lost Forest\n****************\n******{tree}***\n  {face}\n****************\n****************\nGo left or right? ")

print("\nYou got out of the Lost Forest!\n\(^-^)/")