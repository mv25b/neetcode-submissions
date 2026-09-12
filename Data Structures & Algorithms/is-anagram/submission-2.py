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
        
        return letters == lettert

