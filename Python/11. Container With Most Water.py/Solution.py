class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right-left)
                max_area= max(max_area,area)
                left += 1

            elif height[right] < height[left]:
                area = height[right] * (right-left)
                max_area = max(max_area,area)
                right -= 1
            else:
                area = height[left] * (right-left)
                max_area = max(max_area, area)
                left +=1

        return max_area
