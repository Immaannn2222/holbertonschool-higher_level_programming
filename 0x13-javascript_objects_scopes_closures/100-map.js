#!/usr/bin/node
const l = require('./100-data').list
const result = l.map((x, i) => x * i);
console.log(l);
console.log(result);
