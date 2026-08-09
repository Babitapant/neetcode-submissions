class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i, j in enumerate(nums):
            val = target - j

            if val in dictt:
                return [dictt[val], i]

            dictt[j] = i
        