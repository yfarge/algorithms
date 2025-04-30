export default function longestIncreasingSubsequence(
    numbers: number[],
): number {
    const dp: number[] = Array(numbers.length).fill(1);
    for (let i = 1; i < numbers.length; ++i) {
        for (let j = 0; j < i; ++j) {
            if (numbers[i] > numbers[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
    }
    return Math.max(...dp);
}
