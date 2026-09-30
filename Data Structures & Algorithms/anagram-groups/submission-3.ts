class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    
groupAnagrams(strs: String[]): String[][] {
    const found = new Map<String, String[]>
    for (let word of strs) {
        const sortedStr = word.split("").sort().join()

        // found.set(sortedStr, [])
        if (!found.get(sortedStr)) {
            found.set(sortedStr, []);
        }

        found.get(sortedStr)!.push(word);
    }

    return Array.from(found.values());
}


}
