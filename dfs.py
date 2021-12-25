import random


class DFS:
    def __init__(self, total_cols, total_rows):
        self.TOTAL_COLS = total_cols
        self.TOTAL_ROWS = total_rows

    def getCell(self, grid, x, y):
        n = x * self.TOTAL_COLS + y
        return grid[n]

    def getCellNeighbour(self, grid, cell):
        neighbour = []
        y = cell.row
        x = cell.col

        if y + 1 < self.TOTAL_ROWS:
            nc = self.getCell(grid, (y + 1), x)
            if not nc.visited:
                neighbour.append(nc)

        if y - 1 >= 0:
            nc = self.getCell(grid, (y - 1), x)
            if not nc.visited:
                neighbour.append(nc)

        if x + 1 < self.TOTAL_COLS:
            nc = self.getCell(grid, y, (x + 1))
            if not nc.visited:
                neighbour.append(nc)

        if x - 1 >= 0:
            nc = self.getCell(grid, y, (x - 1))
            if not nc.visited:
                neighbour.append(nc)

        return neighbour

    def removeWall(self, cell, neighbour):
        if cell.row == neighbour.row:
            if cell.col < neighbour.col:
                cell.edges['right'] = False
                neighbour.edges['left'] = False
            else:
                cell.edges['left'] = False
                neighbour.edges['right'] = False

        elif cell.col == neighbour.col:
            if cell.row < neighbour.row:
                cell.edges['bottom'] = False
                neighbour.edges['top'] = False
            else:
                cell.edges['top'] = False
                neighbour.edges['bottom'] = False

    def DFSMazeGeneration(self, grid):
        # 1 - Create extranal stack and push the start cell to it
        stack = []
        s = 0
        grid[s].visited = True
        stack.append(grid[s])
        # 2 - if stack is not empty
        while len(stack) > 0:
            # 2.1 - pop the top of stack
            currentCell = stack.pop()

            # 2.2 - get all the non visited neighbour
            neighhbours = self.getCellNeighbour(grid, currentCell)

            # 2.2.1 - if neighbours is not empty push current cell to stack
            if len(neighhbours) > 0:
                stack.append(currentCell)
                # 2.2.2 select random neighbour
                chosenNeighbour = random.choice(neighhbours)
                # 2.2.3 remove the common wall
                self.removeWall(currentCell, chosenNeighbour)
                # 2.2.4 mark the chosen neighbour as visited and push to stack
                chosenNeighbour.visited = True
                stack.append(chosenNeighbour)