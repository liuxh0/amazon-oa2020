from typing import List

def find_pair(nums: List[int], target: int) -> List[int]:
    ans = None

    num_index_dict = {}
    for i, num in enumerate(nums):
        num2 = target - 30 - num
        if num2 in num_index_dict:
            ans = [num_index_dict[num2], i]
        else:
            num_index_dict[num] = i

    return ans

input = {
    'nums': [1, 10, 25, 35, 60],
    'target': 90
}
output = find_pair(**input)
print(output)

input = {
    'nums': [20, 50, 40, 25, 30, 10],
    'target': 90
}
output = find_pair(**input)
print(output)
