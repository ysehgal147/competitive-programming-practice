class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1

        # Solution 1

        while end > start:
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1

        # Solution 2

        def reverseList(s, start, end):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]
            reverseList(s, start+1, end-1)

        reverseList(s, start, end)
