class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters= {}
        lettert = {}
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1
            if t[i] in lettert:
                lettert[t[i]] += 1
            else:
                lettert[t[i]] = 1
        
        tmp = lettert.items()
        for keys in letters.items():
            if keys not in tmp:
                return False
        return True

