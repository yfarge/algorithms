export default function maxSumSubArray(numbers: number[]): number {
  let currentMax = numbers[0];
  let result = numbers[0];

  for (let i = 1; i < numbers.length; ++i) {
    currentMax = Math.max(currentMax + numbers[i], numbers[i]);
    result = Math.max(result, currentMax);
  }

  return result;
}
