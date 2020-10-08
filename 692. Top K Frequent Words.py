# 692. Top K Frequent Words

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # Solution 1 (Hashmap)

        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1

        ret = sorted(d, key=lambda word: (-d[word], word))

        return ret[:k]
