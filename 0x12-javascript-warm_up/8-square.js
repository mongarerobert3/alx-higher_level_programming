#!/usr/bin/node

const arg = parseInt(process.argv[2]);
const message = 'X';

if (isNaN(arg)) {
  console.log('Missing size');
}

for (let i = 0; i < arg; i++) {
  console.log(message.repeat(arg));
}
