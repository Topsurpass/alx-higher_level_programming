#!/usr/bin/node

const argv1 = process.argv[2];

if (!argv1 || !Number(argv1)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Number(argv1)}`);
}
