from src.astar import heuristic
import math

def idastar_search(problem):
    start_state = problem.get_initial_state()
    threshold = heuristic(start_state)

    nodes_expanded = 0
    iterations = 0

    while True:
        iterations += 1
        temp, found, nodes = dfs_f_limit(
            problem, start_state, 0, threshold, []
        )
        nodes_expanded += nodes

        if found is not None:
            return found, nodes_expanded, iterations

        if temp == math.inf:
            return None, nodes_expanded, iterations

        threshold = temp

def dfs_f_limit(problem, state, g, threshold, path):
    f = g + heuristic(state)

    if f > threshold:
        return f, None, 1

    if problem.is_goal(state):
        return f, path, 1

    min_threshold = math.inf
    nodes_expanded = 1

    for action, next_state, cost in problem.get_successors(state):
        temp, found, nodes = dfs_f_limit(
            problem,
            next_state,
            g + cost,
            threshold,
            path + [action]
        )
        nodes_expanded += nodes

        if found is not None:
            return temp, found, nodes_expanded

        min_threshold = min(min_threshold, temp)

    return min_threshold, None, nodes_expanded
