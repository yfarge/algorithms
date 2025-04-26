export default function longestUniqueSubstring(str: string): number {
    const seen: Map<string, number> = new Map();
    let left = 0, result = 0;
    for (let right = 0; right < str.length; right++) {
        if (seen.has(str[right])) {
            const lastSeen = seen.get(str[right])!;
            left = Math.max(left, lastSeen + 1);
        }
        seen.set(str[right], right);
        result = Math.max(result, right - left + 1);
    }
    return result;
}
