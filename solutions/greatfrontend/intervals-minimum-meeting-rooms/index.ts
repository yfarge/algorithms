export default function minMeetingRoomsNeeded(intervals: number[][]): number {
    intervals.sort((a, b) => a[0] - b[0]);
    let result = 0;
    const queue: number[] = [];
    for (const [start, end] of intervals) {
        while (queue.length > 0 && start >= queue[0]) {
            queue.shift();
        }
        queue.push(end);
        queue.sort((a, b) => a - b);
        result = Math.max(result, queue.length);
    }

    return result;
}
