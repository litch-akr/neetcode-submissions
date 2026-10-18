class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        area=0
        while left<right:
            w=abs(right-left)
            area=max(area,w*min(heights[left],heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area