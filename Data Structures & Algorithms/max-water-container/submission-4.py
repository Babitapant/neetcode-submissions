class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = 0
        left = len(heights)-1
        area_max= 0
        
        while right<left:
            
            wide = abs(left-right)
           
            height = min(heights[right], heights[left])
            area = (wide*height)
            area_max = max(area_max, area)
            if heights[right]<heights[left]:
                
                right+=1
            else:
                left-=1
        
        return area_max
        