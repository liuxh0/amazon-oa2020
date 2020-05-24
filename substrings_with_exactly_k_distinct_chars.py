import collections

# Brute force
def k_distinct(s: str, k: int) -> int:
    ans = 0
    for i in range(0, len(s) - k + 1):
        seen = set()
        for j in range(i, len(s)):
            seen.add(s[j])
            if len(seen) == k:
                ans += 1
            elif len(seen) > k:
                break
    return ans

# O(n): exactly(k) = at_most(k) - at_most(k-1)
def k_distinct(s: str, k: int) -> int:

    def most_k(s, k):
        char_count = {}
        left = 0
        ans = 0
        for i, char in enumerate(s):
            char_count[char] = char_count.get(char, 0) + 1

            while len(char_count) > k:
                char = s[left]
                left += 1

                char_count[char] -= 1
                if char_count[char] == 0:
                    del char_count[char]

            ans += i - left + 1

        return ans

    return most_k(s, k) - most_k(s, k - 1)

input = {
    's': 'pqpqs',
    'k': 2
}
output = k_distinct(**input)
print(output)

input = {
    's': 'aabab',
    'k': 3
}
output = k_distinct(**input)
print(output)
