# VL 1st Period While Loops Notes
import time
import random
# infinite loop
num = 1

while num <= 20:
    print(num)
    num += 1 #Prevents an infinite loop
else:
    print("The condition was met")

goose = random.randint(1,20)
count = 0

while count != goose:
    count += 1
    print("duck")
    """if count == goose:
        break
    else:"""
    if count == 6:
        break
else:
    print("GOOSE!")

print("The code is done")


i = 0

while i < 20:
    i+= 1
    if i == 10:
        print("i is 10")
        continue
    else:
        print(f"{i} iteration of the loop")


print("The loop ended!")

hang_man =""" _______
    |     O
    |    /|\\
    |    /\\
    |
    |________
"""
print(hang_man)