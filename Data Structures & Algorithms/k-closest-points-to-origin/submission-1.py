import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for x,y in points:
            d = (x**2) + (y**2)
            minheap.append([d,x,y])
        heapq.heapify(minheap)
        res=[]
        while k>0:
            c=heapq.heappop(minheap)
            res.append(c[1:])
            k-=1
        return res