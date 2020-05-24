import heapq
from typing import List

def min_cost(n: int, edges: List[List[int]], newEdges: List[List[int]]) -> int:
    parent = [n for n in range(n + 1)]
    rank = [0] * (n + 1)
    group_count = n

    def find(node: int) -> int:
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(n1: int, n2: int):
        nonlocal group_count

        if find(n1) == find(n2):
            return

        if rank[n1] < rank[n2]:
            parent[n2] = n1
        elif rank[n1] > rank[n2]:
            parent[n1] = n2
        elif rank[n1] == rank[n2]:
            parent[n1] = n2
            n2 += 1
        group_count -= 1

    # Union already connected nodes
    for edge in edges:
        n1, n2 = edge
        union(n1, n2)

    # Min heap according to cost
    min_cost_heap = []
    for edge in newEdges:
        n1, n2, cost = edge
        heapq.heappush(min_cost_heap, (cost, n1, n2))

    # Add new edge to graph until all connnected
    cost = 0
    while group_count > 1:
        c, n1, n2 = heapq.heappop(min_cost_heap)
        if find(n1) == find(n2):
            continue
        else:
            cost += c
            union(n1, n2)

    return cost

input = {
    'n': 6,
    'edges': [[1, 4], [4, 5], [2, 3]],
    'newEdges': [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
}
output = min_cost(**input)
assert output == 7
