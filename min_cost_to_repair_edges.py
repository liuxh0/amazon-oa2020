import heapq
from typing import List

def min_cost(n: int, edges: List[List[int]], edgesToRepair: List[List[int]]) -> int:
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

    # Cost of all edges
    # Treat non-broken edges with cost 0
    edge_cost_dict ={}
    for edge in edges:
        n1, n2 = edge
        edge_cost_dict[(n1, n2)] = 0
    for edge in edgesToRepair:
        n1, n2, c = edge
        edge_cost_dict[(n1, n2)] = c

    # Min heap according to cost
    min_cost_heap = []
    for edge, cost in edge_cost_dict.items():
        n1, n2= edge
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
    'n': 5,
    'edges': [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],
    'edgesToRepair': [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
}
output = min_cost(**input)
assert output == 20

input = {
    'n': 6,
    'edges': [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]],
    'edgesToRepair': [[1, 6, 410], [2, 4, 800]]
}
output = min_cost(**input)
assert output == 410

input = {
    'n': 6,
    'edges': [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
    'edgesToRepair': [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
}
output = min_cost(**input)
assert output == 79
