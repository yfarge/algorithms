export default function chunk<T>(array: Array<T>, size = 1): Array<Array<T>> {
  if (!Array.isArray(array) || size <= 0) {
    return [];
  }

  const result: Array<Array<T>> = [];

  for (let i = 0; i < array.length; i++) {
    const element = array[i];
    if (i % size == 0) {
      result.push([]);
    }
    result[result.length - 1].push(element);
  }

  return result;
}
