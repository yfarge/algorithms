export default function pairSum(numbers: number[], target: number): number[] {
  const seen: Map<number, number> = new Map();
  for (let i = 0; i < numbers.length; ++i) {
    const complement = target - numbers[i];
    if (seen.has(complement)) {
      return [seen.get(complement)!, i];
    }
    seen.set(numbers[i], i);
  }
  return [];
}
