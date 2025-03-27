export default function findInRotatedArray(
  numbers: number[],
  target: number,
): number {
  let left = 0;
  let right = numbers.length - 1;

  while (left <= right) {
    let mid = Math.trunc((left + right) / 2);

    if (numbers[mid] == target) {
      return mid;
    }

    if (numbers[mid] >= numbers[left]) {
      if (target > numbers[mid] || target < numbers[left]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    } else {
      if (target < numbers[mid] || target > numbers[right]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
  }
  return -1;
}
