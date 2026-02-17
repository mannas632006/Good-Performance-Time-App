from __future__ import annotations
from collections import deque
from typing import Dict, List, Optional, Set, Tuple
from .common import SearchResult

Cell = Tuple[int, int]


def bfs(grid, start: Cell, goal: Cell) -> SearchResult:
    q = deque([start])
    came_from: Dict[Cell, Optional[Cell]] = {start: None}
    explored_order: List[Cell] = []
    frontier_history: List[Set[Cell]] = []

    while q:
        frontier_history.append(set(q))
        cur = q.popleft()
        explored_order.append(cur)

        if cur == goal:
            return SearchResult(True, came_from, explored_order, frontier_history)

        for nxt in grid.neighbors(cur):
            if nxt not in came_from:
                came_from[nxt] = cur
                q.append(nxt)

    return SearchResult(False, came_from, explored_order, frontier_history)
