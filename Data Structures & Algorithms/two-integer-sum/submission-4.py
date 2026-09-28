class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            toFind = target - num
        
            # if toFind in nums: 
            ''' 
            [1,3,2,4]
            won't work for e.g [3, 3] i.e it checks everytime for 
            toFind in nums and even if 3 isn't in the array again it parses as true
            '''
            if toFind in nums[i + 1:]: 
                # print([m for m in nums if nums.index(m) > i].index(toFind))
                # subArr = [m for m in nums if nums.index(m) > i]
                # print(subArr)
                print(num, toFind)

                return [i, nums.index(toFind, i+1)]
            else: 
                continue