class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack =[]  #pair:(temp, idx)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackt,stackidx=stack.pop()
                res[stackidx] = (i-stackidx)
            stack.append([t,i])
        return res