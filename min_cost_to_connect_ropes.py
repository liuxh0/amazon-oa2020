import heapq
from typing import List

def min_cost(ropes: List[int]) -> int:
    heapq.heapify(ropes)

    cost = 0
    while len(ropes) > 1:
        s = heapq.heappop(ropes) + heapq.heappop(ropes)
        heapq.heappush(ropes, s)
        cost += s

    return cost

input = {
    'ropes': [8, 4, 6, 12]
}
output = min_cost(**input)
assert output == 58

input = {
    'ropes': [20, 4, 8, 2]
}
output = min_cost(**input)
assert output == 54

input = {
    'ropes': [1, 2, 5, 10, 35, 89]
}
output = min_cost(**input)
assert output == 224

input = {
    'ropes': [2, 2, 3, 3]
}
output = min_cost(**input)
assert output == 20
