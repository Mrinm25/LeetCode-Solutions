class Solution(object):
    def isAnagram(self, s, t):
        l1 = list(s)
        l2 = list(t)
        count_s = {}
        count_t = {}
        for x in l1:
            count_s[x] = count_s.get(x,0) + 1
        for y in l2:
            count_t[y] = count_t.get(y,0) + 1
        print(count_s)
        print(count_t)
        if count_s == count_t:
            return True
        else:
            return False
        
