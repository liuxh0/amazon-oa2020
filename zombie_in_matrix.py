# https://leetcode.com/discuss/interview-question/411357/

import copy
from typing import List

def hours(grid: List[List[int]]) -> int:
    row = len(grid)
    if row == 0: return 0
    column = len(grid[0])

    human_count = 0
    for i in range(row):
        for j in range(column):
            human_count += 1 if grid[i][j] == 0 else 0

    time = 0
    while human_count != 0:
        time += 1

        for i in range(row):
            for j in range(column):
                if grid[i][j] == time:
                    if i - 1 >= 0 and grid[i - 1][j] == 0:
                        grid[i - 1][j] = time + 1
                        human_count -= 1
                    if i + 1 < row and grid[i + 1][j] == 0:
                        grid[i + 1][j] = time + 1
                        human_count -= 1
                    if j - 1 >= 0 and grid[i][j - 1] == 0:
                        grid[i][j - 1] = time + 1
                        human_count -= 1
                    if j + 1 < column and grid[i][j + 1] == 0:
                        grid[i][j + 1] = time + 1
                        human_count -= 1

    return time

input = [
    [0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0]
]
output = hours(copy.deepcopy(input))
print(input, '\n', output, '\n')
