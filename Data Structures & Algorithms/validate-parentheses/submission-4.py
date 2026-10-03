class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()

        link = {']' : '[', ')':'(', '}': '{'}

        for brace in s:
            if brace in link:
                
                if not q or link[brace] != q.pop():
                    return False
            else:
                q.append(brace)
        return not q