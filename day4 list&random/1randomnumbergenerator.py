#use askpython.com and khanacademy.org
#use import random module to use random number generator
import random

random_integer = random.randint(1, 9)

print(random_integer)

#generates from [0.0, 1.0) excluding 1
random_float = random.random()

print(random_float)

#to get number from 0.00, to 4.00 or [0.00, 5.00)
#as
# 0.1*5 = 0.5
# 0.4*5 = 2.0
#0.9*5 = 4.5

from0to5 = random_float * 5
print(from0to5)