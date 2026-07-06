class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = [-s for s in stones]
        heapq.heapify(minheap)

        while len(minheap)>1:
            first = heapq.heappop(minheap) 
            second = heapq.heappop(minheap)
            if second > first:
                heapq.heappush(minheap, first - second)
        if minheap:
            return -(minheap[0])
        else:
            return 0