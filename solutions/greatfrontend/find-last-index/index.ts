export default function findLastIndex<T>(
  array: Array<T>,
  predicate: (value: T, index: number, array: Array<T>) => boolean,
  fromIndex = array.length - 1,
): number {
  const length = array.length;
  let index = fromIndex >= 0 ? fromIndex : Math.max(fromIndex + length, 0);

  for (index; index >= 0; index--) {
    if (predicate(array[index], index, array)) {
      return index;
    }
  }
  return -1;
}
