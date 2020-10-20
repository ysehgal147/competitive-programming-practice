# 1047. Remove All Adjacent Duplicates In String


class Solution:
    def removeDuplicates(self, S: str) -> str:
        queue=[]
        for char in S:
            queue.append(char)
            if len(queue)>=2:
                if queue[-1]==queue[-2]:
                    queue.pop(-1)
                    queue.pop(-1)
        result=''
        for item in queue:
            result+=item
        return result

        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)
