#!/usr/bin/env python3
import itertools
import sys
from collections import deque
from typing import Deque, List, Optional, Sequence


def main():
    game = NoughtsAndCrosses()

    print("Input a square from 1-9 to move.")

    while not game.finished():
        print(f"{game.turn} to play: ", end="")
        sys.stdout.flush()

        try:
            action = int(sys.stdin.readline())
        except ValueError:
            print("Invalid position")
        else:
            game.move(action)
            game.display()

    game.display_result()


class NoughtsAndCrosses:
    def __init__(self):
        self._turns: Deque = deque(("X", "O"))
        self.position: List = [None] * 9

    @property
    def turn(self) -> str:
        return self._turns[0]

    def move(self, action: int):
        if self.position[action - 1]:
            print("Square already occupied")
            return

        self.position[action - 1] = self._turns[0]
        self._turns.rotate()

    def finished(self) -> bool:
        return self.winner() or all(self.position)

    def winner(self) -> Optional[str]:
        for pos in range(3):
            if self._has_winner(pos):
                return self.position[pos]

    def _has_winner(self, pos: int) -> bool:
        return (
            self._is_line_equal([pos * 3 + j for j in range(3)])
            or self._is_line_equal([pos + j * 3 for j in range(3)])
            or self._is_line_equal((0, 4, 8))
            or self._is_line_equal((2, 4, 6))
        )

    def _is_line_equal(self, line_pos: Sequence[int]) -> bool:
        set_items = {self.position[i] for i in line_pos}
        return len(set_items) == 1 and set_items != {None}

    def display(self):
        for i in range(3):
            for j in range(3):
                print(self.position[i * 3 + j] or " ", end="")
                if j < 2:
                    print("|", end="")
            print()

    def display_result(self):
        print(f"{self.winner()} wins!" if self.winner() else "Draw")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
