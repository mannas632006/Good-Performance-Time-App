from __future__ import annotations
from dataclasses import dataclass
import random
from typing import Iterable, List, Tuple, Set, Optional

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
        """
        Strict clockwise order including ALL diagonals:
        1 Up, 2 Top-Right, 3 Right, 4 Bottom-Right,
        5 Bottom, 6 Bottom-Left, 7 Left, 8 Top-Left
        """
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
        # diagonal move cost higher than straight
        ar, ac = a
        br, bc = b
        dr = abs(ar - br)
        dc = abs(ac - bc)
        if dr == 1 and dc == 1:
            return 1.4
        return 1.0

    def spawn_dynamic_obstacle(self, forbidden: Set[Cell]) -> Optional[Cell]:
        """
        Pick a random empty cell not in forbidden and turn it into a wall.
        Returns the cell if spawned, else None.
        """
        candidates: List[Cell] = []
        for r in range(self.rows):
            for c in range(self.cols):
                cell = (r, c)
                if cell in self.walls:
                    continue
                if cell in forbidden:
                    continue
                candidates.append(cell)

        if not candidates:
            return None

        new_wall = random.choice(candidates)
        self.walls.add(new_wall)
        return new_wall


def demo_grid() -> Grid:
    """
    A simple map you can change later.
    """
    rows, cols = 15, 20
    start = (2, 2)
    target = (12, 17)
    walls: Set[Cell] = set()

    # some static walls
    for c in range(4, 16):
        walls.add((6, c))
    for r in range(1, 10):
        walls.add((r, 10))
    # add a gap
    walls.discard((6, 12))
    walls.discard((6, 13))

    return Grid(rows=rows, cols=cols, start=start, target=target, walls=walls)
