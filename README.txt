GOOD PERFORMANCE TIME APP
Uninformed Search Visualization in a Dynamic Grid Environment

This project is an AI Pathfinder that demonstrates how different uninformed (blind) search algorithms explore a grid.
It visually shows how each algorithm “thinks” step-by-step while navigating from a Start point (S) to a Target point (T), avoiding both static and dynamic obstacles.

Unlike traditional static pathfinding demos, this system includes dynamic hurdles that may randomly appear while the agent is moving. When that happens, the agent detects the blockage and automatically re-plans a new path.

Implemented Algorithms

The following uninformed search algorithms are implemented:

Breadth-First Search (BFS)

Depth-First Search (DFS)

Uniform-Cost Search (UCS)

Depth-Limited Search (DLS)

Iterative Deepening DFS (IDDFS)

Bidirectional Search

Each algorithm follows a strict clockwise movement order including all diagonals.

Visualization Features

The GUI (built using Matplotlib) shows:

Frontier nodes (nodes waiting to be explored)

Explored nodes (already visited)

Final path from Start to Target

Real-time animation of the search process

Dynamic obstacles appearing during execution

Automatic re-planning when the path becomes blocked

Every GUI window is titled:

GOOD PERFORMANCE TIME APP


Dependencies

This project uses:

Python 3

NumPy

Matplotlib

All required packages are listed in requirements.txt.


FOR ANY COMPLAINTS : Contact us at f240576@cfd.nu.edu.pk
