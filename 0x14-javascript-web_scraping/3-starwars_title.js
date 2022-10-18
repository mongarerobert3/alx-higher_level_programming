#!/usr/bin/node

//Star wars API

// Including the request module
const request = require('request');
const id = (process.argv[2])
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
