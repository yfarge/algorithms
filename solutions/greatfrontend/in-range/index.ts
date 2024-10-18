export default function inRange(
  value: number,
  start: number,
  end?: number,
): boolean {
  if (end === undefined) {
    end = start;
    start = 0;
  }

  if (start < end) {
    return start <= value && value < end;
  }

  return end <= value && value < start;
}
