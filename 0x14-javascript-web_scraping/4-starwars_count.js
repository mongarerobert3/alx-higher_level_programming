#!/usr/bin/node

// Star wars API

// Including the request module
const request = require('request');
const url = process.argv[2];

request(url, function (err, request, body) {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body).results;
  let presentIn = 0;

  for (const dataindex in data) {
    const filmCharacters = data[dataindex].characters;

    for (const charindex in filmCharacters) {
      if (filmCharacters[charindex].includes('18')) {
        presentIn++;
      }
    }
  }
  console.log(presentIn);
});
