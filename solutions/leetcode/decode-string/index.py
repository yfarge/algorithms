class Solution:
    def decodeString(self, s: str) -> str:
        stack, prefix, k = [], "", 0

        for c in s:
            if c == "[":
                stack.append(k)
                stack.append(prefix)
                prefix = ""
                k = 0
            elif c == "]":
                prefix = stack.pop() + stack.pop() * prefix
            elif c.isdigit():
                k = k * 10 + int(c)
            else:
                prefix += c

        return prefix

