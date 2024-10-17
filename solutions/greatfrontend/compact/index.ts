export function isDefined<T>(
  value: T | null | undefined | false | 0 | "",
): value is T {
  return Boolean(value);
}

export default function compact<T>(
  array: Array<T | null | undefined | false | 0 | "">,
): Array<T> {
  return array.filter(isDefined);
}
