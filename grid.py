from __future__ import annotations
from dataclasses import dataclass
from typing import List, Set, Tuple

Cell = Tuple[int, int]


@dataclass
class Grid:
    rows: int
    cols: int
    start: Cell
    target: Cell
    walls: Set[Cell]

    def in_bounds(self, c: Cell) -> bool:
        r, col = c
        return 0 <= r < self.rows and 0 <= col < self.cols

    def is_free(self, c: Cell) -> bool:
        return self.in_bounds(c) and c not in self.walls

    def neighbors(self, c: Cell) -> List[Cell]:
        r, col = c
        dirs = [
            (-1, 0),   # Up
            (-1, 1),   # Top-Right
            (0, 1),    # Right
            (1, 1),    # Bottom-Right
            (1, 0),    # Bottom
            (1, -1),   # Bottom-Left
            (0, -1),   # Left
            (-1, -1),  # Top-Left
        ]
        out: List[Cell] = []
        for dr, dc in dirs:
            nxt = (r + dr, col + dc)
            if self.is_free(nxt):
                out.append(nxt)
        return out

    def move_cost(self, a: Cell, b: Cell) -> float:
        ar, ac = a
        br, bc = b
        dr = abs(ar - br)
        dc = abs(ac - bc)
        return 1.4 if (dr == 1 and dc == 1) else 1.0


def demo_grid() -> Grid:
    rows, cols = 15, 20
    start = (2, 2)
    target = (12, 17)
    walls: Set[Cell] = set()

    for c in range(4, 16):
        walls.add((6, c))
    for r in range(1, 10):
        walls.add((r, 10))

    walls.discard((6, 12))
    walls.discard((6, 13))

    return Grid(rows=rows, cols=cols, start=start, target=target, walls=walls)
