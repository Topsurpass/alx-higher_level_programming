#!/usr/bin/node

/*
 * argv[0] = path where the node program is located
 * argv[1] = path to the file being executed
 * argv[2] = the first argument passed to the program
 */

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
