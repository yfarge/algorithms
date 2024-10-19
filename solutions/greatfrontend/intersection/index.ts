export default function intersection<T>(...arrays: Array<Array<T>>): Array<T> {
  if (arrays.length === 0) {
    return [];
  }

  const result = new Set<T>(arrays[0]);

  for (let i = 1; i < arrays.length; i++) {
    result.forEach((value) => {
      if (!arrays[i].includes(value)) {
        result.delete(value);
      }
    });
  }
  return Array.from(result);
}

