# VL 2nd Random Numbers Notes
import random

# Examples of random numbers
print(random.random()) # Float between 0 and 1
print(random.randint(1, 6)) 


name = input("What is your name: \n").strip().title()

# Random Stat Creater D&D
stat_one = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_two = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_three = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_four = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_five = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_six = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_seven = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

# Set Individual Stats
strength = int(input("Which stat are you making your strength")) + 2