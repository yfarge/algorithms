export default function gridDistinctPaths(m: number, n: number): number {
  const memo: Map<string, number> = new Map();
  function backtrack(row: number, col: number): number {
    if (row < 0 || row >= m || col < 0 || col >= n) {
      return 0;
    }

    if (memo.has(`${row},${col}`)) return memo.get(`${row},${col}`)!;

    if (row === m - 1 && col === n - 1) {
      return 1;
    }

    const result = backtrack(row + 1, col) + backtrack(row, col + 1);
    memo.set(`${row},${col}`, result);
    return result;
  }

  return backtrack(0, 0);
}
