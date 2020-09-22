#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  else if (response.statusCode === 200) {
    let i = 0;
    const resultt = JSON.parse(body).results;
    const actor = '/api/people/18/';
    for (let j = 0; j < resultt.length; j++) {
      if (resultt[j].characters.find(x => x.includes(actor))) {
        i++;
      }
    }
    console.log(i);
  }
});
