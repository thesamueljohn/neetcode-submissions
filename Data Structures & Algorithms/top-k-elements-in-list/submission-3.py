class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        resultArr = []
        for num in nums:
            # count.createdefault(num, 0) # set not create
            count.setdefault(num, 0) # set not create
            # print(count)
            count [num] += 1

        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

        for i, key in enumerate(count):
            resultArr.append(key)
            if i == k-1:
                return resultArr