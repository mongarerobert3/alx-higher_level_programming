#!/usr/bin/node

// Script that writes to a file

// FileSystem
const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

fs.writeFile(file, string, 'utf-8', function (err, content) {
  if (err) {
    console.error(err);
  }
});
