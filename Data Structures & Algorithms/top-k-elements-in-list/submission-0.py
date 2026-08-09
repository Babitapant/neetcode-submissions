class Solution:
    def topKFrequent(self, nums: List[int], k: int) ->      List[int]:

        a={}
        for num in nums:
            if num in a:
                a[num]=a.get(num, 0)+1
            else:
                a[num]=1

        sorted_data = dict(sorted(a.items(), key=lambda item:   item[1],reverse=True))
        
        c=list(sorted_data.keys())
        return c[:k]