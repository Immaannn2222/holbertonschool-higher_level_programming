#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const dictt = {};
    for (let i = 0; i < JSON.parse(body).length; i++) {
      const user = JSON.parse(body)[i];
      if (user.userId in dictt && user.completed === true) {
        dictt[user.userId] += 1;
      } else if (!(user.userId in dictt) && user.completed === true) {
        dictt[user.userId] = 1;
      }
    }
    console.log(dictt);
  } else {
    console.log(error);
  }
});
