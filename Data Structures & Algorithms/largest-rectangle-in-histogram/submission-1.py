class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea= 0
        n = len(heights)
        stack = []
        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]]>= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] -1
                maxarea = max(maxarea, height * width)
            stack.append(i)
        return maxarea


        