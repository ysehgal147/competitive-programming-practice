# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Solution 1. (Traversing)

        seen = ''
        mx = 0
        for c in s:
            if c not in seen:
                seen += c
            else:
                seen = seen[seen.index(c) + 1:] + c
            mx = max(mx, len(seen))
        return mx
