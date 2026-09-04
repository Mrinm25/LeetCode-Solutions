class Solution(object):
    def threeSum(self, nums):
        nums_sorted = sorted(nums)
        result = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            while left < right:
                if nums_sorted[i] + nums_sorted[left] + nums_sorted[right] > 0:
                    right -=1
                elif nums_sorted[i] + nums_sorted[left] + nums_sorted[right] < 0:
                    left +=1
                else:
                    result.append([nums_sorted[i],nums_sorted[left],nums_sorted[right]])
                    left +=1
                    right -= 1
                    while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                        right -= 1
        return result
