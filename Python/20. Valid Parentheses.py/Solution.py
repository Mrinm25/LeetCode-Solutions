class Solution(object):
    def isValid(self, s):
        l = list(s)
        stack = []
        pairs = {
            ")" : "(", "}" : "{", "]" : "["
        }
        opening_bracket = [ "(", "{", "["]
        for i in range(len(l)):
            if l[i] in opening_bracket:
                stack.append(l[i])
            else:
                if stack == []:
                    return False
                elif stack[-1] == pairs[l[i]]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
