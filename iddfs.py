from __future__ import annotations
from typing import Tuple
from .dls import dls
from .common import SearchResult

Cell = Tuple[int, int]


def iddfs(grid, start: Cell, goal: Cell, max_depth: int = 50) -> SearchResult:
    combined_explored = []
    combined_frontier = []
    last = None

    for limit in range(max_depth + 1):
        res = dls(grid, start, goal, limit)
        combined_explored.extend(res.explored_order)
        combined_frontier.extend(res.frontier_history)
        last = res
        if res.found:
            # return with combined history so GUI shows the "iterative" behavior
            res.explored_order = combined_explored
            res.frontier_history = combined_frontier
            return res

    # not found
    if last is None:
        return SearchResult(False, {start: None}, [], [])
    last.explored_order = combined_explored
    last.frontier_history = combined_frontier
    return last
