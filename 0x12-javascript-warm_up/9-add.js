#!/usr/bin/node

function add (a, b) {
  console.log(Number(a) + Number(b));
}
add(process.argv[2], process.argv[3]);
