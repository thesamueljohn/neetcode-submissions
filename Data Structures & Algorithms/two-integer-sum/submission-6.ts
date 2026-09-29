class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] { 
        const seen = new Map<number, number>(); 

        for (let i = 0; i < nums.length; i++) {

            const toFind:number = target - nums[i]; 

            if (seen.has(toFind)){ 
                const previousIndex = seen.get(toFind)!; // "!" IS A NOT NULL INDICATOR
                return [previousIndex, i] 
            } 
            seen.set(nums[i], i)
        } 
        return []
    } 
}
