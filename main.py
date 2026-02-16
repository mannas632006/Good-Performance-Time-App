from __future__ import annotations
import random
from typing import Callable, Dict, List, Set, Tuple, Optional

from grid import demo_grid, Grid
from visualizer import Visualizer

from search.common import reconstruct_path, path_blocked
from search.bfs import bfs
from search.dfs import dfs
from search.ucs import ucs
from search.dls import dls
from search.iddfs import iddfs
from search.bidir import bidirectional

Cell = Tuple[int, int]


ALGOS: Dict[str, Callable] = {
    "bfs": bfs,
    "dfs": dfs,
    "ucs": ucs,
    "dls": None,       # handled separately
    "iddfs": iddfs,
    "bidir": bidirectional,
}


def animate_planning(viz: Visualizer, grid: Grid, result, algo_name: str, agent: Cell):
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
            subtitle=f"{algo_name.upper()} planning (step {i+1})",
        )


def main():
    random.seed(7)
    grid = demo_grid()
    viz = Visualizer(grid.rows, grid.cols, delay=0.03)

    algo_name = "bfs"   # CHANGE THIS: bfs/dfs/ucs/dls/iddfs/bidir
    dls_limit = 25      # only used for DLS

    agent = grid.start

    # dynamic obstacle probability each move step
    spawn_prob = 0.05

    try:
        while agent != grid.target:
            # --- PLAN ---
            if algo_name == "dls":
                result = dls(grid, agent, grid.target, limit=dls_limit)
            else:
                algo_fn = ALGOS[algo_name]
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
                break

            path_list = reconstruct_path(result.came_from, agent, grid.target)
            if not path_list:
                break

            # show final planned path briefly
            viz.render(
                walls=grid.walls,
                frontier=set(),
                explored=set(result.explored_order),
                path=set(path_list),
                start=grid.start,
                target=grid.target,
                agent=agent,
                subtitle=f"{algo_name.upper()} planned path (length {len(path_list)})",
            )

            # --- EXECUTE (move one step) ---
            # path_list includes agent as first node
            if len(path_list) >= 2:
                next_cell = path_list[1]
            else:
                next_cell = agent

            # dynamic obstacle spawn
            if random.random() < spawn_prob:
                forbidden = {grid.start, grid.target, agent, next_cell}
                spawned = grid.spawn_dynamic_obstacle(forbidden)
                if spawned is not None:
                    viz.render(
                        walls=grid.walls,
                        frontier=set(),
                        explored=set(),
                        path=set(path_list),
                        start=grid.start,
                        target=grid.target,
                        agent=agent,
                        subtitle=f"Dynamic obstacle spawned at {spawned}",
                    )

            # if next step is blocked now, re-plan (loop continues)
            if next_cell in grid.walls:
                viz.render(
                    walls=grid.walls,
                    frontier=set(),
                    explored=set(),
                    path=set(),
                    start=grid.start,
                    target=grid.target,
                    agent=agent,
                    subtitle="Next step blocked → replanning",
                )
                continue

            # move agent
            agent = next_cell
            viz.render(
                walls=grid.walls,
                frontier=set(),
                explored=set(),
                path=set(path_list),
                start=grid.start,
                target=grid.target,
                agent=agent,
                subtitle="Agent moved 1 step",
            )

        # done
        viz.render(
            walls=grid.walls,
            frontier=set(),
            explored=set(),
            path=set(),
            start=grid.start,
            target=grid.target,
            agent=agent,
            subtitle="DONE",
        )
        input("Press Enter to close...")

    finally:
        viz.close()


if __name__ == "__main__":
    main()
