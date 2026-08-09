class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt = {}
        for num in nums:
            dictt[num] = dictt.get(num, 0)+1

        result= any(value>1 for value in dictt.values())
        return result