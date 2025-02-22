func merge(intervals [][]int) [][]int {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })

    res := make([][]int, 0, len(intervals))
    res = append(res, intervals[0])

    for _, next := range intervals {
        prev := res[len(res) - 1]

        if prev[1] >= next[0] {
            prev[1] = max(prev[1], next[1])
        } else {
            res = append(res, next)
        }
    }

    return res
}
