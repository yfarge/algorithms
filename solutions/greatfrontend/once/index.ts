type Fn<T> = (this: any, args: Array<any>) => T;

export default function once<T>(func: Fn<T>): Fn<T> {
  let called = false;
  let result: T;
  return function (this, ...args) {
    if (called) {
      return result;
    }
    called = true;
    result = func.apply(this, args);
    return result;
  };
}
