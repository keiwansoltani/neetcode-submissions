class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,maxl,res=0,0,0
        counts={}

        for r in range(len(s)):
            counts[s[r]] = 1+ counts.get(s[r],0)
            maxl = max(maxl, counts[s[r]])
            while (r-l+1)-maxl > k:
                counts[s[l]]-=1
                l+=1
            res = max(res, (r-l+1))
        return res