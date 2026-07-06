class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for idx, n in enumerate(nums):
            r = target - n
            if r in prev_map:
                return [prev_map[r], idx]
            prev_map[n]= idx
        return
    