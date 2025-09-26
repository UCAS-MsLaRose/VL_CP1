# VL 2nd Debugging Notes

# Syntax Error - Grammar error
    #print"Ms. LaRose"
# Fix by => reading where the problem is AND fixing it!

# Logic Error - The computer has the wrong steps
num = "10"
num_two = "3"

print(num+num_two)


# Run-Time Errors - The code will start running and it will not finish
import random

while True:
    denomenator = random.randint(0,5)

    print(10/denomenator)