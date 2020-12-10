import sys
from typing import List, NamedTuple, Iterable
from collections import defaultdict
import math


def read_data(stream: Iterable[str]) -> List[int]:
    return [int(line.strip()) for line in stream]


def calc1(adapters: List[int]) -> List[int]:
    adapters.append(0)
    adapters.sort()
    device_adapter = adapters[-1] + 3
    adapters.append(device_adapter)
    diffs = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
    return diffs


def calc2(diffs: List[int]) -> int:
    cnt = defaultdict(int)
    subsequence = []
    for diff in diffs:
        if diff != 3:
            subsequence.append(diff)
        else:
            if len(subsequence) > 1:
                cnt[len(subsequence)] += 1
            subsequence = []
    return int(math.pow(7, cnt[4])) * int(math.pow(4, cnt[3])) * int(math.pow(2, cnt[2]))



if __name__ == "__main__":
    initial_data = read_data(sys.stdin)
    # initial_data = read_data(ADAPTERS.split("\n"))

    diffs = calc1(initial_data)
    print(f"result 1: {diffs.count(3) * diffs.count(1)}")

    res2 = calc2(diffs)
    print(f"result 2: {res2}")
    # 2 -> 2
    # 3 -> 4
    # 4 -> 7
    #
    # 4 - 4
    # 3 - 1
    # 2 - 1
