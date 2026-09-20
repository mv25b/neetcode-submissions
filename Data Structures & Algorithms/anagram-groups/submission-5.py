class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        res = []
        for word in strs:
            s = {}
            for char in word:
                s[char] = s.get(char, 0) + 1
            
            s = frozenset(s.items())
            if s in store:
                res[store[s]].append(word)
            else:
                store[s] = len(res)
                res.append([word])
        return res

