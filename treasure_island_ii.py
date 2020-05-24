from typing import List

def min_steps(grid: [List[List[str]]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()
    current = []
    step = 0

    # Find all starting points
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                visited.add((i, j))
                current.append((i, j))

    def add(x, y, next):
        if x >= 0 and x < m and y >= 0 and y < n \
        and grid[x][y] != 'D' and (x, y) not in visited:
            next.append((x,y))
            visited.add((x,y))

    while True:
        next = []
        for loc in current:
            x, y = loc
            if grid[x][y] == 'X':
                return step

            add(x - 1, y, next)
            add(x + 1, y, next)
            add(x, y - 1, next)
            add(x, y + 1, next)
            current = next
        step += 1

input = {
    'grid': [
        ['S', 'O', 'O', 'S', 'S'],
        ['D', 'O', 'D', 'O', 'D'],
        ['O', 'O', 'O', 'O', 'X'],
        ['X', 'D', 'D', 'O', 'O'],
        ['X', 'D', 'D', 'D', 'O']
    ]
}
output = min_steps(**input)
assert output == 3
