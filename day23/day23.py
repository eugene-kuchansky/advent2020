import sys
from typing import Iterable, Tuple, List, Dict, Set, Optional


class Cup:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional[Cup] = None


def get_cups(numbers: List[int]) -> Tuple[Cup, Dict[int, Cup]]:
    cups: List[Cup] = [Cup(number) for number in numbers]

    for i, cup in enumerate(cups[:-1]):
        cup.next = cups[i + 1]

    cups[-1].next = cups[0]
    pointers = {cup.value: cup for cup in cups}
    return cups[0], pointers


def read_data(stream: Iterable[str]) -> Tuple[Cup, Dict[int, Cup], List[int]]:
    raw = [line.strip() for line in stream][0]
    numbers = [int(number) for number in raw]
    cup, pointers = get_cups(numbers)
    return cup, pointers, numbers


def get_destination_value(current_cup: Cup, pickup_values: Set[int], min_number: int, max_number: int) -> int:
    destination_value = current_cup.value
    while True:
        destination_value -= 1
        if destination_value < min_number:
            destination_value = max_number
        if destination_value not in pickup_values:
            break
    return destination_value


def make_move(current_cup: Cup, pointers: Dict[int, Cup], min_number: int, max_number: int) -> Cup:
    # get pointers to first and last pickups
    first_pickup = current_cup.next
    last_pickup = first_pickup.next.next

    # remove pickups
    current_cup.next = last_pickup.next

    # get dest value which is not in pickups
    pickup_values = {first_pickup.value, first_pickup.next.value, last_pickup.value}
    destination_value = get_destination_value(current_cup, pickup_values, min_number, max_number)

    destination_cup = pointers[destination_value]

    # insert pickups next to destination
    last_pickup.next = destination_cup.next
    destination_cup.next = first_pickup

    return current_cup.next


def print_cups(current_cup: Cup):
    current_value = current_cup.value
    cup = current_cup
    while cup.next.value != current_value:
        print(cup.value, end=" ")
        cup = cup.next
    print(cup.value, end=" ")
    print()


def get_result1(cup: Cup) -> str:
    while cup.value != 1:
        cup = cup.next
    values = []
    cup = cup.next
    while cup.value != 1:
        values.append(cup.value)
        cup = cup.next
    return "".join([str(value) for value in values])


def get_result2(pointers: Dict[int, Cup]) -> int:
    cup1 = pointers[1]
    return cup1.next.value * cup1.next.next.value


def calc1(cup: Cup, pointers: Dict[int, Cup]) -> str:
    numbers = list(pointers.keys())
    min_number = min(numbers)
    max_number = max(numbers)

    # print(1, end=": ")
    # print_cups(cup)
    for i in range(100):
        # print(f"-- move {i + 1} --")
        # print("cups: ", end="")
        # print_cups(cup)
        cup = make_move(cup, pointers, min_number, max_number)
        # print()

    # print_cups(cup)
    return get_result1(cup)


def calc2(init_numbers: List[int]) -> int:
    total_numbers = 1000000
    max_number = max(init_numbers)
    other_numbers = [i for i in range(max_number+1, total_numbers+1)]
    numbers = init_numbers + other_numbers

    cup, pointers = get_cups(numbers)

    min_number = min(init_numbers)
    max_number = total_numbers

    for i in range(10000000):
        cup = make_move(cup, pointers, min_number, max_number)
    return get_result2(pointers)


if __name__ == "__main__":
    initial_cup, initial_pointers, initial_numbers = read_data(sys.stdin)
    res1 = calc1(initial_cup, initial_pointers)
    print(f"result 1: {res1}")

    res2 = calc2(initial_numbers)
    print(f"result 2: {res2}")
