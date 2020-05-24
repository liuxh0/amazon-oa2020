import collections
import itertools
from typing import List

def optional_utilization(a: List[List[int]], b: List[List[int]], target: int) -> List[List[int]]:
    a_dict = collections.defaultdict(list)
    for e in a:
        id, value = e
        a_dict[value].append(id)

    b_dict = collections.defaultdict(list)
    for e in b:
        id, value = e
        b_dict[value].append(id)

    a_values = sorted(list(a_dict.keys()))
    b_values = sorted(list(b_dict.keys()))

    pa, pb = 0, len(b_values) - 1
    sum_dict = collections.defaultdict(list)
    max_sum = 0
    while pa < len(a_values) and pb >= 0:
        s = a_values[pa] + b_values[pb]
        if s <= target:
            if s >= max_sum:
                max_sum = s
                sum_dict[s].append([a_values[pa], b_values[pb]])

            pa += 1
        else:
            pb -= 1

    ans = []
    for pair in sum_dict[max_sum]:
        a_indexes = a_dict[pair[0]]
        b_indexes = b_dict[pair[1]]

        ans += list(itertools.product(a_indexes, b_indexes))

    return ans

input = {
    'a': [[1, 2], [2, 4], [3, 6]],
    'b': [[1, 2]],
    'target': 7
}
output = optional_utilization(**input)
print(output)

input = {
    'a': [[1, 3], [2, 5], [3, 7], [4, 10]],
    'b': [[1, 2], [2, 3], [3, 4], [4, 5]],
    'target': 10
}
output = optional_utilization(**input)
print(output)

input = {
    'a': [[1, 8], [2, 7], [3, 14]],
    'b': [[1, 5], [2, 10], [3, 14]],
    'target': 20
}
output = optional_utilization(**input)
print(output)

input = {
    'a': [[1, 8], [2, 15], [3, 9]],
    'b': [[1, 8], [2, 11], [3, 12]],
    'target': 20
}
output = optional_utilization(**input)
print(output)

input = {
    'a': [[1, 5], [2, 5]],
    'b': [[1, 5], [2, 5]],
    'target': 10
}
output = optional_utilization(**input)
print(output)
