interface Function {
  myApply(this: any, thisArg: any, argArray?: any[]): any;
}

Function.prototype.myApply = function (thisArg, args = []) {
  return this.bind(thisArg, ...args)();
};
