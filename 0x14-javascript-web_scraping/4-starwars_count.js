#!/usr/bin/node
const request = require('request');
const U_R_L = 'https://swapi-api.hbtn.io/api/films';
request(U_R_L, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if ('response.statusCode === 200') {
    let i = 0;
    const resultt = JSON.parse(body).results;
    const actor = '/api/people/18/';
    for (let j = 0; j < resultt.length - 1; j++) {
      if (resultt[i].characters.find(x => x.includes(actor))) {
        i++;
      }
    }
    console.log(i);
  }
});
