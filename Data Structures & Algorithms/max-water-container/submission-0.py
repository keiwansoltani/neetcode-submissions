class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cap = 0
        l, r = 0, len(heights)-1
        while l <= r:
            cap = (r - l) * min(heights[l], heights[r])
            if cap > max_cap:
                max_cap = cap
            if heights[l] <= heights[r]:
                l +=1
            elif heights[r] < heights[l]:
                r -=1
        return max_cap