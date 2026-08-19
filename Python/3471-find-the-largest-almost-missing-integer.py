class Solution(object):
    def largestInteger(self, nums, k):
        
        sub_arrays = []

        for i in range(len(nums) - k + 1):
            s_a = []
            for j in range(i,i+k):
                s_a.append(nums[j])
            sub_arrays.append(s_a)

        count = {}
        for a in sub_arrays:
            for x in set(a):
                count[x] = count.get(x,0) + 1

        r = []
        for b in nums:
            if count[b] == 1:
                r.append(b)
        if len(r) == 0:
            return -1
        else:
            return max(r)
