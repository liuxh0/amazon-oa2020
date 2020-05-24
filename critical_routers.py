# https://leetcode.com/discuss/interview-question/436073/

import collections
from typing import List, Tuple

def critical_routers(numNodes: int, numEdges: int, edges: List[List[int]]) -> List[int]:
    connections = collections.defaultdict(list)
    for edge in edges:
        connections[edge[0]].append(edge[1])
        connections[edge[1]].append(edge[0])

    levels = {}
    ans = []

    def dfs(node: int, parent: int, level: int):
        levels[node] = level
        outgoing_edges = 0                      # Only for starting node

        for neighbor in connections[node]:
            if neighbor == parent: continue     # Skip parent to avoid cycle
            elif neighbor not in levels:
                if parent == -1: outgoing_edges += 1

                neighbor_level = dfs(neighbor, node, level + 1)
                levels[node] = min(levels[node], neighbor_level)

                # Articulation point found via bridge
                if neighbor_level == level + 1:
                    ans.append(node)

                # Articulation point found via cycle
                if neighbor_level == level and parent != -1:
                    ans.append(node)
            else:
                levels[node] = min(levels[node], levels[neighbor])

        # If the starting node has at least two outgoing edges, then it is also an articulation point.
        if parent == -1 and outgoing_edges > 1 :
            ans.append(node)

        return levels[node]

    dfs(0, -1, 0)
    return ans

input = {
    'numNodes': 7,
    'numEdges': 7,
    'edges': [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
}
output = critical_routers(**input)
print(output)

# https://www.youtube.com/watch?v=mKUsbABiwBI
# https://www.youtube.com/watch?v=aZXi1unBdJA
