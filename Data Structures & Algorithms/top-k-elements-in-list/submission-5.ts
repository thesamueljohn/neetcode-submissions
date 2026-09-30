class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const count = new Map<number, number>()
        const resultArr = []
        for (let num of nums) {
            if (!count.get(num)){
                count.set(num, 1)
            }
            else {
                count.set(num, count.get(num)!+1)
            }
        }

        // count = Map(sorted(count.items(), key=lambda item: item[1], reverse=True))
        const sortedCount = new Map(([...count.entries()]).sort((a,b)=> b[1] - a[1] ))
        // console.log(count)
        // console.log(sortedCount)
        var kCount = 0;
        for (const key of sortedCount) {
            console.log(key)
            kCount ++;
            resultArr.push(key[0])
            if (kCount == k) return resultArr
        }
    }
}
