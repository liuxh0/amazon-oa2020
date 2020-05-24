from typing import List

def substrings_k(s: str, k: int) -> List[str]:
    charset = set()
    result = set()
    left, right = 0, 0
    while right < len(s):
        char = s[right]
        if char in charset or len(charset) == k:
            charset.remove(s[left])
            left += 1
        else:
            charset.add(char)
            right += 1

            if right - left == k:
                result.add(s[left:right])

    return list(result)

input = {
    's': 'abcabc',
    'k': 3
}
output = substrings_k(**input)
print(output)

input = {
    's': 'abacab',
    'k': 3
}
output = substrings_k(**input)
print(output)

input = {
    's': 'awaglknagawunagwkwagl',
    'k': 4
}
output = substrings_k(**input)
print(output)
