class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = {}
        for word in strs:
            sortedStr = "".join(sorted(word))
            ''' found[sortedStr] = []  
            create keys for each 
            not needed would only reset the dictionary each iteration
            '''
            found.setdefault(sortedStr, []).append(word) 

        return list(found.values())

        