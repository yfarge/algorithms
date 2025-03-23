export default function arrayReachableEnd(numbers: number[]): boolean {
  const n = numbers.length;
  if (n <= 1) return true;

  const queue: number[] = [0];
  const visited: Set<number> = new Set();

  while (queue.length > 0) {
    const current = queue.shift()!;
    for (let i = 1; i <= numbers[current]; ++i) {
      const next = current + i;
      if (next >= n - 1) return true;
      if (!visited.has(next)) {
        visited.add(next);
        queue.push(next);
      }
    }
  }
  return false;
}
