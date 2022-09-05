#!/usr/bin/node

const arg = parseInt(process.argv[2]);
let argscount = 0;

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
}
while (argscount < arg) {
  console.log('C is fun');
  argscount++;
}
