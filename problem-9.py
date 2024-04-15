import math

def get_pythagorean(a, b):
    new_item = (a*a) + (b*b)
    return math.sqrt(new_item)

# define minimum values
a = 3
b = 4
c = get_pythagorean(a, b)

stop_loop = False
for a_change in range(3, 400):
    for b_change in range(4, 400):
        z = a_change + b_change + get_pythagorean(a_change, b_change)
        if z == 1000:
            result = a_change * b_change * get_pythagorean(a_change, b_change)
            print(result)
            stop_loop = True
            break
    if stop_loop:
        break
    