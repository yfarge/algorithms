class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for i in range(len(s)):
            if s[i] in pairs.values():
                stack.append(s[i])
            elif stack and stack.pop() == pairs[s[i]]:
                continue
            else:
                return False

        return len(stack) == 0
