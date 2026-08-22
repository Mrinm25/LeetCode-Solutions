class Solution(object):
    def singleNumber(self, nums):
        count = {}
        for x in nums:
            count[x] = count.get(x,0) + 1
        for y in count:
            if count[y] == 1:
                return y
