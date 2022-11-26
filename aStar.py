from grid import Grid, Node
import pygame

def Astar(grid: Grid, start: Node, end: Node):
    openNodes = []
    closedNodes = [] 

    openNodes.append(start)

    while len(openNodes) > 0:
        currentNode = openNodes[0]
        currentIndex = 0

        #print(currentNode)

        for index, node in enumerate(openNodes):
            if node.f < currentNode.f:
                currentNode = node
                currentIndex = index

        openNodes.pop(currentIndex)
        closedNodes.append(currentNode)

        if currentNode.pos == end.pos:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.pos)
                current = current.parent

            return path[::-1]

        neighbours = grid.getSurrounding(currentNode.pos)
        for pos in neighbours:
            child = Node(pos, currentNode)
            for closed in closedNodes:
                if child.pos == closed.pos:
                    continue

            child.g = currentNode.g + grid.largestDistance
            child.h = (child.pos[0] - end.pos[0]) ** 2 + (child.pos[1] - end.pos[1]) ** 2
            child.f = child.g + child.h

            for node in openNodes:
                if child.pos == node.pos and child.g > node.g:
                    continue

            openNodes.append(child)

if __name__ == "__main__":
    grid = Grid(10, 10)
    start = Node((0, 0), None)
    end = Node((grid.width - 1, 0), None)

    for y in range(grid.height - 1):
        grid.setPos((1, y), 0)

    path = Astar(grid, start, end)
    #print(path)

    screen = pygame.display.set_mode((1000, 1000))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        grid.draw(screen, path, start, end)

        pygame.display.flip()

    pygame.quit()