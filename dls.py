from __future__ import annotations
from typing import Dict, List, Optional, Set, Tuple
from .common import SearchResult

Cell = Tuple[int, int]


def dls(grid, start: Cell, goal: Cell, limit: int) -> SearchResult:
    stack: List[Tuple[Cell, int]] = [(start, 0)]
    came_from: Dict[Cell, Optional[Cell]] = {start: None}
    explored_order: List[Cell] = []
    frontier_history: List[Set[Cell]] = []

    while stack:
        frontier_history.append({c for c, _ in stack})
        cur, depth = stack.pop()
        explored_order.append(cur)

        if cur == goal:
            return SearchResult(True, came_from, explored_order, frontier_history)

        if depth == limit:
            continue

        for nxt in grid.neighbors(cur):
            if nxt not in came_from:
                came_from[nxt] = cur
                stack.append((nxt, depth + 1))

    return SearchResult(False, came_from, explored_order, frontier_history)
