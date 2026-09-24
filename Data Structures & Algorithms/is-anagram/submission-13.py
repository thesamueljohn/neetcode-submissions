class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print("s: " + s)
        print("t: " + s)
        # splitS = s.split() # doesn't work returns s the whole strigr
        splitS = list(s)
        splitS.sort()
        # print(dir(splitS))
        splitT = list(t)
        # splitT = splitT.sort() # wrong statement 
        # use # splitT = sorted(splitT) or
        splitT.sort() # correct


        # print("splitS:")
        # print(splitS)
        # print("splitT:")
        # print(splitT)
        # splitS.join("") # doesn't work like js
        "".join(splitS) # correct syntax
        "".join(splitT) # correct syntax

        if splitS == splitT:
            return True
        else:
            return False


        
        
        