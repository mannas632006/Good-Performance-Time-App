from __future__ import annotations
import heapq
from typing import Dict, Optional, Set, Tuple, List
from .common import SearchResult

Cell = Tuple[int, int]


def ucs(grid, start: Cell, goal: Cell) -> SearchResult:
    heap: List[Tuple[float, Cell]] = [(0.0, start)]
    came_from: Dict[Cell, Optional[Cell]] = {start: None}
    best_g: Dict[Cell, float] = {start: 0.0}
    explored_order: List[Cell] = []
    frontier_history: List[Set[Cell]] = []

    while heap:
        frontier_history.append({cell for _, cell in heap})
        g, cur = heapq.heappop(heap)

        # ignore outdated heap entries
        if g != best_g.get(cur, float("inf")):
            continue

        explored_order.append(cur)

        if cur == goal:
            return SearchResult(True, came_from, explored_order, frontier_history)

        for nxt in grid.neighbors(cur):
            new_g = g + grid.move_cost(cur, nxt)
            if new_g < best_g.get(nxt, float("inf")):
                best_g[nxt] = new_g
                came_from[nxt] = cur
                heapq.heappush(heap, (new_g, nxt))

    return SearchResult(False, came_from, explored_order, frontier_history)
