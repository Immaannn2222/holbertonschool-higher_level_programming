#!/usr/bin/node
const request = require('request');
const U_R_L = 'https://swapi-api.hbtn.io/api/films/';
request(U_R_L, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let i = 0;
    const resultt = JSON.parse(body).results;
    for (let j = 0; j < resultt.length; j++) {
      if (resultt[i].characters.find(el => el.includes('/api/people/18/'))) {
        i++;
      }
    }
    console.log(i);
  }
});
