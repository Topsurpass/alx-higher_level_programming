#!/usr/bin/node

exports.esrever = function (list) {
  const newArr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newArr.push(list[i]);
  }
  return newArr;
};
