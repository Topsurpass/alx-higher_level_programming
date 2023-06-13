#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}
const ans = factorial(Number(process.argv[2]));
console.log(ans);
