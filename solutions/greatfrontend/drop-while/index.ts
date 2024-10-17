export default function dropWhile<T>(
  array: Array<T>,
  predicate: (value: T, index: number, array: Array<T>) => boolean,
): Array<T> {
  let i = 0;
  while (i < array.length && predicate(array[i], i, array)) {
    i++;
  }
  return array.slice(i);
}
