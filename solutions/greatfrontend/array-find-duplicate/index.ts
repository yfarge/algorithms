export default function findDuplicates(numbers: number[]): boolean {
  const set = new Set();

  for (const num of numbers) {
    if (set.has(num)) {
      return true;
    }
    set.add(num);
  }

  return false;
}
