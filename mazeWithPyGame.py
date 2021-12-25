import pygame
from Cell import Cell
from dfs import DFS
import random


class Player:
    def __init__(self, shift):
        self.color = (255, 255, 0)
        self.row = 0
        self.col = 0
        self.CELL_WIDTH = 50
        self.shift = shift
        self.width = 40
        self.solved = False

    def display_player(self, screen):
        y0 = self.row * self.CELL_WIDTH + self.shift + 5
        x0 = self.col * self.CELL_WIDTH + self.shift + 5
        if not self.solved:
            pygame.draw.rect(screen, self.color, (x0, y0, self.width, self.width))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (x0, y0, self.width, self.width))

    def move_right(self):
        self.col += 1

    def move_left(self):
        self.col -= 1

    def move_up(self):
        self.row -= 1

    def move_down(self):
        self.row += 1


class MazeGame:
    TOTAL_ROWS = 10
    TOTAL_COLS = 10
    CELL_WIDTH = 50
    windowHeight = 600
    windowWidth = 600
    shift = 50
    mazeGrid = []

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        size = (self.windowHeight, self.windowWidth)
        self._running = True
        self._screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Maze game")
        self.title = "pygame"
        self.mazeGrid = [Cell(i, j) for i in range(self.TOTAL_ROWS) for j in range(self.TOTAL_COLS)]
        self.dfs = DFS(self.TOTAL_COLS, self.TOTAL_ROWS)

    def quitGame(self):
        pygame.quit()

    def display_maze(self):
        for cell in self.mazeGrid:
            cell.display(pygame, self._screen, shift=self.shift)

        pygame.draw.rect(self._screen, (255, 255, 255), pygame.Rect(9*50+self.shift+5, 9*50+self.shift+5, 40, 40))

    def getCell(self, x, y):
        n = x * self.TOTAL_COLS + y
        return self.mazeGrid[n]
        # return n

    def render(self, player):
        self._screen.fill((143,188,143))
        self.display_maze()
        player.display_player(self._screen)
        if self.maze_solved(player):
            self.solved_widgets()
        pygame.display.flip()

    def validate_move(self, cell, dir):
        if dir == "UP":
            return not cell.edges["top"]

        if dir == "DOWN":
            return not cell.edges["bottom"]

        if dir == "LEFT":
            return not cell.edges["left"]

        if dir == "RIGHT":
            return not cell.edges["right"]

    def print_gridMaze(self):
        for i in range(10):
            for j in range(10):
                print((self.getCell(i, j)), end=" ")

            print("")

    def maze_solved(self, player):
        if (player.row == self.TOTAL_ROWS - 1) and (player.col == self.TOTAL_COLS - 1):
            player.solved = True
            return True
        return False

    def solved_widgets(self):
        myfont = pygame.font.Font('freesansbold.ttf', 20)
        label = myfont.render("Solved..!", 1, (255, 255, 255))
        self._screen.blit(label, (250, 20))

    def run(self):
        p1 = Player(self.shift)
        self.dfs.DFSMazeGeneration(self.mazeGrid)
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

                if not self.maze_solved(p1) and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN and self.validate_move(self.getCell(p1.row, p1.col), "DOWN"):
                        p1.move_down()

                    if event.key == pygame.K_UP and self.validate_move(self.getCell(p1.row, p1.col), "UP"):
                        p1.move_up()

                    if event.key == pygame.K_LEFT and self.validate_move(self.getCell(p1.row, p1.col), "LEFT"):
                        p1.move_left()

                    if event.key == pygame.K_RIGHT and self.validate_move(self.getCell(p1.row, p1.col), "RIGHT"):
                        p1.move_right()

            self.render(p1)

        self.quitGame()


if __name__ == '__main__':
    mazeGame = MazeGame()
    mazeGame.run()
