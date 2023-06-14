#!/usr/bin/node

const fs = require('fs');
const filePathA = process.argv[2];
const filePathB = process.argv[3];
const filePathC = process.argv[4];

const fileA = fs.readFileSync(filePathA, 'utf8');
const fileB = fs.readFileSync(filePathB, 'utf8');

fs.writeFileSync(filePathC, fileA + fileB);
