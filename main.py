# Generator of numbers for a lotteries
# Only for fan.
# Clearly, there are no guarantees that these are the numbers that will win. )))
# This example simply gives my experience with python.
# ver 01
# Andrey Glushchenko (c), 2024
import random

DIM = set()

L_PB = {'name': 'Powerball', 'max': 69, 'qnt': 5, 'last': 26}
L_MM = {'name': 'MegaMillion', 'max': 70, 'qnt': 5, 'last': 25}
L_Lot = {'name': 'Lotto', 'max': 50, 'qnt': 6, 'last': 1}


def get_random_val(limit: int) -> int:
    """
    Generation of random value from 1 to 'limit'
    :param : int, limit
    :return: int, generated value
    """
    return random.randint(1, limit)


def random_add(count_m: int, max_v: int) -> None:
    """
    Function for adding a unique value to DIM
    :param max_v: int, maximum value
    :param count_m: int, quantity of element in the set
    :return: None
    """
    i = 0
    while True:
        val1 = get_random_val(max_v)
        DIM.add(val1)
        if i == len(DIM):
            continue
        else:
            i += 1
            if len(DIM) == count_m:
                break


def count_val(lot: dict) -> None:
    """
    Main function. Generation and printing results
    :param lot: dict, dict of lottery
    :return: None
    """
    name_l = lot.get("name")
    max_v = lot.get("max")
    cnt = lot.get("qnt")
    max_2 = lot.get("last")
    random_add(cnt, max_v)
    point_plus = get_random_val(max_2)
    sorted(DIM)
    if max_2 > 1:
        print(f'Result {name_l}: {DIM} - {point_plus}')
    else:
        print(f'Result {name_l}: {DIM}')
    DIM.clear()


if __name__ == '__main__':
    count_val(L_PB)
    count_val(L_MM)
    count_val(L_Lot)
