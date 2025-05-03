# Random Generator
# Only for fan.
# ver 01
# Andrey Glushchenko (c)
import random

dim = []
dim_max = 69
count_n = 5
dim_max2 = 26
point = 0


def random_n():
    while True:
        val1 = random.randint(1, dim_max)
        if val1 in dim:
            continue
        else:
            dim.append(val1)
            break


def count_val():
    for i in range(count_n):
        random_n()
    point_plus = random.randint(1, dim_max2)
    dim.sort()
    print(f'Result: {dim} - {point_plus}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count_val()
