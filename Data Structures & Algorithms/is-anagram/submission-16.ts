class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        let splitS:string[] = s.split("");
        let splitT:string[] = t.split("");

        splitS.sort();
        splitT.sort();
        
        // console.log("sort")
        // console.log(splitS)
        // console.log(splitT)
        
        let sSorted = splitS.join();
        let tSorted = splitT.join();
       
        // console.log("join")
        // console.log(sSorted)
        // console.log(tSorted)

        if (sSorted === tSorted) {
            return true;
        } else{
            return false;
        }

    }
}
