#!/usr/bin/node

function factorial (a) {
  a = parseInt(process.argv[2]);

  let ans = 1;

  for (let i = 2; i <= a; i++) { ans = ans * i; }

  console.log(ans);
}
factorial();
