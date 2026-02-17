from __future__ import annotations

import random
from typing import Callable, Dict, Optional, Set, Tuple

from grid import Grid, demo_grid
from visualizer import Visualizer

from search.common import SearchResult, reconstruct_path
from search.bfs import bfs
from search.dfs import dfs
from search.ucs import ucs
from search.dls import dls
from search.iddfs import iddfs
from search.bidir import bidirectional

Cell = Tuple[int, int]
AlgoFn = Callable[[Grid, Cell, Cell], SearchResult]

ALGOS: Dict[str, Optional[AlgoFn]] = {
    "bfs": bfs,
    "dfs": dfs,
    "ucs": ucs,
    "dls": None,
    "iddfs": iddfs,
    "bidir": bidirectional,
}


def animate_planning(viz: Visualizer, grid: Grid, result: SearchResult, algo_name: str, agent: Cell) -> None:
    explored_set: Set[Cell] = set()

    for i, cur in enumerate(result.explored_order):
        explored_set.add(cur)
        frontier = result.frontier_history[i] if i < len(result.frontier_history) else set()

        viz.render(
            walls=grid.walls,
            frontier=frontier,
            explored=explored_set,
            path=set(),
            start=grid.start,
            target=grid.target,
            agent=agent,
            subtitle=f"{algo_name.upper()} planning (step {i + 1})",
        )


def choose_algorithm() -> str:
    print("\nChoose an algorithm to visualize:")
    print("1) BFS")
    print("2) DFS")
    print("3) UCS")
    print("4) DLS")
    print("5) IDDFS")
    print("6) Bidirectional")
    choice = input("Enter number (1-6): ").strip()

    mapping = {
        "1": "bfs",
        "2": "dfs",
        "3": "ucs",
        "4": "dls",
        "5": "iddfs",
        "6": "bidir",
    }
    return mapping.get(choice, "bfs")


def main() -> None:
    random.seed(7)
    grid = demo_grid()
    viz = Visualizer(grid.rows, grid.cols, delay=0.03)

    algo_name = choose_algorithm()
    dls_limit = 25
    agent = grid.start

    try:
        if algo_name == "dls":
            result = dls(grid, agent, grid.target, limit=dls_limit)
        else:
            algo_fn = ALGOS.get(algo_name)
            if algo_fn is None:
                raise ValueError(f"Unknown algorithm: {algo_name}")
            result = algo_fn(grid, agent, grid.target)

        animate_planning(viz, grid, result, algo_name, agent)

        if not result.found:
            viz.render(
                walls=grid.walls,
                frontier=set(),
                explored=set(result.explored_order),
                path=set(),
                start=grid.start,
                target=grid.target,
                agent=agent,
                subtitle=f"{algo_name.upper()} could not find a path",
            )
            input("Press Enter to close...")
            return

        path_list = reconstruct_path(result.came_from, agent, grid.target)

        viz.render(
            walls=grid.walls,
            frontier=set(),
            explored=set(result.explored_order),
            path=set(path_list),
            start=grid.start,
            target=grid.target,
            agent=agent,
            subtitle=f"{algo_name.upper()} final path (length {len(path_list)})",
        )

        input("Press Enter to close...")

    finally:
        viz.close()


if __name__ == "__main__":
    main()
