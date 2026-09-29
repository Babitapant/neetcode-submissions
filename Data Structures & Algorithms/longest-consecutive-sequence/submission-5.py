class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        current = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                current+=1
            else:
                current = 1
            max_count = (max(max_count, current))
        return max_count
        
        