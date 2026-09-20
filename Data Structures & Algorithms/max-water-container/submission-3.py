

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water, n = 0, len(heights)
        left, right = 0, n-1

        while(left < right):
            max_water = max(max_water, (right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water