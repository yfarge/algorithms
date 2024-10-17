export default function difference<T>(
  array: Array<T>,
  values: Array<T>,
): Array<T> {
  const toBeRemoved = new Set(values);
  return array.filter((value) => !toBeRemoved.has(value));
}

