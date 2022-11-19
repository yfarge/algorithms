class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        seen = set()

        def dfs(cur):
            if len(cur) == len(nums):
                res.append([i for i in cur])
                return

            for num in nums:
                if num in seen:
                    continue
                seen.add(num)
                cur.append(num)
                dfs(cur)
                cur.pop()
                seen.remove(num)
        dfs([])
        return res
