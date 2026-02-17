from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Set, Tuple

Cell = Tuple[int, int]


class Visualizer:
    def __init__(self, rows: int, cols: int, delay: float = 0.03):
        self.rows = rows
        self.cols = cols
        self.delay = delay

        self.fig, self.ax = plt.subplots()
        self.fig.suptitle("GOOD PERFORMANCE TIME APP")
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.im = None

        self.cmap = plt.cm.get_cmap("tab20", 8)

    def render(
        self,
        walls: Set[Cell],
        frontier: Set[Cell],
        explored: Set[Cell],
        path: Set[Cell],
        start: Cell,
        target: Cell,
        agent: Optional[Cell],
        subtitle: str,
    ):
        grid = np.zeros((self.rows, self.cols), dtype=int)

        for r, c in walls:
            grid[r, c] = 1
        for r, c in explored:
            if grid[r, c] == 0:
                grid[r, c] = 3
        for r, c in frontier:
            if grid[r, c] == 0:
                grid[r, c] = 2
        for r, c in path:
            if grid[r, c] == 0:
                grid[r, c] = 4

        sr, sc = start
        tr, tc = target
        grid[sr, sc] = 5
        grid[tr, tc] = 6

        if agent is not None:
            ar, ac = agent
            grid[ar, ac] = 7

        self.ax.set_title(subtitle)

        if self.im is None:
            self.im = self.ax.imshow(
                grid, cmap=self.cmap, vmin=0, vmax=7, interpolation="nearest"
            )
            self._setup_cell_gridlines()
        else:
            self.im.set_data(grid)

        plt.pause(self.delay)

    def _setup_cell_gridlines(self):
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.ax.set_xticks(np.arange(-0.5, self.cols, 1), minor=True)
        self.ax.set_yticks(np.arange(-0.5, self.rows, 1), minor=True)

        self.ax.grid(which="minor", linestyle="-", linewidth=0.6, color="black")
        self.ax.tick_params(which="minor", bottom=False, left=False)

    def close(self):
        plt.close(self.fig)
