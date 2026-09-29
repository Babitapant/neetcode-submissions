class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictt = {}
        for i, j in enumerate(numbers, start=1):
            val = target-j
           
            if val in dictt:
                return [dictt[val], i]
            dictt[j] = i