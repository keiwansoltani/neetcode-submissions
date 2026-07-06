class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cap = 0
        l, r = 0, len(heights)-1
        while l <= r:
            cap = (r - l) * min(heights[l], heights[r])
            max_cap = max(cap, max_cap)
            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1
        return max_cap