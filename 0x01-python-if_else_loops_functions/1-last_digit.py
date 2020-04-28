#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = abs(number) % 10
if number < 6 and number != 0:
    if i == 0:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
              .format(number, i))
    else:
        print("Last digit of {:d} is -{:d} and is less than 6 and not 0"
              .format(number, i))
elif number > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, i))
else:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, i))
