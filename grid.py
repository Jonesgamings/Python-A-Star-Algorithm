import pygame

class Node:
    def __init__(self, pos, parent):
        self.pos = pos
        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0

    def __str__(self) -> str:
        return f"{self.pos} - F:{self.f}, G:{self.g}, H:{self.h}, PARENT:({self.parent})"

class Grid:

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.largestDistance = (width - 1) ** 2 + (height - 1) ** 2
        self.grid = {}

        self.generateBlank()

    def generateBlank(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[(x, y)] = None

    def getSurrounding(self, pos):
        neighbours = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                newPos = (x + pos[0], y + pos[1])
                if self.grid.keys().__contains__(newPos):
                    if self.grid[newPos] != 0:
                        neighbours.append(newPos)

        return neighbours

    def draw(self, screen: pygame.Surface, path, start, end):
        gridX = screen.get_size()[0] / self.width
        gridY = screen.get_size()[1] / self.height
        for key, value in self.grid.items():
            realX = key[0] * gridX
            realY = key[1] * gridY
            rect = pygame.Rect(realX, realY, gridX, gridY)

            if key == start.pos:
                pygame.draw.rect(screen, (0, 150, 0), rect)

            elif key == end.pos:
                pygame.draw.rect(screen, (0, 0, 150), rect)

            elif key in path:
                pygame.draw.rect(screen, (150, 0, 0), rect)

            elif value == 0:
                pygame.draw.rect(screen, (0, 0, 0), rect)

            else:
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)

    def setPos(self, pos, value):
        self.grid[pos] = value

if __name__ == "__main__":
    grid = Grid(10, 10)