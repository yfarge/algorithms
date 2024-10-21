export default function maxBy<T>(
  array: Array<T>,
  iteratee: (value: T) => any,
): any {
  let max, result;

  for (const item of array) {
    const current = iteratee(item);
    if (current != null && (max == null || current > max)) {
      result = item;
      max = current;
    }
  }
  return result;
}
