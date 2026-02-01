class VacuumWorld:
    def __init__(self, grid, start, dirty_cells):
        """
        grid: 2D list where 0 = empty, 1 = obstacle
        start: (row, col)
        dirty_cells: set of (row, col)
        """
        self.grid = grid
        self.start = start
        self.dirty_cells = set(dirty_cells)
        self.rows = len(grid)
        self.cols = len(grid[0])

    def get_initial_state(self):
        return (self.start[0], self.start[1], frozenset(self.dirty_cells))

    def is_goal(self, state):
        _, _, dirty = state
        return len(dirty) == 0

    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_obstacle(self, row, col):
        return self.grid[row][col] == 1

    def get_actions(self, state):
        """
        Returns a list of valid actions from the given state.
        """
        actions = ["UP", "DOWN", "LEFT", "RIGHT", "CLEAN"]
        return actions

    def get_successor(self, state, action):
        row, col, dirty = state
        dirty = set(dirty)

        new_row, new_col = row, col

        if action == "UP":
            new_row -= 1
        elif action == "DOWN":
            new_row += 1
        elif action == "LEFT":
            new_col -= 1
        elif action == "RIGHT":
            new_col += 1
        elif action == "CLEAN":
            if (row, col) in dirty:
                dirty.remove((row, col))
            return (row, col, frozenset(dirty)), 1

        # Movement validation
        if not self.in_bounds(new_row, new_col):
            return None

        if self.is_obstacle(new_row, new_col):
            return None

        return (new_row, new_col, frozenset(dirty)), 1

    def get_successors(self, state):
        successors = []
        for action in self.get_actions(state):
            result = self.get_successor(state, action)
            if result is not None:
                next_state, cost = result
                successors.append((action, next_state, cost))
        return successors

