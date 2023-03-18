class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target <nums[0]:
            return 0
        if len(nums)==1 and target>nums[0]:
            return 1
        for i in range(0,len(nums)-1):
            if target > nums[i] and target <nums[i+1]:
                return i+1
            
        return i+2