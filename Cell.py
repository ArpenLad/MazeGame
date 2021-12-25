class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.edges = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True
        }
        self.CELL_WIDTH = 50
        self.cell_border = (255, 255, 255)

    def display(self, pygame, screen, shift=10):
        y0 = self.row * self.CELL_WIDTH + shift
        x0 = self.col * self.CELL_WIDTH + shift
        y1 = self.row * self.CELL_WIDTH + self.CELL_WIDTH + shift
        x1 = self.col * self.CELL_WIDTH + self.CELL_WIDTH + shift

        if self.edges["left"]:
            pygame.draw.line(screen, self.cell_border, (x0, y0), (x0, y1))

        if self.edges["bottom"]:
            pygame.draw.line(screen, self.cell_border, (x0, y1), (x1,y1))

        if self.edges["right"]:
            pygame.draw.line(screen, self.cell_border, (x1, y1), (x1, y0))

        if self.edges["top"]:
            pygame.draw.line(screen, self.cell_border, (x1, y0), (x0, y0))
