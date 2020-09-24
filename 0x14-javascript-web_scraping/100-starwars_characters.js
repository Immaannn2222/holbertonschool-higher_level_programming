#!/usr/bin/node
const request = require('request');
const address = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(address, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const cast = JSON.parse(body).characters;
    for (let j = 0; j < cast.length; j++) {
      request.get(cast[j], function (e, r, b) {
        console.log(JSON.parse(b).name);
      });
    }
  }
});
