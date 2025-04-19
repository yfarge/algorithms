export default function disjointIntervals(intervals: number[][]): number {
    intervals.sort((a, b) => a[1] - b[1]);
    let result = 0;
    let prevEnd = Number.MIN_SAFE_INTEGER;
    for (let i = 0; i < intervals.length; ++i) {
        if (intervals[i][0] >= prevEnd) {
            prevEnd = intervals[i][1]
        } else {
            result += 1;
        }
    }
    return result;
}
