export default function mergeOverlappingIntervals(
    intervals: number[][],
): number[][] {
    intervals.sort((a, b) => a[0] - b[0])
    const result: number[][] = [];
    for (const [start, end] of intervals) {
        if (result.length === 0 || result[result.length - 1][1] < start) {
            result.push([start, end]);
        } else {
            result[result.length - 1][1] = Math.max(
                result[result.length - 1][1],
                end
            );
        }
    }
    return result;
}
