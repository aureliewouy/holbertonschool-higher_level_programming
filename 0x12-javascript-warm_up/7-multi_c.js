#!/usr/bin/node
const args = process.argv.slice(2);
const arg = args[0];
let i;
if (parseInt(arg) && arg !== undefined) {
  for (i = 0; i < arg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
