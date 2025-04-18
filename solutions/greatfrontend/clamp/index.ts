export default function clamp(
  value: number,
  lower: number,
  upper: number,
): number {
  return Math.max(lower, Math.min(value, upper))
}
