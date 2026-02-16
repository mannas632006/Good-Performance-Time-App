from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Set

Cell = Tuple[int, int]


@dataclass
class SearchResult:
    found: bool
    came_from: Dict[Cell, Optional[Cell]]
    explored_order: List[Cell]
    frontier_history: List[Set[Cell]]  # snapshot each step


def reconstruct_path(came_from: Dict[Cell, Optional[Cell]], start: Cell, goal: Cell) -> List[Cell]:
    if goal not in came_from:
        return []
    path: List[Cell] = []
    cur: Optional[Cell] = goal
    while cur is not None:
        path.append(cur)
        cur = came_from.get(cur)
    path.reverse()
    if path and path[0] == start:
        return path
    return []


def path_blocked(path: List[Cell], walls: Set[Cell]) -> bool:
    return any(cell in walls for cell in path)
