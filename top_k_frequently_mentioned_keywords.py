# https://leetcode.com/discuss/interview-question/542597/

import functools
import heapq
from typing import List

def top_k_keywords(k: int, keywords: List[str], reviews: List[str]) -> List[str]:
    word_count = {}

    for review in reviews:
        # Lowercase letters and remove non-alphabet characters
        def convert_word(word):
            word = word.lower()
            word = ''.join(filter(lambda l: l.isalpha(), list(word)))
            return word

        words = review.lower().split(' ')
        words = list(map(convert_word, words))

        for keyword in keywords:
            if keyword in words:
                word_count[keyword] = word_count.get(keyword, 0) + 1

    def compare_keywords(keyword1, keyword2):
        if keyword1[1] - keyword2[1] != 0:
            return keyword2[1] - keyword1[1]
        else:
            return -1 if keyword1[0] < keyword2[0] else 1

    sorted_tuples = sorted(word_count.items(), key=functools.cmp_to_key(compare_keywords))
    sorted_keywords = list(map(lambda t: t[0], sorted_tuples))

    return sorted_keywords[:k]

input = {
    'k': 2,
    'keywords': ["anacell", "cetracular", "betacellular"],
    'reviews': [
        "Anacell provides the best services in the city",
        "betacellular has awesome services",
        "Best services provided by anacell, everyone should use anacell",
    ]
}
output = top_k_keywords(**input)
print(input, '\n', output, '\n')

input = {
    'k': 2,
    'keywords': ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"],
    'reviews': [
        "I love anacell Best services; Best services provided by anacell",
        "betacellular has great services",
        "deltacellular provides much better services than betacellular",
        "cetracular is worse than anacell",
        "Betacellular is better than deltacellular.",
    ]
}
output = top_k_keywords(**input)
print(input, '\n', output, '\n')
