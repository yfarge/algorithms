export default function isMeetingCalendarValid(intervals: number[][]): boolean {
    intervals.sort((a, b) => a[1] - b[1]);

    let prevEnd = Number.MIN_SAFE_INTEGER;
    for (const [start, end] of intervals) {
        if (start >= prevEnd) {
            prevEnd = end;
        } else {
            return false;
        }
    }
    return true;
}
