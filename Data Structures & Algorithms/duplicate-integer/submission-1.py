class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t= "false"
        count= []
        for i in range(len(nums)):
            p = nums[i]
            if p in count:
                return True
            count.append(p)
        return False