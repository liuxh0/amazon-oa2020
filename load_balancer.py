from typing import List

def load_balancer(A: List[int]) -> bool:
    total_sum = sum(A)

    left_sum, right_sum = A[0], A[-1]
    left_sep, right_sep = 1, len(A) - 2
    mid_sum = total_sum - left_sum - A[left_sep] - right_sum - A[right_sep]

    while left_sep < right_sep and mid_sum >= max(left_sum, right_sum):
        if left_sum == right_sum:
            if mid_sum == left_sum:
                return True
            else:
                left_sum += A[left_sep]
                left_sep += 1
                mid_sum -= A[left_sep]
        elif left_sum > right_sum:
            right_sum += A[right_sep]
            right_sep -= 1
            mid_sum -= A[right_sep]
        elif left_sum < right_sum:
            left_sum += A[left_sep]
            left_sep += 1
            mid_sum -= A[left_sep]

    return False

input = {
    'A': [1, 3, 4, 2, 2, 2, 1, 1, 2]
}
output = load_balancer(**input)
assert output == True

input = {
    'A': [1, 1, 1, 1, 1, 1]
}
output = load_balancer(**input)
assert output == False

input = {
    'A': [1, 2] * 10000
}
output = load_balancer(**input)
assert output == True
