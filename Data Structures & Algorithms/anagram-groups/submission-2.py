class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=dict()
        for i in strs:
            st= ''.join(sorted(i))
            if st in a:
                a[st].append(i)
            else:
                a[st]=[i]
        
        return list(a.values())
        