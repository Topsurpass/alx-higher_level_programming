#!/usr/bin/node

const list = require('./100-data.js').list;

const newArr = list.map((n, i) => n * i);
console.log(list);
console.log(newArr);
