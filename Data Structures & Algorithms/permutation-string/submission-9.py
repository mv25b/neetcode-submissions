class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def check(long, short):
            setlong, setshort = {}, {}

            for char in short:
                setshort[char] = setshort.get(char, 0) + 1


            for i in range(len(short)):
                setlong[long[i]] = setlong.get(long[i], 0) + 1

            if setlong == setshort:
                return True
            for i in range(len(short), len(long)):
                setlong[long[i]] = setlong.get(long[i], 0) + 1

                
                remove = long[i - len(short)]
                setlong[remove] -= 1

                if setlong[remove] == 0:
                    setlong.pop(remove)

                if setlong.items() == setshort.items():
                    return True
            
            return False

        return check(s2,s1)
            