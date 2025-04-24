export default function staircaseClimbingCombinations(steps: number): number {
  const memo: Map<number, number> = new Map();
  function backtrack(total: number): number {
    if (memo.has(total)) {
      return memo.get(total)!;
    }

    if (total === steps) {
      return 1;
    }

    if (total > steps) {
      return 0;
    }

    const result = backtrack(total + 1) + backtrack(total + 2);
    memo.set(total, result);
    return result;
  }

  return backtrack(0);
}
