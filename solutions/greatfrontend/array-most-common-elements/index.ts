export default function mostCommonElements(
  numbers: number[],
  k: number,
): number[] {
  const counter: { [key: number]: number } = {};
  for (const num of numbers) {
    counter[num] = (counter[num] || 0) + 1;
  }

  const buckets: number[][] = Array(numbers.length + 1)
    .fill(null)
    .map(() => []);

  for (const num in counter) {
    const count = counter[num];
    buckets[count].push(Number(num));
  }

  const result: number[] = [];
  for (let i = buckets.length - 1; i > 0 && k > 0; --i) {
    if (buckets[i].length == 0) {
      continue;
    }

    for (const num of buckets[i]) {
      result.push(num);
      k--;
      if (k == 0) break;
    }
  }

  return result;
}
