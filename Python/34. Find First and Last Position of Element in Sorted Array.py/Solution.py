class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        left2 = 0
        right2 = len(nums) - 1
        first_occurance = -1
        last_occurance = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
               first_occurance = mid
               right = mid - 1
               
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        while left2 <= right2:
            mid = (left2 + right2) // 2
            if nums[mid] == target:
               last_occurance = mid
               left2 = mid + 1
               
            elif nums[mid] < target:
                left2 = mid + 1
            else:
                right2 = mid - 1
        if first_occurance != -1:
            return [first_occurance,last_occurance]
        else:
            return [-1,-1]
