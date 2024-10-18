export default function get<T>(
  objectParam: Record<string, any>,
  pathParam: string | Array<string>,
  defaultValue?: T,
): T {
  const params = Array.isArray(pathParam) ? pathParam : pathParam.split(".");
  let result = objectParam;

  for (const param of params) {
    if (result == null || !result.hasOwnProperty(param)) {
      return defaultValue!;
    }
    result = result[param];
  }

  return (result === undefined ? defaultValue : result) as T;
}
