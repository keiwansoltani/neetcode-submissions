class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap=[-n for n in nums]
        heapq.heapify(minheap)
        res=None
        while k>0:
            res = -1 * heapq.heappop(minheap)
            k -=1

        return res
