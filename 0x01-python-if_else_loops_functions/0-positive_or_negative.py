#!/usr/bin/python3
import random
number = random.ranint(-10, 10)
if number > 0:
    print("{} is positive".format(numer))
elif number == 0:
    print("{} is Zero".format(number))
elif number < 0:
    print("{} is Negative".format(number))
