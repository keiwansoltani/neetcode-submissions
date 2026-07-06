class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = [-s for s in stones]
        heapq.heapify(minheap)

        while len(minheap)>1:
            s1 = heapq.heappop(minheap) * -1
            s2 = heapq.heappop(minheap) * -1
            if s1 < s2:
                heapq.heappush(minheap, (s2-s1)*-1)
            elif s1>s2:
                heapq.heappush(minheap, (s1-s2)*-1)
        if minheap:
            return (minheap[0]*-1)
        else:
            return 0