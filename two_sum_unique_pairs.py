def unique_pairs(nums: int, target: int) -> int:
    seen = set()
    ans = set()

    for n in nums:
        if n in seen:
            ans.add(min(n, target - n))
        else:
            seen.add(target - n)

    return len(ans)

input = {
    'nums': [1, 1, 2, 45, 46, 46],
    'target': 47
}
output = unique_pairs(**input)
print(output)

input = {
    'nums': [1, 1],
    'target': 2
}
output = unique_pairs(**input)
print(output)

input = {
    'nums': [1, 5, 1, 5],
    'target': 6
}
output = unique_pairs(**input)
print(output)
