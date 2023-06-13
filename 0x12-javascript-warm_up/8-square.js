#!/usr/bin/node

const argv1 = process.argv[2];

if (!Number(argv1)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv1; i++) {
    let output = '';
    for (let j = 0; j < argv1; j++) {
      output += 'X';
    }
    console.log(output);
  }
}
