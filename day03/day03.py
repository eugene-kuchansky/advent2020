import sys
from collections import namedtuple
from typing import List
import math

TREE = "#"
SPACE = "."

Move = namedtuple("Move", "right down")
PositionTuple = namedtuple("Position", "x y")

class Position(PositionTuple):
    # def __init__(self, width: int, height: int):
    #     self.x = 0
    #     self.y = 0
    #     self._width = width
    #     self._height = height
    def next_position(self, move: Move, area: "Area") -> "Position":
        # next_position = Position(self._width, self._height)
        x = self.x + move.right
        y = self.y + move.down
        if x >= area.width:
            x = x - area.width
        return Position(x, y)

    def is_bottom(self, area: "Area") -> bool:
        return self.y >= area.height


class Area:
    def __init__(self, data: List[str]):
        self._area = data
        self.width = len(self._area[0])
        self.height = len(self._area)

    def on_position(self, position: Position) -> str:
        return self._area[position.y][position.x]

    def __str__(self):
        return "\n".join(self._area)


def read_data() -> List[str]:
    return [line.strip() for line in sys.stdin]


def calc1(area: Area, move: Move):
    position = Position(0, 0)
    trees = 0
    while not position.is_bottom(area):
        if area.on_position(position) == TREE:
            trees += 1
        position = position.next_position(move, area)
    return trees


if __name__ == "__main__":
    raw_data = read_data()
    tree_area = Area(raw_data)
    move1 = Move(right=3, down=1)
    res1 = calc1(tree_area, move1)
    print(f"result 1: {res1}")

    moves = [
        Move(right=1, down=1),
        Move(right=5, down=1),
        Move(right=7, down=1),
        Move(right=1, down=2),
    ]
    res2 = res1
    for move2 in moves:
        res = calc1(tree_area, move2)
        res2 *= res

    print(f"result 2: {res2}")
