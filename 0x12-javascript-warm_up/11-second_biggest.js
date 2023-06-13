#!/usr/bin/node

const arr = process.argv.slice(2);

function secondBiggest (array) {
  let ans;
  if (array.length === 0 || array.length === 1) {
    return (0);
  } else {
    array.sort((a, b) => b - a);
    array.shift();
    ans = array.shift();
    return (ans);
  }
}
const ans = secondBiggest(arr);
console.log(ans);
