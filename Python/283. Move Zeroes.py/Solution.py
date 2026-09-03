class Solution(object):
    def moveZeroes(self, nums):
        p1 = 0
        p2 = 1
        for i in range(len(nums) - 1):
            if nums[p1] == 0 and nums[p2] != 0:
                nums[p1] = nums[p2]
                nums[p2] = 0
                p1 += 1
                p2 += 1
            elif nums[p1] != 0 and nums[p2] == 0:
                p1 += 1
                p2 += 1
            elif nums[p1] != 0 and nums[p2] != 0:
                p1 +=1
                p2 +=1
            elif nums[p1] == 0 and nums[p2] == 0:
                p2 +=1
        
