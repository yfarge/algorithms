export default function combinationTargetSum(
    numbers: number[],
    target: number,
): number {
    const dp: number[] = new Array(target + 1).fill(0);
    dp[0] = 1;

    for (let sum = 1; sum <= target; sum++) {
        for (const num of numbers) {
            if (sum - num >= 0) {
                dp[sum] += dp[sum - num];
            }
        }
    }

    return dp[target];
}

