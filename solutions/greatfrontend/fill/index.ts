export default function fill<T>(
  array: Array<T>,
  value: any,
  start: number = 0,
  end: number = array.length,
): Array<T> {
  const length = array.length;
  start = start < 0 ? start + length : start;
  end = end < 0 ? end + length : end;
  if (start > length) {
    return array;
  }

  if (end > length) {
    end = length;
  }

  for (let i = start; i < end; i++) {
    array[i] = value;
  }

  return array;
}
