def max_length(string: str) -> int:
    vowel_counts = []
    for c in string:
        if c in 'aeiou':
            if len(vowel_counts) == 0:
                vowel_counts.append(1)
            elif vowel_counts[-1] == 0:
                vowel_counts.append(1)
            elif vowel_counts[-1] > 0:
                vowel_counts[-1] += 1
        else:
            if len(vowel_counts) == 0:
                vowel_counts.append(0)
            elif vowel_counts[-1] == 0:
                pass
            elif vowel_counts[-1] > 0:
                vowel_counts.append(0)

    if len(vowel_counts) == 0:
        return 0
    elif len(vowel_counts) == 1:
        return vowel_counts[0]
    else:
        return vowel_counts[0] + vowel_counts[-1] + max(vowel_counts[1:-1])

input = {
    'string': 'earthproblem'
}
output = max_length(**input)
assert output == 3

input = {
    'string': 'letsgosomewhere'
}
output = max_length(**input)
assert output == 2
