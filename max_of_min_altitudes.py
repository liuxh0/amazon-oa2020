from typing import List

def max_score(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

    ans = 0
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0: continue
            if i == m - 1 and j == n - 1:
                ans = max(dp[i+1][j], dp[i][j+1])

            dp[i+1][j+1] = min(max(dp[i+1][j], dp[i][j+1]), matrix[i][j])
    return ans

input = {
    'matrix': [
        [5, 1],
        [4, 5]
    ]
}
output = max_score(**input)
print(output)

input = {
    'matrix': [
        [1, 2, 3],
        [4, 5, 1]
    ]
}
output = max_score(**input)
print(output)
