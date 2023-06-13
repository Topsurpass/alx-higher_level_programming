#!/usr/bin/node

const arr = 'C is fun';

if (!Number(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(arr);
  }
}
