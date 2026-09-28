class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            toFind =  target - num

            if toFind in seen:
                return [seen[toFind], i]
            
            seen[num] = i
            