#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  console.error('error:', error);
  console.log('code:', response.statusCode);
});
