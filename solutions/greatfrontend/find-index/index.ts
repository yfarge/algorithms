export default function findIndex<T>(
  array: Array<T>,
  predicate: (value: T, index: number, array: Array<T>) => boolean,
  fromIndex = 0,
): number {
  let index = fromIndex < 0 ? Math.max(fromIndex + array.length, 0) : fromIndex;
  for (index; index < array.length; index++) {
    if (predicate(array[index], index, array)) return index;
  }
  return -1;
}
