## This program (i) prints the real solutions (if any) of a second degree polynomial given its coefficients.
## (ii) It had an oversight that causes a division by zero error when a is 0. This has since been fixed and handles all possible cases.

import sys
import math
def do_stuff():
    a = float(sys.argv[1])
    if a == 0:
        print("Cannot divide by zero, enter a different value for a.")
        exit(1)
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}')
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}')
    else:
        print('There are no real solutions.')


do_stuff()