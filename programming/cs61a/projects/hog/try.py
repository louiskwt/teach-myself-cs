import hog

always_one = hog.make_test_dice(1)
always_two = hog.make_test_dice(2)
always_three = hog.make_test_dice(3)
always = hog.always_roll

# example 2

s0, s1 = hog.play(always(2), always(1), score0=0, score1=0, goal=5, dice=hog.make_test_dice(2, 2))

print(s0, s1)