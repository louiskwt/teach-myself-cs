def check_strategy():
    # Opp -->  Rock (A) Paper (B) Scissor (C)
    # Me --> Roack (X) 1 Paper (Y) 2 Scissor (Z) 3
    # outcome --> L (0)  D(3)  W(6)
    try:
        strategy_guide = open("day_2_input.txt", "r").read().split("\n")
        strategy_lst = [line.split(" ") for line in strategy_guide if line != ""]
        options_dict = {
            "X": 1,
            "Y": 2,
            "Z": 3
        }
        total_score = 0
        for round in strategy_lst:
            opp, me = round
            total_score += (options_dict[me] + calculate_outcome(opp, me))
            
        return total_score 
    except IOError:
        print("Error with opening file")
        return 0

def calculate_outcome(opp, me):
    win_dict = {
        "Y": "A",
        "X": "C",
        "Z": "B"
    }

    draw_dict = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }

    if draw_dict[me] == opp:
        return 3
    elif win_dict[me] == opp:
        return 6
    else:
        return 0
    


ans = check_strategy()
print(ans)
