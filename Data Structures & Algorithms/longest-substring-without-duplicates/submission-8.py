class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        res = 1

        l, r = 0, 0

        store = set(s[l])
        count = 1
        while (r < len(s)):
            if l == r:
                r += 1
                continue

            if s[r] in store:
                res = max(res, count)

                while(s[r] in store):
                    store.remove(s[l])
                    l+=1
                    count -= 1
                store.add(s[r])
                count += 1
                r += 1
            else:
                count += 1
                store.add(s[r])
                r+=1
            
        return max(res, count)
