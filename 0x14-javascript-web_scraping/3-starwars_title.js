#!/usr/bin/node
const request = require('request');
const U_R_L = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(U_R_L, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
