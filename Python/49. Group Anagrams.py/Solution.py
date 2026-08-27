class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in dic:
                dic[key] = []
                dic[key].append(word)
            else:
                dic[key].append(word)
        return dic.values()
