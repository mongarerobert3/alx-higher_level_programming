#!/usr/bin/node

// file system
const fs = require('fs');
const filename = process.argv[3];

// Including the request module
const request = require('request');
const url = process.argv[2];

request(url, function (err, header, body) {
  if (err) {
    console.error(err);
  }
  fs.writeFile(filename, body, 'utf-8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
