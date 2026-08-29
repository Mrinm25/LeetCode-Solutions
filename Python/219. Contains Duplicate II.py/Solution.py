class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        index = 0
        for num in nums:
            if num not in seen:
                seen[num] = index
            else:
                i = seen[num]
                if abs(i - index) <= k:
                    return True
                else:
                    seen[num] = index
            index += 1
            
        return False
        
