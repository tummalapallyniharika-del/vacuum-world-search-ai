import heapq

def heuristic(state):
    row, col, dirty = state
    if not dirty:
        return 0

    distances = []
    for dr, dc in dirty:
        distances.append(abs(row - dr) + abs(col - dc))

    return min(distances) + len(dirty) - 1

def astar_search(problem):
    start_state = problem.get_initial_state()

    frontier = []
    heapq.heappush(frontier, (0, start_state, []))

    g_costs = {start_state: 0}
    explored = set()

    nodes_expanded = 0
    max_frontier_size = 1

    while frontier:
        max_frontier_size = max(max_frontier_size, len(frontier))
        f, state, path = heapq.heappop(frontier)

        if problem.is_goal(state):
            return path, nodes_expanded, max_frontier_size

        if state in explored:
            continue

        explored.add(state)
        nodes_expanded += 1

        for action, next_state, cost in problem.get_successors(state):
            new_g = g_costs[state] + cost

            if next_state not in g_costs or new_g < g_costs[next_state]:
                g_costs[next_state] = new_g
                f_cost = new_g + heuristic(next_state)
                heapq.heappush(frontier, (f_cost, next_state, path + [action]))

    return None, nodes_expanded, max_frontier_size
