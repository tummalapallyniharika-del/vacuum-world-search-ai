from src.vacuum_world import VacuumWorld
from src.dfs import dfs_search
from src.astar import astar_search
from src.idastar import idastar_search

def main():
    grid = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]

    start = (0, 0)
    dirty_cells = {(0, 2), (1, 3), (2, 0), (3, 2)}

    problem = VacuumWorld(grid, start, dirty_cells)

    solution, nodes_expanded, max_frontier = dfs_search(problem)

    print("DFS Solution Path:")
    print(solution)
    print("Steps:", len(solution) if solution else None)
    print("Nodes Expanded:", nodes_expanded)
    print("Max Frontier Size:", max_frontier)

    solution, nodes_expanded, max_frontier = astar_search(problem)

    print("\nA* Solution Path:")
    print(solution)
    print("Steps:", len(solution) if solution else None)
    print("Nodes Expanded:", nodes_expanded)
    print("Max Frontier Size:", max_frontier)

    solution, nodes_expanded, iterations = idastar_search(problem)

    print("\nIDA* Solution Path:")
    print(solution)
    print("Steps:", len(solution) if solution else None)
    print("Nodes Expanded:", nodes_expanded)
    print("Iterations:", iterations)



if __name__ == "__main__":
    main()
