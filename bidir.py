from __future__ import annotations
from collections import deque
from typing import Dict, List, Optional, Set, Tuple
from .common import SearchResult

Cell = Tuple[int, int]


def bidirectional(grid, start: Cell, goal: Cell) -> SearchResult:
    if start == goal:
        return SearchResult(True, {start: None}, [start], [{start}])

    q_s = deque([start])
    q_g = deque([goal])

    came_s: Dict[Cell, Optional[Cell]] = {start: None}
    came_g: Dict[Cell, Optional[Cell]] = {goal: None}

    explored_order: List[Cell] = []
    frontier_history: List[Set[Cell]] = []

    meet: Optional[Cell] = None

    while q_s and q_g:
        frontier_history.append(set(q_s) | set(q_g))

        cur_s = q_s.popleft()
        explored_order.append(cur_s)
        for nxt in grid.neighbors(cur_s):
            if nxt not in came_s:
                came_s[nxt] = cur_s
                q_s.append(nxt)
                if nxt in came_g:
                    meet = nxt
                    break
        if meet is not None:
            break

        cur_g = q_g.popleft()
        explored_order.append(cur_g)
        for nxt in grid.neighbors(cur_g):
            if nxt not in came_g:
                came_g[nxt] = cur_g
                q_g.append(nxt)
                if nxt in came_s:
                    meet = nxt
                    break
        if meet is not None:
            break

    if meet is None:
        merged = dict(came_s)
        merged.update({k: merged.get(k) for k in came_g.keys()})
        return SearchResult(False, merged, explored_order, frontier_history)

    came_from = dict(came_s)

    chain = []
    cur = meet
    while cur is not None:
        chain.append(cur)
        cur = came_g.get(cur)

    for i in range(len(chain) - 1):
        a = chain[i]
        b = chain[i + 1]
        came_from[b] = a

    return SearchResult(True, came_from, explored_order, frontier_history)
