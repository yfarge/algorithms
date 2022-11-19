def permute(nums: list[int]):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []

    def dfs(cur: list[int]):
        if len(cur) == len(nums):
            res.append([i for i in cur])
            return
        for num in nums:
            if num in cur:
                continue
            cur.append(num)
            dfs(cur)
            cur.pop()
    dfs([])
    return res


print(permute([1, 2, 3]))
