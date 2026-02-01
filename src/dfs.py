from collections import deque

def dfs_search(problem):
    """
    Perform Depth-First Search.
    Returns:
        solution_path, nodes_expanded, max_frontier_size
    """
    start_state = problem.get_initial_state()

    stack = deque()
    stack.append((start_state, []))

    explored = set()

    nodes_expanded = 0
    max_frontier_size = 1

    while stack:
        max_frontier_size = max(max_frontier_size, len(stack))
        state, path = stack.pop()

        if problem.is_goal(state):
            return path, nodes_expanded, max_frontier_size

        if state in explored:
            continue

        explored.add(state)
        nodes_expanded += 1
        
        for action, next_state, cost in problem.get_successors(state):
            if next_state not in explored:
                stack.append((next_state, path + [action]))

    return None, nodes_expanded, max_frontier_size
