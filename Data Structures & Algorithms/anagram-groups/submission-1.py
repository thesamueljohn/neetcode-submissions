class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = {}
        for i, str in enumerate(strs):
            strsSortedEach = strs
            strsSortedEach[i] = "".join(sorted(str))
            # if strsSortedEach[i] in found:
            #     found[str].append(strsSortedEach[i]) 
            sortedStr = strsSortedEach[i]
            # found[sortedStr] = [] # create keys for each # not needed would only reset the dictionary each iteration

            found.setdefault(sortedStr, []).append(str) 

        # print((list(found.values())))
        return (list(found.values()))

        